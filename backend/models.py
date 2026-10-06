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

    @classmethod
    def convert_data(cls, data: dict) -> "ErasureRecord":
        return cls(
            serial_number=data["serial_number"],
            manufacturer=data["manufacturer"],
            model=data["model"],
            erasure_date=data["erasure_date"],
            method=data["method"],
            status=data["status"],
            failure_reason=data.get("failure_reason"),
        )