import unittest
from botsrc import Bot

class BotTestCase(unittest.TestCase):

    def setUp(self):
        self.Bot = Bot(473559457, ":AAH5NFuZppQP0PrypaussjDoo_d0FpJUDxg")


    def test_bot_connect(self):
        self.assertEqual(self.Bot.getMe(), True, 'cannot connect')


if __name__ == '__main__':
        unittest.main()
