from .first_input_parser import important_words, parse_user_input
from .interface_requests import call_wiki_page, call_wiki_title


class UserInterface:
    """
    User program interface and body of program
    """
    def __init__(self, parsed_user_input, parsed_sentence):
        self.parsed_user_input = parsed_user_input
        self.parsed_sentence = parsed_sentence

    def user_interface_user_to_bot_with_hello(self):
        print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        self.parsed_user_input = parse_user_input(user_input)
        self.parsed_sentence = important_words(self.parsed_user_input)
        wiki_title = call_wiki_title(self.parsed_sentence)
        wiki_text = call_wiki_page(wiki_title)
        text = "{}{}{}".format(
            self.parsed_user_input[0],
            wiki_title,
            wiki_text)
        print(text)


if __name__ == "__main__":
    UserInterface.user_interface_user_to_bot_with_hello(UserInterface)
