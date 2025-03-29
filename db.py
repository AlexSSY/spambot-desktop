import os
import aiosqlite
from dotenv import load_dotenv


load_dotenv()


async def setup_db():
    async with aiosqlite.connect(os.getenv("DB_NAME")) as db:
        with open("create_db.sql", "r") as f:
            sql_script = f.read()
        await db.executescript(sql_script)  # Executes the entire SQL file
        await db.commit()


async def save_session(phone_number, session_string):
    async with aiosqlite.connect("sessions.db") as db:
        await db.execute("""
            INSERT OR REPLACE INTO sessions (phone, session_string) VALUES (?, ?)
        """, (phone_number, session_string))
        await db.commit()


async def load_session(phone_number):
    async with aiosqlite.connect("sessions.db") as db:
        async with db.execute("""
            SELECT session_string FROM sessions WHERE phone = ?
        """, (phone_number,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None
        

async def phone_exists(phone):
    async with aiosqlite.connect("your_database.db") as db:
        async with db.execute("SELECT 1 FROM sessions WHERE phone = ?", (phone,)) as cursor:
            return await cursor.fetchone() is not None
