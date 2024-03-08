from typing import List

from clients.space_client import SpaceClient

class BaseCommand:
    name: str

    def __init__(self, space_client: SpaceClient):
        self.space_client = space_client

    def __invoke__(self, parts: List[str]) -> None:
        command_handlers = self.get_command_handlers()
        if parts[1].lower() in command_handlers:
            command_handlers[parts[1]](parts)

    def get_command_handlers(self) -> dict:
        return []