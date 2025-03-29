import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

import db


async def main():
    await db.setup_db()
    print("hello world!")


async def add_phone(phone):
    # check if phone exists in db
    if await db.phone_exists(phone):
        pass


asyncio.run(main())
