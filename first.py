import requests
from botsrc import Bot

id = 473559457
key = ":AAH5NFuZppQP0PrypaussjDoo_d0FpJUDxg"
b = Bot(id, key)
print(b.getMe())
b.getUpdates()
