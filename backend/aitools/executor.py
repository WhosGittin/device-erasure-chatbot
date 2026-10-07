from backend.aitools.implementations import *


TOOL_HANDLERS = {
    "get_erasure_by_serial_number": get_erasure_by_serial_number,

    "search_erasures": search_erasures,

    "count_erasures": count_erasures,
}

def execute_tool(
    name: str,
    arguments: dict,
    database: Database,
) -> dict:

    handler = TOOL_HANDLERS.get(name)

    if handler is None:
        raise ValueError(f"No handler found for tool: {name}")

    return handler(database, **arguments)