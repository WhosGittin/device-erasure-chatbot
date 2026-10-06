from dataclasses import dataclass
from datetime import datetime

#Define a dataclass to represent an erasure record
@dataclass
class ErasureRecord:
    serial_number: str
    manufacturer: str
    model: str
    erasure_date: datetime
    method: str
    status: str
    failure_reason: str | None