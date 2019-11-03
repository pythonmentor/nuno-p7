import re
import json


def parse_user_input(user_input):
    """
    Get and parse user's sentences.
    """

    user_input = re.split(",|'| |-", user_input)
    user_input = [x.lower() for x in user_input]
    with open("../../stop_words.json") as json_stop_words:
        stop_words_custom = json.load(json_stop_words)
    
    new_sentence = []

    for word in user_input:
        if word not in stop_words_custom:
            if len(word) > 2:
                if word[-2:] != "er":
                    new_sentence.append(word)
    return new_sentence


if __name__ == "__main__":

    print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

    while True:
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        parsed_user_input = parse_user_input(user_input)

        if len(parsed_user_input) >= 1:
            print("Mots a envoyer", parsed_user_input)
            break
        else:
            continue
