from GrandPyApp.process import grandPyWork
from GrandPyApp import app


def test_grand_py_work():
    result = {'message': [
        "Et donc tu veux savoir tout sur OpenClassrooms",
        "Coquinou, quand même!",
        "Et bein oui c'est au 7 Cité Paradis, 75010 Paris, France",
        "Pas bête la bête!",
        "En plus ce-ci est cadeau, gratos, rien que pour toi",
        "A propos de ta demande et pour la petitte histoire :" +
        "OpenClassrooms est une école en ligne qui propose à ses membres " +
        "des cours certifiants et des parcours débouchant sur un métier" +
        "d'avenir, réalisés en interne, par des écoles, des universités," +
        "ou encore par des entreprises partenaires comme Microsoft ou IBM." +
        " Jusqu'en 2018, n'importe quel membre du site pouvait être auteur," +
        " via un outil nommé 'Course Lab'. De nombreux cours sont issus" +
        " de la communauté, mais ne sont plus mis en avant. Initialement" +
        " orientée autour de la programmation informatique, la plate-forme " +
        "couvre depuis 2013 des thématiques plus larges tels que le " +
        "marketing, l'entrepreneuriat et les sciences. Créé en 1999 sous" +
        " le nom de Site du Zéro, il se forme essentiellement sur" +
        " la base de contributions de bénévoles proposant des tutoriels" +
        " vulgarisés avec un ton léger portant sur des sujets " +
        "informatiques divers. À la suite du succès et de la fin des" +
        " études des gérants, l'entreprise Simple IT, renommée ensuite" +
        " OpenClassrooms, est fondée dans le but de pérenniser le site." +
        " Celle-ci base son modèle économique sur la délivrance de " +
        "certifications payantes et propose un abonnement" +
        " pour être suivi par un mentor,.",
        "Je te montre?, un dessin ?" +
        " https://maps.google.com/?cid=14940048721031988763",
        "Voilà petit fou! Une autre Question a me soumetre ?"
        ]}
    assert grandPyWork("openclassrooms", app) == result
