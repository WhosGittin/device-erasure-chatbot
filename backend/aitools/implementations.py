from datetime import datetime

from backend.database.base import Database

#Retrieve an erasure record by its serial number using the provided database tools.
def get_erasure_by_serial_number(
    database: Database,
    serial_number: str,
) -> dict:

    record = database.get_by_serial_number(serial_number)

    if record is None:
        return {
            "found": False,
            "error": "No record found for the given serial number."
        }

    #Return the erasure record details in a structured format.
    return {
        "found": True,
        "record": {
            "serial_number": record.serial_number,
            "manufacturer": record.manufacturer,
            "model": record.model,
            "erasure_date": record.erasure_date,
            "method": record.method,
            "status": record.status,
            "failure_reason": record.failure_reason,
        },
    }

#Count erasure records that match the given parameters using the provided database tools.
def count_erasures(
    database: Database,
    manufacturer: str | None = None,
    status: str | None = None,
    erasure_date: datetime | None = None,
) -> int:

    count = database.count(
        manufacturer=manufacturer,
        status=status,
        erasure_date=erasure_date
    )

    return {
        "count": count
    }

#Search and return a list of erasure records that match the given parameters using the provided database tools.
def search_erasures(
    database: Database,
    manufacturer: str | None = None,
    status: str | None = None,
    erasure_date: datetime | None = None,
) -> dict:

    records = database.search(
        manufacturer=manufacturer,
        status=status,
        erasure_date=erasure_date,
    )

    return [
        {
            "serial_number": record.serial_number,
            "manufacturer": record.manufacturer,
            "model": record.model,
            "erasure_date": record.erasure_date.isoformat(),
            "method": record.method,
            "status": record.status,
            "failure_reason": record.failure_reason,
        }
        for record in records
    ]