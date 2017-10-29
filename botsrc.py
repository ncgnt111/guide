import requests
import asyncio
import time


class Bot:

    def __init__(self, id, key):
        self.id = str(id)+str(key)
        self.link = "https://api.telegram.org/bot"
        self.offset = 0

    def getMe(self):
        response = (requests.get(self.link+self.id+"/getMe").json())
        try:
            return response["ok"]
        except KeyError:
            return "Not ok"

    def sendMessage(self, arg):
        text = arg[0]
        chat_id = arg[1]
        # time.sleep(5)
        data = {'text': arg[0], 'chat_id': arg[1]}
        requests.get(self.link+self.id+"/sendMessage", data)

    def makeResponse(self, result):
        person = result["message"]["from"]["id"]
        text = result["message"]["text"]
        args = ["echo:\n"+text, str(result["message"]["from"]["id"])]
        self.sendMessage(args)

    def getUpdates(self):
        while(True):
            data = {'offset': self.offset}
            answer = requests.get(self.link+self.id+"/getUpdates", data).json()
            result = answer["result"]
            try:
                if result[0]["update_id"] >= self.offset:
                    loop = asyncio.get_event_loop()
                    loop.run_in_executor(None, self.makeResponse, result[0])
                    self.offset = answer["result"][0]["update_id"]+1
            except IndexError:
                continue
