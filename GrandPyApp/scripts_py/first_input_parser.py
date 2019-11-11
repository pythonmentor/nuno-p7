import re
from ..views import app

app.config.from_object('config')


def parse_user_input(user_input):
    """
    Get and parse user's sentences.
    """
    user_input = re.split(",|'| |-", user_input)
    user_input = [x.lower() for x in user_input]

    stop_words_custom = app.config['STOP_WORDS']
    new_sentence = []

    for word in user_input:
        if word not in stop_words_custom:
            if len(word) > 2:
                if word[-2:] != "er":
                    new_sentence.append(word)
    return new_sentence


def important_words(parsed_sentence):
    """
    Get a positionement word
    """
    position_words = ["adresse", "situé", "situe", "trouve"]
    new_sentence = []
    for word in parsed_sentence:
        if word in position_words:
            index = position_words.index(word)
            i = index
            while i < len(parsed_sentence):
                new_sentence.append(parsed_sentence[i])
                i += 1
    if len(new_sentence) == 1:
        title = new_sentence[0]
    else:
        title = ' '.join(new_sentence[0:2])
    print(title)
    return title


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
