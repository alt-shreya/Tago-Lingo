# Artificially Correct Challenge 1

Team: Data Science in Stockholm

Challenge 1 : Interactive station for recording and crowdsourcing a multilingual speech dataset https://www.goethe.de/prj/one/en/aco/ver/hac/cha.html#i7094282

## Run it

The project consists of different parts:
- Face/gesture dection on Raspberry Pi
- Main interface (now via web), in Flutter - see https://github.com/jimm1034/challange_1_ui/tree/main/lib 
- Language API server

see requirements.txt for required libraries.

Start the language API server:
```sh
uvicorn lang_api:app --reload
```

Endpoints:

- `/words/[lang]`
    
    `lang` is ISO 639-3 language code. Now has only `eng`, `deu` and `jpn`.

    ```
    http://127.0.0.1:8000/words/eng
    ```
    will give something like
    ```json
    {
        "word": "half",
        "lang": "eng",
        "difficulty": 1
    }
    ```

- `/record/[lang]`

  will send a word of that language to WebSocket (record mode)

- `/listen/[lang]`

  will send a word of that language to WebSocket (listen mode)


## Background

Existing speech datasets often lack data of less common languages and speakers with protected attributes like dialect or gender. Thus, computer audition algorithms are not capable of or struggle with understanding underrepresented groups.    

## Description

The aim of this challenge is to develop a digital interface prototype with necessary tools for crowdsourcing a speech dataset that lets the users record and validate spoken words. 
The long-term goal (not part of this challenge) is to embed this prototype into an interactive station and deploy it in the museum and other public spaces around the world so we can collect a highly diverse speech dataset. The dataset we aim for will contain examples of people saying the word for their language in that same language, e.g., "english", "deutsch", "español", "français". The size of the dataset should be small enough to capture a large variety of speakers and languages. The resulting dataset may be used to overcome language barriers by training an AI to identify the desired language, thereby keeping the bias to a minimum. 

## Considerations

Due to the pandemic, it is necessary to implement touchless interfaces for interacting with the station. To validate an audio sample, individuals must listen to a recording and either accept or reject it. The resulting tools and dataset will be released under an open-source license. We hope the interactive station will be deployed in public spaces all over the world. The resulting dataset may be used to overcome language barriers by training an AI to identify the desired language. 

## Partner

ZKM - Center for Art and Media
