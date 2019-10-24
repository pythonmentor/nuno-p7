import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")


def get_user_choice():
    """
    Get and parse user's sentences.
    """
    while True:
        
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        user_input = re.split(",|'| |-", user_input)
        stop_words = set(stopwords.words('french'))
        stop_words_capitalize = [x.capitalize() for x in stop_words]

        new_stop_words = list(stop_words) 
        words_to_eliminate = new_stop_words + stop_words_capitalize

        new_sentence = []
        for word in user_input:
            if word not in words_to_eliminate:
                if len(word) > 2:
                    if word[-2:] != "er":
                        if word[0].isupper():
                            new_sentence.append(word)
        print(new_sentence)

        if len(new_sentence) == 0:

            print("Tu sais, avec mon age, " +
                "je ne t'ai pas trés bien compris mon enfant, " +
                "peut-tu me rappeller en utilisant une majuscule, " +
                "afin que je puisse mieux comprendre!  ")
            continue

        if len(new_sentence) >= 1:
            print("Mots a envoyer", new_sentence)
            break

        else:
            break

        
if __name__ == "__main__":
    get_user_choice()
