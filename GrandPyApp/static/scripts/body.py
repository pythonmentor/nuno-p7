from .first_input_parser import parse_user_input


class UserInterface:
    """
    User program interface and body of program
    """

    print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

    def user_first_question():
        while True:
            user_input = input('Que veux-tu savoir mon enfant?  :  ')
            parsed_user_input = parse_user_input(user_input)

            if len(parsed_user_input) >= 1:
                print("Mots a envoyer", parsed_user_input)
                break
            else:
                continue
        return parsed_user_input
        

if __name__ == "__main__":
    pass
