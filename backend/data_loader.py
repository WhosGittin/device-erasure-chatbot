import json

from backend.models import ErasureRecord

#Load erasure records from a JSON file and convert them into ErasureRecord objects.
def load_records(path: str) -> list[ErasureRecord]:
    with open(path) as file:
        data = json.load(file)

    return [
        ErasureRecord.convert_data(record)
        for record in data
    ]

#print(load_records("data/example_records.json"))
