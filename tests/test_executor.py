
from backend.data_loader import load_records
from backend.database.local import LocalDatabase
from backend.aitools.executor import *

def test_executor_get_erasure_by_serial_number():
    # Load test data from the JSON file
    records = load_records("data/example_records.json")
    db = LocalDatabase(records)

    result = execute_tool(
        "get_erasure_by_serial_number",
        {"serial_number": "SN-TEST-0001"},
        db,
    )

    assert result["found"] is True
    assert result["record"]["serial_number"] == "SN-TEST-0001"