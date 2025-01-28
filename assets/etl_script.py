import boto3
from sqlalchemy import create_engine
import pandas as pd
import logging
import os

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('application.log'),  
        logging.StreamHandler()  
    ]
)

DATABASE_URL = "postgresql+psycopg2://postgres:5629@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='XXXXXXXXXXXX',
    aws_secret_access_key='XXXXXXXXXXXXXX'
)

def load_data_from_s3(s3_resource, bucket_name, file_key, file_name):
    """
    Downloads data from S3 and returns it as a DataFrame.
    """
    try:
        logging.info(f"Downloading file '{file_key}' from bucket '{bucket_name}'.")
        s3_resource.Bucket(bucket_name).download_file(Key=file_key, Filename=file_name)
        df = pd.read_csv(file_name, index_col=0)
        logging.info("File downloaded and loaded into DataFrame successfully.")
        return df
    except FileNotFoundError:
        logging.error("The specified file does not exist in the bucket.")
        return None
    except boto3.exceptions.S3UploadFailedError as e:
        logging.error(f"Failed to download file from S3: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def data_transform(df):
    """
    Transforms, cleans, and filters the data.
    """
    try:
        logging.info("Starting data transformation.")

        df.reset_index(inplace=True)
        df = df.drop_duplicates(subset='id', keep='first')
        df = df.dropna()
        df['call_timestamp'] = pd.to_datetime(df['call_timestamp'])
        df.rename(columns={'call duration in minutes':'call_duration_in_minutes'}, inplace=True)
        df['State'] = df['call_center'].apply(lambda x: x.split('/')[1] if len(x.split('/')) > 1 else None)
        df['call_duration_in_minutes'] = df['call_duration_in_minutes'].astype(int)
        df['csat_score'] = df['csat_score'].astype(int)
        logging.info("Data transformation completed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        return None

def validate_data(df):
    """
    Validates the data: checks for negative values and incorrect dates.
    """
    if df is None:
        logging.error("Data validation skipped due to previous errors.")
        return False
    
    logging.info("Starting data validation.")
    valid = True

    if 'call_duration_in_minutes' in df.columns and (df['call_duration_in_minutes'] < 0).any():
        logging.warning("Negative values found in 'call_duration_in_minutes'.")
        valid = False

    if 'csat_score' in df.columns and (df['csat_score'] < 0).any():
        logging.warning("Negative values found in 'csat_score'.")
        valid = False

    if 'call_timestamp' in df.columns and (df['call_timestamp'].dt.year < 2020).any():
        logging.warning("Incorrect values found in 'call_timestamp'.")
        valid = False

    if valid:
        logging.info("Data validation passed successfully.")
    else:
        logging.error("Data validation failed.")

    return valid

def upload_to_postgresql(df, table_name, engine):
    """
    Uploads the DataFrame to a PostgreSQL database.
    """
    try:
        logging.info(f"Uploading data to PostgreSQL table '{table_name}'.")
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info("Data uploaded successfully.")

    except Exception as e:
        logging.error(f"Failed to upload data to PostgreSQL: {e}")

bucket_name = 'ilk-kovam'
file_key = 'Call Center.csv'
file_name = 'Call Center.csv'

df = load_data_from_s3(s3, bucket_name, file_key, file_name)

if df is not None:
    df = data_transform(df)

if df is not None and validate_data(df):
    logging.info("Data is ready for the next steps.")
    upload_to_postgresql(df, 'call_center_data', engine)  # Upload data to 'call_center_data' table
else:
    logging.error("Data preparation process failed.")
