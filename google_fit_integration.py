from google_oauth2 import service_account
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
            :
