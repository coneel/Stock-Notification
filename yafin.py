#import boto3
#import yfinance as yf
#from datetime import date, timedelta
#import numpy as np
#import pandas as pd

def ticker(bucket, name):
    #sqs = boto3.client('sqs')
    print(f"This is the ticker {bucket} and the name {name}")


ticker("CHKP", "bar")
    