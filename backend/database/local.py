class LocalErasureDatabase:

    def __init__(self, records):
        self.records = records

# Retrieve an erasure record by its serial number.
    def get_by_serial_number(self, serial_number):
        for record in self.records:
            if record.serial_number == serial_number:
                return record

#Search for erasure records based on manufacturer, status, and/or date.
    def search(self, manufacturer, status, erasure_date):
        results = []
        for record in self.records:
            if manufacturer and (record.manufacturer != manufacturer):
                continue
            if status and (record.status != status):
                continue
            if erasure_date and (record.erasure_date.strftime("%d-%m-%Y") != erasure_date):
                continue
            results.append(record)
        return results

#Count the number of erasure records that match the given parameters.
    def count(self, manufacturer, status, erasure_date):
        count = 0
        for record in self.records:
            if manufacturer and (record.manufacturer != manufacturer):
                continue
            if status and (record.status != status):
                continue
            if erasure_date and (record.erasure_date.strftime("%d-%m-%Y") != erasure_date):
                continue
            count += 1
        return count