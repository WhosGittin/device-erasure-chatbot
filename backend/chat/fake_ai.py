from backend.chat_interface import ChatModel

#A fake AI model implementation for testing purposes and local development
class FakeAIModel:

    def generate(self, messages: list[dict]) -> dict:
        last_message = messages[-1]

        if last_message.get("role") == "user":
            content = last_message.get("content", "")

            if "SN-TEST-0001" in content:
                return {
                    "type": "tool_call",
                    "name": "get_erasure_by_serial_number",
                    "arguments": {"serial_number": "SN-TEST-0001"},
                }

            return {
                "type": "text",
                "text": (
                    "Please provide a device serial number"
                ),
            }

        return {
            "type": "text",
            "text": "Here are the details for the given serial number"
        }
        