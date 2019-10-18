import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

user_input = input('Que veux-tu savoir mon enfant?  :  ').split(sep=" ")

stop_words = set(stopwords.words('french'))

new_sentence = []
for word in user_input:
    if word not in stop_words:
        if len(word) > 2:
            if word[-2:] != "er":
                if word[0].isupper():
                    new_sentence.append(word)
print(new_sentence)
