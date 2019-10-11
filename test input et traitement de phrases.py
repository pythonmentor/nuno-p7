import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

user_input = input('Que veux-tu savoir mon enfant?  :')

stop_words = set(stopwords.words('french'))
words = word_tokenize(user_input, language='french')

new_sentence = []
for word in words:
    if word not in stop_words:
        if len(word) > 2:
            new_sentence.append(word)
print(new_sentence)
position_words = ["lieu", "adresse", "trouve", "situe"]