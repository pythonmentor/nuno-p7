import re
import json

print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")


def get_user_choice():
    """
    Get and parse user's sentences.
    """

    while True:
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        user_input = re.split(",|'| |-", user_input)
        user_input = [x.lower() for x in user_input]
    
        with open('stop_words.json') as json_stop_words:
            stop_words_custom = json.load(json_stop_words)
        
        new_sentence = []

        for word in user_input:
            if word not in stop_words_custom:
                if len(word) > 2:
                    if word[-2:] != "er":
                        new_sentence.append(word)

        if len(new_sentence) >= 1:
            print("Mots a envoyer", new_sentence)
            break

        else:
            break


if __name__ == "__main__":
    get_user_choice()
