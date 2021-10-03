from fastapi import FastAPI
from record_listen import get_word

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
