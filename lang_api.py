from fastapi import FastAPI
import logging

from record_listen import get_word
from websocket import server

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Language API is alive"}


@app.get("/words/{lang}")
async def pick_word(lang):
    word = get_word(lang)

    if word:
        return {
            "word": word,
            "lang": lang,
            "difficulty": 1,
        }
    return {"word": ""}


@app.get("/record/{lang}")
async def record(lang):
    word = get_word(lang)
    server.send_to_clients(f"record: {word}")  # send to websocket for RPI
    logging.info(f"Pick '{word}' for record.")
    if word:
        return {
            "word": word,
            "lang": lang,
            "difficulty": 1,
        }
    return {"word": ""}


@app.get("/listen/{lang}")
async def listen(lang):
    word = get_word(lang)
    server.send_to_clients(f"listen: {word}")  # send to websocket for RPI
    logging.info(f"Pick '{word}' for listen.")
    if word:
        return {
            "word": word,
            "lang": lang,
            "difficulty": 1,
        }
    return {"word": ""}
