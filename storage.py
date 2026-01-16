# Import JSON module to enable the process of reading and writing data.
import json
# Import datetime to create and shape timestamps
from datetime import datetime

# File name keeps the records of time card history.
FILE_NAME = "history.json"

def save_timecard(card):
    # Form a dictionary containing the records from the TimeCard object.
    record = {
        "employee": card.employee_name,             # Employee name
        "date": card.date,                          # Time card date
        "total_hours": card.total_hours(),          # Total of work hours
        "timestamp": datetime.now().isoformat()     # Save time of record formation
    }

    try: 
        # Try to open and load available file of history records.
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
    except:
        # If file is unavailable or invalid, create an empty list.
        data = []

    # Post the updated record to the list of history.
    data.append(record)

    # Write the history with its new record in the JSON file.
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)