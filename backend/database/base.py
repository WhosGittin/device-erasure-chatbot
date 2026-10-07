from datetime import datetime
from typing import Protocol

from backend.models import ErasureRecord

#Interface for database tools to ensure that any implementation provides the required methods for interacting with erasure records.
class DatabaseTools(Protocol):
# Retrieve an erasure record by its serial number.
    def get_by_serial_number(
        self,
        serial_number: str,
    ) -> ErasureRecord | None:  
        ...

#Search for erasure records based on manufacturer, status, and/or date.
    def search(
        self,
        manufacturer: str | None = None,
        status: str | None = None,
        erasure_date: datetime | None = None,
    ) -> list[ErasureRecord]:
        ...

#Count the number of erasure records that match the given parameters.
    def count(
        self,
        manufacturer: str | None = None,
        status: str | None = None,
        erasure_date: datetime | None = None,
    ) -> int:
        ...