##Note: The link for the application is http://13.53.177.53:8501 please paste it in any browser for accesing the application

# Creating a YouTube like application

## Getting the data from youtube
Run the "Final_Youtube_data_scraping.ipynb" file by giving google api keys it will download the video data raw data from YouTube

## Pushing the raw data to S3 bucket
Run the "pushing raw json file to AWS S3.ipynb" file by giving the keys from the IAM user in AWS and the respective bucket keys and stuff this will push the raw data to AWS S3 bucket

## Pulling the raw data from S3 bucket and cleaning the data and push it to RDS SQL database
Run the "pulling data form s3 and Youtube_Data_Cleaning_and_pushing_to_AWS_RDS.ipynb" file by giving the keys from the IAM user in AWS and the respective bucket keys to pull the RAW data from S3 and clean the data and push it back to RDS SQL for clustering

## Pulling the cleaned data from AWS RDS and TFIDF Hierarchical clustering
Run the "Pulling_from_AWS_RDS_and_TFIDF_Hierarchial_clustering.ipynb" file by giving the required security keys of the respective RDS database and then it will make the clustering and will save the output pickel files

## Making the GitHub Repository
Make a git hub repository like this one with the same requirements.txt, Pickle file outputs from the hierarchical clustering, youtube_data.xlsx file and the capstone.py file whcih contains the code for using the outputs to run a streamlit application.

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone https://github.com/monishavenkatesh7/ML-Capstone-project.git
```
this is my repository you can change to yours accordingly

```bash
cd ML-Capstone-project
```
this is my repository you can change to yours accordingly

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```
Note: If the above one doesnt work
```bash
pip install -r requirements.txt --break-system-packages
```

#Temporary running
```bash
python3 -m streamlit run capstone.py
```
change the file name to your streamlit application file name

#Permanent running
```bash
nohup python3 -m streamlit run capstone.py
```
change the file name to your streamlit application file name
Note: Streamlit runs on this port: 8501

#For reloading the git
```bash
git pull origin main
```

#For Terminating the permanently running application
```bash
sudo pkill -f streamlit
```

