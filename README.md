![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/bar.png)

<div align="center">
  <h1>Call-Center Monthly Performance Dashboard</h1>
 </p>
</div>


## Project Introduction

This project successfully extracts data from the AWS S3 bucket, cleans it and makes it available for analysis. The data is then written to a PostgreSQL database and visualized using Tableau. The dashboard is automatically updated every month, allowing management to analyze performance and trends with the most up-to-date data. This prevents wasted time, accelerates **data-driven decision-making processes** and makes strategic decisions easier.

## Project Steps
![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/digram_new.svg)

+ Extracting Data from AWS S3 Bucket: Using the Boto3 library, data was extracted from the AWS S3 bucket. The extracted data was downloaded in CSV format and loaded into a pandas DataFrame.

+ Data Preparation and Cleaning:
Data preparation and cleaning processes, such as filling missing values and removing erroneous records, were performed on the data. Necessary columns for data analysis were selected, and unnecessary columns were removed. Data types were appropriately converted and normalized.

+ Writing Data to PostgreSQL Database: After completing the data cleaning processes, a connection to the PostgreSQL database was established using the SQLAlchemy library. The cleaned data was written to appropriate tables in the PostgreSQL database.

+ Creating a Dashboard with Tableau: The data was transferred to Tableau by connecting to the PostgreSQL database. In Tableau, data visualizations were created to form a dashboard containing performance and trend analyses. The dashboard includes interactive charts and visuals, enabling users to easily track performance and trends.

+ Regular Updates: The dashboard is configured to be updated automatically every month, ensuring the data is refreshed regularly. This automation system ensures that up-to-date data is continuously available, allowing users to access the most current information.

[Script](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/etl_script.py)

## Snapshot

[Dashboard](https://public.tableau.com/app/profile/atilla.kiziltas/viz/call_center_dashboard/Dashboard3)

![image](https://github.com/AtilaKzlts/Call-Center-Automation/blob/main/assets/call_center.png)


### [**Return to Portfolio**](https://github.com/AtilaKzlts/Atilla-Portfolio)
