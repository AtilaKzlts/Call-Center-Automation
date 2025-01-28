![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/bar.png)

# **Monthy Performance Dashboard**

### Table of Contents

- Project Introduction
- Project Steps
- Conclusion

## Project Introduction

![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/diagram_svg.svg)

The objective of this project is to extract data from an AWS S3 bucket using Python, write the data to a PostgreSQL database, and create a dashboard in Tableau to visualize this data. The dashboard will be updated automatically every month.

## Project Steps

+ Extracting Data from AWS S3 Bucket: Using the Boto3 library, data was extracted from the AWS S3 bucket. The extracted data was downloaded in CSV format and loaded into a pandas DataFrame.

+ Data Preparation and Cleaning:
Data preparation and cleaning processes, such as filling missing values and removing erroneous records, were performed on the data. Necessary columns for data analysis were selected, and unnecessary columns were removed. Data types were appropriately converted and normalized.

+ Writing Data to PostgreSQL Database: After completing the data cleaning processes, a connection to the PostgreSQL database was established using the SQLAlchemy library. The cleaned data was written to appropriate tables in the PostgreSQL database.

+ Creating a Dashboard with Tableau: The data was transferred to Tableau by connecting to the PostgreSQL database. In Tableau, data visualizations were created to form a dashboard containing performance and trend analyses. The dashboard includes interactive charts and visuals, enabling users to easily track performance and trends.

+ Regular Updates: The dashboard is configured to be updated automatically every month, ensuring the data is refreshed regularly. This automation system ensures that up-to-date data is continuously available, allowing users to access the most current information.

[Script](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/etl_script.py)
## Conclusion

This project successfully extracts data from an AWS S3 bucket, cleans and prepares it for analysis, writes it to a PostgreSQL database, and visualizes it using Tableau. The dashboard, which is updated automatically every month, allows users to perform performance and trend analyses with the latest data.

[Dashboard](https://public.tableau.com/app/profile/atilla.kiziltas/viz/call_center_dashboard/Dashboard3)

![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/call_center.png)
