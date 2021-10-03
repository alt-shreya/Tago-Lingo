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

The aim of this challenge is to develop a digital interface prototype with necessary tools for crowdsourcing a speech dataset that lets the users record and validate spoken words. 
The long-term goal (not part of this challenge) is to embed this prototype into an interactive station and deploy it in the museum and other public spaces around the world so we can collect a highly diverse speech dataset. The dataset we aim for will contain examples of people saying the word for their language in that same language, e.g., "english", "deutsch", "español", "français". The size of the dataset should be small enough to capture a large variety of speakers and languages. The resulting dataset may be used to overcome language barriers by training an AI to identify the desired language, thereby keeping the bias to a minimum. 

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
