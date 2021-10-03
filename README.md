# Artificially Correct Challenge 1 - Team 1a

Challenge 1 : Interactive station for recording and crowdsourcing a multilingual speech dataset

Team 1a: Data Science in Stockholm
-  [Concept doc](https://docs.google.com/document/d/1Jz-y8O6klXgqN_5tMxI8Ths5nY8XCw33q4dvrSSQfnQ/edit) | [Technical doc submission](https://docs.google.com/document/d/1QPxCbAu8YQ_8IrJqLWqkBUgI8C8m270VsehPtDh6MdY/edit) | [Top 5 pitch](https://www.canva.com/design/DAErwj0iZPg/VRoPFC9EaXIdMWS8SoqyPQ/view)


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

We have focused on encouraging people from diverse backgrounds to participate in the crowdsourcing of the data.

### Technology

1. Flutter to design our UI, as this is highly scalable 
2. Behind the interface, we have developed a WebSocket in Python.

### Architecture

In order for us to be able to deploy the solution onto mobile phones, tablets, and other devices including the Kiosk itself, we imagine that it will work best with a two-tier client-server structure. 
This will allow the client-side to receive input events like face detections, hand gestures, and/or sound pick-ups, while also storing the dataset into a centralized database. The server side will of course also send audio samples from its database to the client-side. 

### Designing UI

The design behind our UI was guided by different principles from gamification and behavioral design to encourage the visitors to engage with the Kiosk. 

### Encouraging Participation


## Considerations

The following aspects of our design give it an advantage in achieving our goal of increasing participation:

1. Friendly, unbiased mascot
2. Easy to understand text and gameplay interface
3. Integrating the use of simple gestures with confirmation and feedback, to encourage participation from diverse groups.
4. Anonymous crowdsourcing, with the option of entering protected attributes: empowers the user, rather than the collector with the choice of entering their details.
5. Easily scalable technologies: help to promote platform agnostic use
6. Integration of behavioral design principles promotes playability and engagement

## Partner

ZKM - Center for Art and Media
