# Stock-Notification
AWS Lambda project to work with stock notifications

Link to Project Demo: https://youtu.be/adZrlpoFcyU

## Project Ecosystem Graphic
![AWS Lambda Ecosystem](https://user-images.githubusercontent.com/68971919/100132446-6c5b0600-2e53-11eb-8e24-9a2bec9036a9.jpg)


#Overview
In this project I created an automated AWS Lambda function to send me daily text message notifications on my stock portfolio's performance. This incorporated S3, Lambda, Cloudwatch triggers, and SNS from the AWS product suite.  

#Project Infrastructure:
I created this project in the AWS Cloud9 enviroment connected to Github via SSH key. I have set up a makefile to download python packages needed to run the lambda function such as boto3, pylint, Pandas, yfinance, datetime and xlrd. The makefile also is used to lint the code, and identify any bugs in the process. This helps with automating the data pipeline. Within the actions of GitHub, I have set it up so that it automatically lints before it can push to github. 

#Code
The Lambda function is triggered to run every Monday through Friday at 5pm by an AWS Cloud watch timer. The Lamda handler function which receives this trigger then uses boto3 to connect to 23 and extract the information from the bucket I needed. I then extracted the information from the file uploaded to s3 (in this case, the stock tickers) and put them into a dataframe. Before feeding this ticker into the yahoo finance API to extract the info I wanted, I also needed to grab the date, and yesterdays date using the datetime package. Once I had the tickers, date, and yesterdays date, I could use this to extract the closing stock price, yesterdays closing price, and the day overday change for each stock in my portfolio. I then formatted them as a string which is a requirement for Simple Notification Services. This formatted data is sent back to my lambda Handler function which uses boto3 to connect to the SNS group I want this information sent out to. In this case, SNS group is formatted to be sent out as an SMS sent to my phone. 


#Future plans
I would like to potentially incorporate an additional component that scrapes a website to give a quick blurb about daily news associated with each of the stocks. However, I have not find a great website that allows scraping for this portion of it. I would also like to create a front in interface that allows anyone to upload their portfolio and preferred message settings to receive their own messages. 

