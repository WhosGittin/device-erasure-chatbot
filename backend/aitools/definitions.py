TOOL_DEFINITIONS = [
    {
        "toolSpec": {
            "name": "get_erasure_by_serial_number",
            "description": "Retrieve a single erasure record by its serial number.",

            "inputSchema": {
                "type": "object",
                "properties": {
                    "serial_number": {
                        "type": "string",
                        "description": "The serial number of the device"
                    }
                },
                "required": ["serial_number"]
            }
        }
    },
    {
        "toolSpec": {
            "name": "search_erasures",
            "description": "Search for erasure records based on manufacturer, status, and/or date.",

            "inputSchema": {
                "type": "object",
                "properties": {
                    "manufacturer": {
                        "type": "string",
                        "description": "The manufacturer of the device"
                    },
                    "status": {
                        "type": "string",
                        "description": "The status of the erasure record"
                    },
                    "erasure_date": {
                        "type": "string",
                        "format": "date",
                        "description": "The date the device was erased"
                    }
                }
            }
        }
    },
    {
        "toolSpec": {
            "name": "count_erasures",
            "description": "Count the number of erasure records that match the given parameters.",

            "inputSchema": {
                "type": "object",
                "properties": {
                    "manufacturer": {
                        "type": "string",
                        "description": "The manufacturer of the device"
                    },
                    "status": {
                        "type": "string",
                        "description": "The status of the erasure record"
                    },
                    "erasure_date": {
                        "type": "string",
                        "format": "date",
                        "description": "The date the device was erased"
                    }
                }
            }
        }
    }
]