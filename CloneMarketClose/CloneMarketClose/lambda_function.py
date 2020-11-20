import boto3
import io
import yfinance as yf
from datetime import date, timedelta
import datetime
import pandas as pd
import xlrd


def lambda_handler(event, context):
    if event:
        df = s3_read()
        today, yest = todays_date()
        text = update(df, today, yest)
        stringtext = listToString(text)
        client = boto3.client('sns')
        response = client.publish(
            PhoneNumber='+15089817709',
            Message = stringtext,
            Subject='Update',
)
        return text
    
    
def s3_read():
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='tickercto', Key='TICKER.xlsx')
    contents = data['Body'].read()
    read_excel_file = io.BytesIO(contents)
    df = pd.read_excel(read_excel_file)
    return df   
    
    
def update(df, today, yest):
    stocklist = []
    for ind, tick in enumerate(df['Ticker']):
        appendlist =[]
        stock = yf.download(tick, yest)
        yestclose = stock.iloc[0,3]
        todayclose = stock.iloc[1,3]
        close = round(stock.iloc[1,3],2)
        change = (todayclose - yestclose)/yestclose
        percentage = "{:.2%}".format(change)
        stocklist.append(f"\n {tick} - Closing Price: ${close}, DoD: {percentage}")
    return stocklist


def todays_date():
    today = date.today()
    dayofweek = datetime.datetime.today().weekday()
    if (dayofweek == 6):
        pass

    elif (dayofweek == 5):
        pass
    
    elif (dayofweek == 0):
        yest = today - timedelta(days=3)
        today = today.strftime("%Y-%m-%d")
        return today, yest
    
    else:
        yest = today - timedelta(days=1)
        today = today.strftime("%Y-%m-%d")
        return today, yest
        
        
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele + ' '  
    return str1  