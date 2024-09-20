import json
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Initialize Google Fit service (this is where your `service_account_file` comes in)
def initialize_google_fit_service():
    credentials = service_account.Credentials.from_service_account_file('black-resource.json')
    service = build('fitness', 'v1', credentials=credentials)
    return service

# Read macros from JSON
def read_macros_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    carbs = data.get('Carbohydrates')
    protein = data.get('Protein')
    fat = data.get('Fat')
    
    return carbs, protein, fat

# Send data to Google Fit
def send_nutrition_data(service, carbs, protein, fat, dataSourceId):
    # Example start and end times for dataset
    start_time = int(datetime.datetime.now().timestamp() * 1000)
    end_time = start_time + 60 * 1000
    
    # Dataset ID
    dataset_id = f"{start_time}-{end_time}"
    
    # Prepare the data
    data = {
        "startTimeMillis": start_time,
        "endTimeMillis": end_time,
        "value": [
            {"fpVal": float(carbs)},
            {"fpVal": float(protein)},
            {"fpVal": float(fat)}
        ],
        "dataTypeName": "com.google.nutrition"
    }
    
    # Send data to Google Fit
    request = service.users().dataSources().datasets().patch(
        userId='me',
        dataSourceId=dataSourceId,
        datasetId=dataset_id,
        body=data
    )
    response = request.execute()
    return response

# Main function to call
def main():
    # Initialize the Google Fit service
    service = initialize_google_fit_service()
    
    # Read macros from JSON
    carbs, protein, fat = read_macros_from_json('macros.json')
    
    # Send the data to Google Fit
    dataSourceId = 'your-data-source-id'  # Replace with actual data source ID
    response = send_nutrition_data(service, carbs, protein, fat, dataSourceId)
    
    print(response)

# Run the main function
if __name__ == "__main__":
    main()

