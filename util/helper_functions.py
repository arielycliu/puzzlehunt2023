import random
import hashlib
import json

incorrect_dialogue = [
    "God, read the instructions.",
    "Learn some spelling",
    "That's not an option...",
    "Why do I put up with this",
    "What are you doing?",
    "No"
]


def hash_text(text_to_hash):
    text_to_hash = text_to_hash.lower()
    try:
        text_to_hash = float(text_to_hash)
        text_to_hash = int(text_to_hash)
        text_to_hash = str(text_to_hash)
    except:
        text_to_hash = text_to_hash.replace(" ", "")

    # Create SHA-256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the bytes of the input text
    sha256.update(text_to_hash.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hashed_text = sha256.hexdigest()
    return hashed_text


def get_dialogue_json(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


def answer_puzzle(blurb):
    print("")
    print("=" * 170)
    question = blurb["message"]
    partials = blurb["partials"]
    answer = blurb["answer"]
    print(question)
    solved = False
    while not solved:
        response = input(">>> ")
        response = hash_text(response)
        if response == answer:
            if "answer_response" in blurb.keys():
                print(blurb["answer_response"])
            else:
                print("Correct!")
            solved = True
        elif response in partials.keys():
            if partials[response]:
                print(partials[response])
            else:
                print("Correct, that's a partial answer - keep going!")
        else:
            print("Incorrect, try again?")
    return


def print_text(blurb):
    message = blurb["message"] if blurb["speaker"] == "narrator" else blurb["speaker"] + ": " + blurb["message"]
    print(message)
    if "wait" not in blurb.keys() or blurb["wait"] != "False":
        input(" ~ ")


def friend_print_text(blurb, friend_name):
    message = friend_name + ": " + blurb["message"]
    print(message)
    print("")


def ask_question(blurb):
    question = blurb["message"]
    options = blurb["options"]
    global incorrect_dialogue
    print(question)
    if options != "":
        for i in range(len(options)):
            print(f"   {i + 1}. {options[i]}")
    invalid = True
    while invalid:
        response = input("> ")
        if options == "" and response != "":  # name question, no lowercase
            invalid = False
        elif options == "" and response == "":
            print("Blank answers are not allowed here!")
        else:
            response = response.lower()
            if response in options:
                invalid = False
            else:
                print(random.choice(incorrect_dialogue))
    return response


def tutorial():
    data = get_dialogue_json("../dialogue/tutorial_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            print_text(blurb)
        elif blurb["type"] == "question":
            ask_question(blurb)
        elif blurb["type"] == "puzzle":
            answer_puzzle(blurb)
    return

