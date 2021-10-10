import time
import os
import re

from telegram.client import Telegram

# this the id of the bot that returns ids of bots and channels.
# This constant was acquired by sending message to this bot in official telegram client
USERNAME_TO_ID_CHAT_ID = 850434834

class TGError(BaseException):
    pass


#
# pure functions that don't need to communicate with Telegram API
# are written outside of the TGAPI class:
#

def get_chat_id_from_username_bot_messages(handle, response):
    def extract_chat_id(message):
        # TODO: make sure that it won't throw an error
        # if bot suddently sends us different type of message
        # that doesn't have these fields
        text = message['content']['text']['text']
        if not f'\n@{handle}\n' in text:
            return None

        match = re.search('\nid: (-?\d+)\n', text)
        if not match:
            return None
        return int(match[1])

    def is_present(x):
        return not (not x)

    ids = list(filter(is_present, map(extract_chat_id, response['messages'])))
    if len(ids) == 0:
        return None
    return ids[0]



# This class provides methods that work in terms
# of business logic of our app. It wraps Telegram API client
# and provides more complicated scenarios to work with API
class TGAPI:
    def __init__(self):
        self.tg = Telegram(
            api_id=os.environ.get('TELEGRAM_APP_ID'),
            api_hash=os.environ.get('TELEGRAM_API_HASH'),
            phone=os.environ.get('TELEGRAM_PHONE'),  # you can pass 'bot_token' instead
            database_encryption_key=os.environ.get('TELEGRAM_DATA_CRYPT_KEY'),
        )
    
    def login(self):
        self.tg.login()

    # in order to get a chat_id, we send message to @username_to_id_bot
    # and read the response.
    # TODO: find a way to get chat_id without using external bots
    def get_chat_id_for_handle(self, handle):
        r = self.tg.send_message(USERNAME_TO_ID_CHAT_ID, f'@{handle}')
        r.wait()
        if r.error:
            # if telegram servers are unreachable, request may fail with error
            # just throw it, expect caller function to handle it
            raise TGError(r.error_info)
        # now we need to wait for response from the @username_to_id_bot
        # for now let's just sleep and hope that it would respond in 1 second
        # in future this should be extracted into a separate thread or even process
        #
        # The best solution would be to use message queue, send requests for chat_id
        # and get responses. This way many concurrent requests for chat_id wouldn't interfere
        # with each other. Requests for chat-id could possiblity handled in bulk, with
        # respect to quotas that Telegram may impose on such requests.
        time.sleep(1)
        # now we are trying to get the response from the bot
        # it must be in chat history
        r = self.tg.get_chat_history(USERNAME_TO_ID_CHAT_ID, limit=5)
        r.wait()
        if r.error:
            raise TGError(r.error_info)

        return get_chat_id_from_username_bot_messages(handle, r.update)
