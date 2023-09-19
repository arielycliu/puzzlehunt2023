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


def answer_puzzle(question, partial, answer):
    print(question)
    solved = False
    while not solved:
        response = input("> ")
        response = hash_text(response)
        if response == answer:
            print("Correct, you got the final answer!")
            solved = True
        elif response == partial:
            print("Correct, that's a partial answer - keep going")
        else:
            print("Incorrect, try again?")


def print_text(statement, wait=True):
    try:
        print(eval(statement))
        print("sdf")
    except:
        print(statement)
    if wait:
        input("")


def ask_question(question, options):
    global incorrect_dialogue
    print(question)
    if options != "N/A":
        for i in range(len(options)):
            print(f"   {i + 1}. {options[i]}")
    invalid = True
    while invalid:
        response = input("> ")
        response = response.lower()
        if options == "N/A" and response != "":
            invalid = False
        elif response in options:
            invalid = False
        else:
            print(random.choice(incorrect_dialogue))
    return response


def tutorial():
    print_text("Press enter to advance in the story, let try it now...")
    ask_question("A '> ' tells you have you need to respond to a question to continue, let's practice it too...",
          ["yes", "no", "maybe"])
    print("Good job, I think you're ready.")
    return

