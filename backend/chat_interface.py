from typing import Protocol

class ModelRespone(Protocol):
    ...

class ChatModel(Protocol):

    def generate(self, messages: list[dict]) -> dict:
        ...