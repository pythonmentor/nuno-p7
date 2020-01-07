import random


def picAfunny():
    blagues = [
        {"messages": [
            "Pourquoi les Belges viennent-ils à la messe avec du savon ?",
            "Pour l'Ave Maria!"
        ]},
        {"messages": [
            "Comment appelle t'on les parents de l'homme invisible?",
            "Les transparents "
        ]},
        {"messages": [
            "Pourquoi Napoléon n' a jamais déménagé?",
            "Parce qu'il avait un Bonaparte"
        ]},
        {"messages": [
            "2 vaches discutent ..." +
            "Ça te fait pas peur toi ces histoires de 'vache folle' ?",
            "Ben j'm'en fous j'suis un lapin"
        ]},
        {"messages": [
            "Pendant l'acte... Dit moi des chose sale !",
            "La cuisine, la salle de bain......"
        ]},
        {"messages": [
            "Comment appelle-t-on le fait de se retrouver " +
            "coincé entre une Marine et un Jean-Marie ?",
            "Une double Pen."
        ]},
        {"messages": [
            "Le viagra c'est comme l'enfer! ",
            "Satan l'habite. "
        ]},
        {"messages": [
            "À Paris quand il pleut je suis comme un Tampax",
            "Je suis dans le plus bel endroit du monde mais à la mauvaise période."
        ]},
        {"messages": [
            "Quel super héros donne le plus vite l'heure ?",
            "Speed heure man !"
        ]},
        {"messages": [
            "Pourquoi le corps de Ben Laden ne rouille pas dans l'eau ?",
            "Parce qu'il est antioxydant (anti-occident)"
        ]},
        {"messages": [
            "Tu connais la blague de la chaise?",
            "Elle est pliante!"
        ]},
        {"messages": [
            "C'est l'histoire d'un poil avant il etait bien,",
            "maintenant il est pubien!"
        ]},
        {"messages": [
            "Tu savais que la 'ouate' vient des phoques ? ",
            "Ouate de Phoques ! "
        ]},
        {"messages": [
            "Pourquoi il n'y a pas de ballon à question pour un champion ?",
            "Car Julien Lepers"
        ]},
        {"messages": [
            "Tu connais schling-schling la girafe?",
            "C'est une girafe qui passe trop près" +
            " d un helico et schling-schling la girafe. "
        ]},
        ]

    return random.choice(blagues)
