# Using protocol to make sure ErasureRecord-object provides the required methods
from typing import Protocol

from backend.models import ErasureRecord


class ErasureDatabase(Protocol):
# Retrieve an erasure record by its serial number.
    def get_by_serial_number(
        self,
        serial_number: str,
    ) -> ErasureRecord | None:  
        ...

#Search for erasure records based on manufacturer, status, and/or date.
#Limit the number of results to stop the whole database from being returned.
    def search(
        self,
        manufacturer: str | None = None,
        status: str | None = None,
        erasure_date: str | None = None,
        limit: int | int = 20,
    ) -> list[ErasureRecord]:
        ...

#Count the number of erasure records that match the given parameters.
    def count(
        self,
        manufacturer: str | None = None,
        status: str | None = None,
        erasure_date: str | None = None,
    ) -> int:
        ...