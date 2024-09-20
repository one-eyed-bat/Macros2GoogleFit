from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import datetime
SERVICE_ACCOUNT_FILE = '/black_resource.json'
SCOPES = ['https://www.googleapis.com/auth/fitness.nutrition.write']
def initialize_google_fit_service():
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('fitness', 'v1', credentials=credentials)
  
def insert_nutrition_data(service, carbs, protein, fat):
     data = {
             "startTimeMillis": int(datetime.now().timestamp() * 1000),
             "endTimeMillis": int((datetime.datetime.now() + datetime.timedelta(minutes=1)).timestamp() * 1000),
             "valeu": [
                 {
                     "name": "Carbohydrate",
                     "value": carbs
                     },
                  {
                     "name": "Protein",
                     "value": protein
                     },
                 {"name": "Fat",
                  "value": fat
                  }
                 ],
             "type": "com.google.nutrition"
             }
     request = service.users().dataSrouces().datasets().patch(
             userId='me',
             dataSourceId='your-dataset-id',
             body=data
             )
     response = request.execute()
     return response
 
def main():
    service = initialize_google_fit_service()

    carbs = 200
