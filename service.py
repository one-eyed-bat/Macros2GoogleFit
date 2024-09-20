from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'black-resource.json'

# Define the required API scopes
SCOPES = ['https://www.googleapis.com/auth/fitness.nutrition.write']

# Create a credentials object from the service account file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize the service object for Google Fit API
service = build('fitness', 'v1', credentials=credentials)

nutrition_data_source = {
    "dataStreamName": "nutrition data",
    "type": "derived",
    "application": {
        "name": "Macros-to-Fit App",
        "version": "1.0"
    },
    "dataType": {
        "name": "com.google.nutrition",
        "field": [
            {"name": "nutrition.carbs", "format": "floatPoint"},
            {"name": "nutrition.protein", "format": "floatPoint"},
            {"name": "nutrition.fat", "format": "floatPoint"}
        ]
    },
    "device": {
        "uid": "12345",
        "type": "phone",
        "model": "Android",
        "manufacturer": "Google"
    }
}

# Create the data source
request = service.users().dataSources().create(userId='me', body=nutrition_data_source)
response = request.execute()

print(response)

