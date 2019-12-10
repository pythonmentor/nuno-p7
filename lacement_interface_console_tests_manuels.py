from GrandPyApp.first_input_parser import important_words, parse_user_input
from GrandPyApp.interface_requests import (
    call_google_maps_positionnement,
    call_google_maps_details,
    call_wiki_by_geocoordinates,
    call_wiki_main_page,
    call_wiki_found_page
)
from GrandPyApp.views import app


class UserInterface:
    """
    User program interface and body of program
    """
    key = app.config("MAPS_API_KEY")
    print(key)

    call_by_name = call_google_maps_positionnement(key, "openclassrooms")
    call_google_maps_details(key, call_by_name[0])
    call_wiki_main_page("openclassrooms")
    call_wiki_found_page("openclassrooms")

    def __init__(self, parsed_user_input, parsed_sentence):
        self.parsed_user_input = parsed_user_input
        self.parsed_sentence = parsed_sentence

    def user_interface_user_to_bot_with_hello(self):
        print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        self.parsed_user_input = parse_user_input(user_input)
        self.parsed_sentence = important_words(self.parsed_user_input)
        google_coordinates = call_google_maps_positionnement(
            self.parsed_sentence
            )
        call_wiki_by_geocoordinates(google_coordinates[1])


if __name__ == "__main__":
    UserInterface.user_interface_user_to_bot_with_hello(UserInterface)
