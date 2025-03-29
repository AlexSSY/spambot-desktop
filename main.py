import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, send_from_directory

import db


app = Flask(__name__, static_folder="./web/dist")

@app.route('/')
async def serve_vue():
    await db.setup_db()
    return send_from_directory(app.static_folder, 'index.html')

async def add_phone(phone):
    # check if phone exists in db
    if await db.phone_exists(phone):
        pass

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
