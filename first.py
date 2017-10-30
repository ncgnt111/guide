import requests
from botsrc import Bot

id = # put your bot id here( only first numbers from token)
key = # put here a key. Rest of token
b = Bot(id, key)
print(b.getMe())
b.getUpdates()
