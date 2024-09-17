from PIL import Image
import pytesseract
import json
import schedule
import time
from datetime import datetime, timedelta
import re

screenshot_path = 'macros.png' #/storage/emulated/0/Pictures/Macros/macros.png

def extract_nutrition_info(text):
    # Print extracted text for debugging
    print("Extracted Text:\n", text)
    lines = text.split('\n')
    matches = re.findall(r'(\d+)(?=/\d+g)', text)

    # Use regex to find Carbohydrates, Protein, and Fat values
    '''    carbs_match = re.search(r'(\d+)(?=/\d+g)', text)
    protein_match = re.search(r'(\d+)(?=/\d+g)', lines[2])
    '''
    fat_match = re.search(r'(\d+)(?=/\d+ g)', text)
    
    # Print regex matches for debugging
    print("matches:", matches)

    
    # Extract values if found
    '''carbs = carbs_match.group(1) if carbs_match else None
    protein = protein_match.group(1) if protein_match else None'''
    fat = fat_match.group(1) if fat_match else None

    carbs = matches[0] if len(matches) > 0 else None
    protein = matches[1] if len(matches) > 1 else None

    return carbs, protein, fat

def process_screenshot():
    image = Image.open(screenshot_path)

    extracted_text = pytesseract.image_to_string(image)
    carbs, protein, fat = extract_nutrition_info(extracted_text)
    print("Extracted Text:\n", extracted_text)

    data = {
            'timestamp': datetime.now().isoformat(),
            'Carbohydrates': carbs,
            'Protein': protein,
            'Fat': fat
        }

    json_data = json.dumps(data, indent=4)

    print(json_data)
    with open('macros.json',  'w') as json_file:  #/storage/emulated/0/Pictures/Macros/macros.png'
        json_file.write(json_data)

def job():

    process_screenshot()

def time_until_next_run(run_time="06:00"):
    now = datetime.now()
    next_run = datetime.combine(now.date(), datetime.strptime(run_time, "%H:%M").time())

    if now>= next_run:
        next_run += timedelta(days=1)
    return (next_run - now).total_seconds()


schedule.every().day.at("06:00").do(job)

'''while True:
    schedule.run_pending()
    sleep_duration = time_until_next_run("06:00")
    time.sleep(sleep_duration)
'''
job()
