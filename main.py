from pydantic import BaseModel
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, send_from_directory, jsonify, Response
from flask_cors import CORS
from flask_pydantic import validate

import db


app = Flask(__name__, static_folder="./web/dist")
CORS(app)


def response(message: str, *, code: int = 0, meta: dict = {}) -> Response:
    return jsonify({
        "code": code,
        "message": message,
        "meta": meta
    })


@app.route('/')
async def serve_vue():
    await db.setup_db()
    return send_from_directory(app.static_folder, 'index.html')


class AddFormData(BaseModel):
    phone: str


@app.route("/api/accounts/add/", methods=["POST"])
@validate()
def accounts_add(body: AddFormData):
    print("Received data:", body.model_dump())
    return response("Form submitted successfully!")


@app.route("/api/accounts")
def accounts():
    return jsonify({
        "count": 0,
        "data": []
    })


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
