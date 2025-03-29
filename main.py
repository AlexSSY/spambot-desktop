import asyncio
import aiosqlite
from telethon import TelegramClient


async def setup_db():
    async with aiosqlite.connect("sessions.db") as db:
        with open("create_db.sql", "r") as f:
            sql_script = f.read()
        await db.executescript(sql_script)  # Executes the entire SQL file
        await db.commit()


async def main():
    await setup_db()
    print("hello world!")


async def add_phone(phone):
    # check if phone exists in db
    async with aiosqlite.connect()


asyncio.run(main())
