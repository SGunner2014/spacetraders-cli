from typing import List

from clients.space_client import SpaceClient

class BaseCommand:
    name: str

    def __init__(self, space_client: SpaceClient):
        self.space_client = space_client

    def get_command_handlers(self) -> dict:
        pass

    def on_invoke(self, parts: List[str]) -> None:
        pass