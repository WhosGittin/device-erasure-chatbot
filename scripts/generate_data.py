import json
import random
from datetime import datetime, timedelta, timezone

#List of manufacturers, models, methods, and failure reasons for generating random erasure records
MANUFACTURERS = [
    "Apple",
    "Dell",
    "HP",
]

MODELS = [
    "MacBook Pro",
    "XPS 13",
    "Spectre x360",
]

METHODS = [
    "Crypto erase",
    "Manual erase",
    "Secure erase",
]

FAILURES = [
    "Power failure",
    "Device not found",
    "Unsupported device",
    "Unknown error",
]

#Generate a list of random erasure records
def generate_records(count: int = 100) -> list[dict]:

    #For reproducibility
    random.seed(42)

    #Set the start date for generating random erasure dates
    start = datetime(2026, 1, 1)

    #Initialize a list for the random records
    records = []

    #Generate the specified number of random erasure records
    for i in range(1, count + 1):
        date = start + timedelta(
            days=random.randint(0, 180),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )

        #Randomly choose a status for the erasure record
        status = random.choice(["success", "failure"])

        #Create an object representing the erasure record with random values for each field
        record = {
            "serial_number": f"SN-TEST-{i:04d}",
            "manufacturer": random.choice(MANUFACTURERS),
            "model": random.choice(MODELS),
            "erasure_date": date.isoformat(),
            "method": random.choice(METHODS),
            "status": status,
            "failure_reason": (
                random.choice(FAILURES)
                if status == "failure"
                else None
            ),
        }
        records.append(record)
    return records

#Generate 100 random erasure records and save them to a JSON file
if __name__ == "__main__":

    records = generate_records(100)
    with open("data/example_records.json", "w") as file:
        json.dump(records, file, indent=2)

    #Print the number of generated records to the console
    print(f"Generated {len(records)} records.")