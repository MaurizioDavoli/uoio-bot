from telethon import TelegramClient, events
import logging
from utility import generate_reply, check_message
import os


API_ID_TDLIB = os.getenv('API_ID_TDLIB')
API_HASH_TDLIB = os.getenv('API_HASH_TDLIB')
BOT_TOKEN = os.getenv("BOT_TOKEN")

UOIO_ID = 684773287
CHAT_ID = -380555853
MY_ID = 109665285

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient('botSession', API_ID_TDLIB, API_HASH_TDLIB)


async def send_message(chat, msg):
    await client.send_message(chat, msg)


client.start()


@client.on(events.NewMessage(chats=-380555853))
async def handler(event):
    if event.message.from_id.user_id == UOIO_ID and check_message(event.message.message):
        await event.reply(generate_reply())


@client.on(events.NewMessage(chats=109665285))
async def handler2(event):
    msg = event.message.message
    await client.send_message(CHAT_ID, msg)


client.run_until_disconnected()
