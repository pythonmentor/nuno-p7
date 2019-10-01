import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
print("Salut, je suis GrandPy, je suyis là afion de t'aider ;-)")

user_input = input('Que veux-tu savoir mon enfant?')

stop_words = set(stopwords.words('french'))
words = word_tokenize(user_input, language = 'french')

new_sentence = []
 
for word in words:
    if word not in stop_words:
        new_sentence.append(word)
 
print(new_sentence)

