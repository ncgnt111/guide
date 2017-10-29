import requests
from botsrc import Bot
id = 423596530
key = ":AAGb8vMov2FA0PQKZKdC9Qq56YxV7v-FupY"
b = Bot(id, key)
print(b.getMe())
b.getUpdates()
