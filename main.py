from lib.space_client import SpaceClient

api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiRVhfQ0FMTFNJR05fMiIsInZlcnNpb24iOiJ2Mi4xLjUiLCJyZXNldF9kYXRlIjoiMjAyNC0wMi0xMSIsImlhdCI6MTcwNzc0ODUxNCwic3ViIjoiYWdlbnQtdG9rZW4ifQ.gza8wfjs8t8KP1LqBKTYBYrhrva5Aiw_hwQq9tro50fwSpZc0_urm8b3CR6ZhSTjkjzYY1qDugkZatWCTYApqGHdzPPU6HqDqKTEEEhHnKyufhbZH_By1ehzz38MkmDg1-rgcUZw1-pxyUVr7U1ZTdTbaUpJoU0EFu6TSYpZ6VRQUuf8mLfrSa2k3ZA6K1_SHRk9yUrBnQZRaZVGXB6o9NWco1L69XnLFm3SBPuayrQ5nTPlj_tRIhXOARbIlGhnYKv1MJOuvHQZcoVwZ59UIHhRPpB7LPcwPUWbDlG5cCo3E2Xq1mlGKdgT_58TkU6b0iR8_AdCv2YjTXTn0KQxQQ"

space_client = SpaceClient(api_token)
ships = space_client.ships.get_ships()

print(ships[0].frame.symbol.value)