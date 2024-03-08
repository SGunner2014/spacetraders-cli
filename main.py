import os
from dotenv import load_dotenv

load_dotenv()

from clients.space_client import SpaceClient
from commands import ships_command, contracts_command

api_token = os.getenv("API_TOKEN")

space_client = SpaceClient(api_token)

commands = []
commands.append(ships_command(space_client))
commands.append(contracts_command(space_client))

def get_name(command):
    return command.name

commands_str = ", ".join(map(get_name, commands))
print(commands_str)

while True:
    command = input("> ")
    commandParts = command.split(" ")
    for command in commands:
        if command.name == commandParts[0].lower():
            command.__invoke__(commandParts)
            break
