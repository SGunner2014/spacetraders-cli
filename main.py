from clients.space_client import SpaceClient
from commands import ships_command

api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiRVhfQ0FMTFNJR04iLCJ2ZXJzaW9uIjoidjIuMS41IiwicmVzZXRfZGF0ZSI6IjIwMjQtMDItMjUiLCJpYXQiOjE3MDg5MDgwNjUsInN1YiI6ImFnZW50LXRva2VuIn0.guEsxQgWbnnmImUBE-L5yIHXfQBPWyOZt835F8kQVMXWqGDcpumjhSCE0Gnqqw4LYtUJxPQ66iVH4kiuDkjnBo_qJnVn35itpIj-xkxKHWWjSFbvT16Cf3S8eJkZwqS_jyeUjhMICMhsexIIi8Uma5fKyDudMlZh8CJeDsVwikBd39FXQvEQVaEd91ZJj8kP0XbzjYP-ufULy-kH_Jbq_gQayMLGae8xCYdh4D5QPVTg1mxpHDMAa6-TJCgZ7rUNVPog_tRdc1kHQWxspoLG-mWwCEJROPTWUoyRNGeA7KGfdDokJyAj5E_g98JTJv-wiTkf4WoqncSmmDtg1Or3pg"

space_client = SpaceClient(api_token)

commands = []
commands.append(ships_command(space_client))
print(commands[0].name)

while True:
    command = input("> ")
    commandParts = command.split(" ")
    for command in commands:
        if command.name == commandParts[0].lower():
            command.on_invoke(commandParts)
            break