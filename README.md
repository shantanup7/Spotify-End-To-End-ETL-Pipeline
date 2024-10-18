# Spotify End To End ETL Pipeline

### Description
In this project, we will build an automated ETL pipeline leveraging AWS services to extract, transform, and load data from Spotify's top playlists weekly. This repository contains Python scripts for data extraction, transformation, and loading, along with an architecture diagram and setup instructions.

### Architecture Diagram
![Architecture Diagram](https://github.com/shantanup7/Spotify-End-To-End-ETL-Pipeline/blob/main/Architecture%20Diagram.png)

### Dataset Used
This project leverages the [Spotify Web API](https://developer.spotify.com/documentation/web-api) to access real-time data from Spotify's top playlists. The API facilitates the retrieval of extensive metadata about music tracks, albums, and artists. For this project, the [Anjunadeep 2024](https://open.spotify.com/playlist/2wSNKxLM217jpZnkAgYZPH?si=d51da583ba504452) playlist was specifically utilized as a primary data source, but the setup is designed to be flexible. Users can easily adapt the code to analyze any playlist of their choice by changing the playlist ID in the extraction script.

![Anjunadeep 2024](https://github.com/shantanup7/Spotify-End-To-End-ETL-Pipeline/blob/main/Images/Anjunadeep%202024.jpg)

Here's a brief overview of the type of data we collect:
- **Tracks:** Song titles, artists, and duration.
- **Albums:** Album names, release dates, and track counts.
- **Artists:** Artist names and related metadata.

### Services Used

- **AWS S3 (Simple Storage Service):** Amazon S3 (Simple Storage Service) is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web. It is commonly used to store and distribute large media files, data backups, and static website files.

- **AWS Lambda:** AWS Lambda is a serverless computing service that lets you run your code without managing servers. You can use Lambda to run code in response to events like changes in S3, DynamoDB, or other AWS services.

-  **AWS CloudWatch:** Amazon CloudWatch is a monitoring service for AWS resources and the applications you run on them. You can use CloudWatch to collect and track metrics, collect and monitor log files, and set alarms.

-  **AWS Glue Crawler:** AWS Glue Crawler is a fully managed service that automatically crawls your data sources, identifies data formats, and infers schemas to create an AWS Glue Data Catalog.

- **AWS Data Catalog:** AWS Glue Data Catalog is a fully managed metadata repository that makes it easy to discover and manage data in AWS. You can use the Glue Data Catalog with other AWS services, such as Athena.

- **Amazon Athena:** Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. You can use Athena to analyze data in your Glue Data Catalog or in other S3 buckets.

### Installed Packages
```
pip install pandas
pip install numpy
pip install spotipy
```

### Project Execution Flow

**Extract Data from API:**
- The process begins with the extraction of data from Spotify's API using a Python script deployed on AWS Lambda. This script specifically targets Spotify's top playlists to gather data about tracks, albums, and artists.
- Frequency: The Lambda function is set to execute once a week.

**Lambda Trigger (every 1 week):**
- An AWS CloudWatch event is scheduled to trigger the AWS Lambda function weekly. This ensures that the data is consistently updated to reflect the latest trends and changes in Spotify playlists.
  
**Run Extract Code:**
- Once triggered, the AWS Lambda function runs the extraction code, which makes calls to the Spotify API, retrieves data, and processes it to ensure it is in the correct format for storage.
  
**Store Raw Data:**
- The raw data fetched from the API is stored in an AWS S3 bucket. This acts as the initial landing zone for the data before transformation. The raw data is stored in JSON format, preserving the original structure as received from Spotify.
  
**Trigger Transform Function:**
- A new AWS Lambda function is triggered automatically once the raw data is successfully stored in S3. This function is responsible for transforming the raw data into a more analytics-friendly format.
  
**Transform Data and Load it:**
- The transformation process includes cleaning, normalizing, and structuring the data according to the predefined schema that supports easier analysis and querying.
After transformation, the cleaned data is loaded back into a different S3 bucket or folder designated for transformed data.

**Query using Athena:**
- With the transformed data stored in S3 and cataloged using AWS Glue Crawler, it becomes queryable using Amazon Athena.
Amazon Athena allows users to run SQL queries directly against the dataset stored in S3, providing insights into the music trends, popular tracks, artists, and albums from the Spotify playlists.
