from datetime import datetime, timezone

from backend.database.local import LocalDatabase
from backend.aitools.implementations import get_erasure_by_serial_number
from backend.data_loader import load_records


#Test for the get_erasure_by_serial_number function to ensure it 
#correctly retrieves an erasure record by its serial number.
def test_get_erasure_by_serial_number():

    # Load test data from the JSON file
    records = load_records("data/example_records.json")
    db = LocalDatabase(records)

    # Test with an existing serial number
    serial_number = "SN-TEST-0001"
    result = get_erasure_by_serial_number(db, serial_number)
    assert result["found"] is True
    assert result["record"]["serial_number"] == serial_number

#Test for the get_erasure_by_serial_number function to ensure it
#correctly handles the case when no record is found for a given serial number.  
def test_get_erasure_by_serial_number_not_found():
    
    # Load test data from the JSON file
    records = load_records("data/example_records.json")
    db = LocalDatabase(records)

    # Test with a non-existing serial number
    serial_number = "SN-NOT-FOUND"
    result = get_erasure_by_serial_number(db, serial_number)
    assert result["found"] is False