"""def place_for_ggapp(self):
    '''in order to give a correct entry for google "word+word"'''
    pl_list = self.user_entry.split()
    self.user_entry = "+".join(pl_list)


def geocoding(self):
    """"""get geographical coordinates: latitude""""""

    geocode_result = gmaps.geocode(self.user_entry)

    try:
        self.lat = geocode_result[0]["geometry"]["location"]["lat"]
        self.lng = geocode_result[0]["geometry"]["location"]["lng"]
        self.address = geocode_result[0]["formatted_address"]
    except IndexError:
    #to skip indexerror when a place is not find we put temporaly the coords of a nice place in France
        self.lat = 0
        self.lng = 0
        self.address ="No address found"


def format_add(self):
    """"""get the place adress""""""
    if self.address == "No address found":
        self.address = "Désolé je ne trouve pas d'adresse"
    else:
        answer_beginning = random.choice(ANSWERSADD)
        self.address = "{}{}".format(answer_beginning,self.address)"""

"""#wiki"""
"""def some_words_about(place):
    """"""Extract and treat wikipedia contents""""""
    page_title = call_wiki_main_page(place)
    article = call_wiki_found_page(page_title)

    try:
        a = article["query"]["pages"]
        # to skip pg id number witch differs from page to page
        for value in a.values():
            extract = value["extract"]
            # format GPY answer
            b = random.choice(ANSWERSSTORY)
            text = "{}{}".format(b, extract)

            #add a mock answer when the page is not found
            for k,v in a.items():
                if k == "85296": #the page id of "2CV"
                    text = "{}\n{}".format(ANSWERWHERENOIDEA[0], extract)

    except IndexError:
        text = "Verifie ton orthographe pour avoir une histoire ! En attendant je parle dans ma barbe !!!"

    return text"""
    