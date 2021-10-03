# DSIS ACH Challenge 1

Team: Data Science in Stockholm

Challenge 1 : Interactive station for recording and crowdsourcing a multilingual speech dataset.

Conducted by ZKM (Center for Art and Media, Karlsruhe).

Access the UI here: https://github.com/jimm1034/challange_1_ui/tree/main/lib 

### Run it

Start the language server:
```sh
uvicorn lang_api:app --reload
```

The language API now only supports `/words/[lang]` endpoint.
`lang` is ISO 639-3 language code. Now has only `eng`, `deu` and `jpn`.
```
http://127.0.0.1:8000/words/eng
```
will give something like
```json
{
    "word":"half",
    "lang":"eng",
    "difficulty": 1
}
```

### Background

Existing speech datasets often lack data of less common languages and speakers with protected attributes like dialect or gender. Thus, computer audition algorithms are not capable of or struggle with understanding underrepresented groups.    

### Description

We have focused on encouraging people from diverse backgrounds to participate in the crowdsourcing of the data.

### Technology:
1. Flutter to design our UI, as this is highly scalable 
2. Behind the interface, we have developed a WebSocket in Python.

### Architecture: 
In order for us to be able to deploy the solution onto mobile phones, tablets, and other devices including the Kiosk itself, we imagine that it will work best with a two-tier client-server structure. 
This will allow the client-side to receive input events like face detections, hand gestures, and/or sound pick-ups, while also storing the dataset into a centralized database. The server side will of course also send audio samples from its database to the client-side. 

### Designing UI:
The design behind our UI was guided by different principles from gamification and behavioral design to encourage the visitors to engage with the Kiosk. 

### Encouraging Participation

The following aspects of our design give it an advantage in achieving our goal of increasing participation:
1. Friendly, unbiased mascot
2. Easy to understand text and gameplay interface
3. Integrating the use of simple gestures with confirmation and feedback, to encourage participation from diverse groups.
4. Anonymous crowdsourcing, with the option of entering protected attributes: empowers the user, rather than the collector with the choice of entering their details.
5. Easily scalable technologies: help to promote platform agnostic use
6. Integration of behavioral design principles promotes playability and engagement


### Partner

ZKM - Center for Art and Media
