from __future__ import print_function

from googleapiclient.discovery import build
from google.oauth2 import service_account

import pandas as pd
import requests
from datetime import date
import xmltodict
from sqlalchemy import create_engine
import time

# Create database connection engine 
engine = create_engine('postgresql://postgres:password@db/googledata')

# Authorisation info for retriewing data from googlesheet
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

# As we created service account for api, we use its credentials
credo = None
credo = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of spreadsheet
SAMPLE_SPREADSHEET_ID = '10KFiOJ8vuE3eX9ysA_KTjySfkheDP4xVOds91C-7r7E'

# We need this to run endless
flag=True

# Get todays data
today = date.today()
d1 = today.strftime("%d/%m/%Y")

# Parse xml info about $ -> Rub conver (we can put it in a loop with 24 hours sleep for example)
url="https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ=R01235".format(d1,d1)
res = requests.get(url)
dict_data = xmltodict.parse(res.content)
price_rub = (dict_data["ValCurs"]["Record"]["Value"]).replace(',', '.')

while flag: 
        service = build('sheets', 'v4', credentials=credo)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="List1!A1:D51").execute()

        values = result.get('values', [])

        # Create dataframe from spreadsheet's data
        df = pd.DataFrame(values, columns=['Num', 'Order number', 'Price_usd', 'Date'])       

        # Add column with prices in rubles
        df["Price_rub"] = (df['Price_usd'].iloc[1:]).apply(lambda x: float(x)*float(price_rub))

        # Write dataframe to database and rewrite table if exist (we could compare dataframe and write only differences)
        df[1:].to_sql('orders', engine, if_exists='replace', index=False)
        time.sleep(1)

