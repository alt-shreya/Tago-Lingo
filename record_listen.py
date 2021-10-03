from pathlib import Path
from random import choice
from time import sleep

files = dict()
files["deu"] = "data/deu-basic.txt"
files["eng"] = "data/eng-oxford3000.txt"
files["jpn"] = "data/jpn-jlpt-n5.txt"

words = dict()
words["deu"] = None
words["eng"] = None
words["jpn"] = None

def load_words(path):
    with open(path, "r") as fh:
        lines = fh.read().splitlines()
    lines = [line.strip() for line in lines]
    return lines

def get_word(lang: str, difficulty: int = 1):
    global files
    global words

    word_list = None
    
    if not lang or (lang not in files):
        return("(no dictionary for the selected language)")
    
    if words[lang]:
        word_list = words[lang]
    else:
        word_list = load_words(files[lang])

    if word_list:
        return choice(word_list)

    return("(no word available)")


def stage_record(lang: str):
    print("=== RECORD MODE: START ===")

    quit = False
    retry_count = 1
    word = get_word(lang)
    repeat = False

    while not quit:
        print()
        if repeat:
            print("Please re-read this word:")
        else:
            print("Please read this word:")

        print(f"\n{word}\n")
        sleep(1)
        print(f"<play user's recording of '{word}' for user to check>\n")
        sleep(0.5)

        response = None
        while (not response) or (response not in "CcRrSsQq"):
            print("(C: Confirm)   (R: Record again)   (S: Skip)   (Q: quit)")
            response = input()

        if response in "Qq":  # quit
            quit = True
        if response in "Cc":  # confirm
            # store re-record count and wave file to record table
            print(f"<Store a wavefile for '{word}', with re-record count = {retry_count}>")
            word = get_word(lang)
            retry_count = 1
            repeat = False
        elif response in "Rr":  # record again
            retry_count = retry_count + 1
            repeat = True
        else:  # skip
            # store try count (without wave file) to record table
            print(f"<Store no wavefile for '{word}', with re-record count = {retry_count}>")
            word = get_word(lang)
            retry_count = 1
            repeat = False

    print("=== RECORD MODE: END ===")

            
def stage_listen(lang: str):
    print("=== LISTEN MODE: START ===")

    quit = False
    retry_count = 1
    word = get_word(lang)
    repeat = False

    while not quit:
        print()
        if repeat:
            print("Please re-listen to the recording and see if it match with this word:")
        else:
            print("Please listen to the recording and see if it match with this word:")
        print()
        print(f"<play recording of '{word}'>")
        sleep(1)
        print(f"\n{word}\n")
        sleep(0.5)
        
        response = None
        while (not response) or (response not in "YyNnRrSsQq"):
            print("(Y: Yes)   (N: No)  (R: Repeat again)   (S: Skip)   (Q: quit)")
            response = input()

        if response in "Qq":  # quit
            quit = True
        elif response in "Yn":  # yes
            # store retry count and Accept to validate table
            print(f"<Store Accept for '{word}', with re-listen count = {retry_count}>")
            word = get_word(lang)
            retry_count = 1
            repeat = False
        elif response in "Nn":  # no
            # store retry count and Reject to validate table
            print(f"<Store Reject for '{word}', with re-listen count = {retry_count}>")
            word = get_word(lang)
            retry_count = 1
            repeat = False
        elif response in "Rr":  # repeat
            retry_count = retry_count + 1
            repeat = True
        else:  # skip
            # store retry count and Skip to validate table
            print(f"<Store Skip for '{word}', with re-listen count = {retry_count}>")
            word = get_word(lang)
            retry_count = 1
            repeat = False

    print("=== LISTEN MODE: END ===")
