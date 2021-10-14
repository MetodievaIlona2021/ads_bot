from __future__ import print_function

import datetime

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from data.config import YOUR_SPREADSHEET_ID, RANGE_TABLE_NAME

SAMPLE_RANGE_NAME = RANGE_TABLE_NAME


class GoogleSheet:
    SPREADSHEET_ID = YOUR_SPREADSHEET_ID
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

    def read_range_values(self, range_, major_dimension='ROWS'):
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.SPREADSHEET_ID,
            range_=range_,
            majorDimension=major_dimension
        ).execute()

        print(values)
        exit()

    def update_range_values(self, range_, values):
        data = [{
            'range': range_,
            'values': values
        }]

        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                  body=body).execute()
        print(f'{result.get("totalUpdatedCells")} cells updated.')

    def append_range_values(self, range_, values):
        range_ = range_
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        value_range_body = {
            'values': values
        }

        result = self.service.spreadsheets().values().append(spreadsheetId=self.SPREADSHEET_ID,
                                                             range=range_,
                                                             valueInputOption=value_input_option,
                                                             insertDataOption=insert_data_option,
                                                             body=value_range_body).execute()

        updates = result.get('updates')

        print(f'Данные успешно добавлены!\n{updates}')
