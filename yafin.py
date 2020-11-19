import boto3
import io
import yfinance as yf
from datetime import date, timedelta
import datetime
#import numpy as np
import pandas as pd

#def ticker(bucket, name):
    #s3 = boto3.client('s3')
    #print(f"This is the ticker {bucket} and the name {name}")
    #bucket_name = str(s3["s3"]["bucket"]["name"])
    #print(bucket_name)

#def lambda_handler(event, context):
def s3_read():
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='tickercto', Key='TICKER.xlsx')
    contents = data['Body'].read()
    read_excel_file = io.BytesIO(contents)
    df = pd.read_excel(read_excel_file)
    return df

def Lambda():
    df = s3_read()
    today, yest = todays_date()
    text = update(df, today, yest)
    print(text)
#print(df)
#for ind, tick in df.iteritems():
 #   print(ind, tick.values)
def update(df, today, yest):
    stocklist = []
    for ind, tick in enumerate(df['Ticker']):
        appendlist =[]
        stock = yf.download(tick, yest)
        #print(stock.iloc[0,3])
        #stocklist.append(stock)
        yestclose = stock.iloc[0,3]
        todayclose = stock.iloc[1,3]
        close = round(stock.iloc[1,3],2)
        change = (todayclose - yestclose)/yestclose
        percentage = "{:.2%}".format(change)
        stocklist.append(f"{tick} closed: ${close} DoD change: {percentage}")
    return stocklist
        #stocklist.append(f"{tick} closed: ${close} DoD: ${percentage}")
    #return tick, stocklist
        

def todays_date():
    today = date.today() - timedelta(days=1)
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
        







#LOG = logging.getLogger()
#LOG.setLevel(logging.INFO)
#logHandler = logging.StreamHandler()
#formatter = jsonlogger.JsonFormatter()
#logHandler.setFormatter(formatter)
#LOG.addHandler(logHandler)