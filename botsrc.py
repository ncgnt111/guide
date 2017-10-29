import requests
import asyncio
import time


class Bot:

    def __init__(self, id, key):
        self.id = str(id)+str(key)
        self.link = "https://api.telegram.org/bot"
        self.offset = 0
        self.prev_res = None
        self.is_awake = False

    def logger(func):
        def write(*args, **kwargs):
            result = func(*args, **kwargs)
            if ("{'result': [], 'ok': True}" != str(result) and
               "{'ok': True, 'result': []}" != str(result)):
                with open("log.txt", "a") as f:
                    f.write(str(result)+'\n\n')
            return result
        return write

    @logger
    def get(self, method, data=None, type_answ='json'):
        "make get to self.link and returns status from serv"
        reply = requests.get(self.link+self.id+"/"+method, data)
        try:
            if reply.json()["ok"] is True:
                self.is_awake = True
            else:
                self.is_awake = False
        except KeyError:
            self.is_awake = False
            time.sleep(10)
            self.get(method, data, type_answ)
        if type_answ == 'json':
            return reply.json()
        elif type_answ == 'text':
            return reply.text
        else:
            return reply

    def getMe(self):
        response = self.get(method="getMe")
        return response["ok"]

    def showMenu(self, id, menu=None):
        "still dont work"
        if menu is None:
            reply_markup = {'keyboard': [["1", "2", "3"]]}
            data = {'text': "1", 'chat_id': id, 'reply_markup': reply_markup}
            print(requests.get(self.link+self.id+"/sendMessage", data).text)

    def sendMessage(self, arg):
        text = arg[0]
        chat_id = arg[1]
        # time.sleep(5)
        data = {'text': arg[0], 'chat_id': arg[1]}
        self.get(method="sendMessage", data=data)
        # self.showMenu(chat_id)

    def makeResponse(self, result):
        person = result["message"]["from"]["id"]
        text = result["message"]["text"]
        # text = proceed(person, text)
        args = ["echo:\n"+text, str(result["message"]["from"]["id"])]
        self.sendMessage(args)

    def getUpdates(self):
        while(True):
            data = {'offset': self.offset}
            answer = self.get(method="getUpdates", data=data, type_answ="json")
            result = answer["result"]
            try:
                if result[0]["update_id"] >= self.offset:
                    loop = asyncio.get_event_loop()
                    loop.run_in_executor(None, self.makeResponse, result[0])
                    self.offset = answer["result"][0]["update_id"]+1
            except IndexError:
                continue
