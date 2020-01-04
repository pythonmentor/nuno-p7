from GrandPyApp.process import grandPyWork
from GrandPyApp.views import app


def test_grand_py_work():
    result = {'message': [
        "Et donc tu veux savoir tout sur OpenClassrooms",
        "Coquinou, quand même!\n",
        "Et bein oui c'est au 7 Cité Paradis, 75010 Paris, France",
        "Pas bête la bête!\n",
        "En plus ce-ci est cadeau, gratos, rien que pour toi",
        "A propos de ta demande et pour la petitte histoire quand même:" +
        " OpenClassrooms est une école en ligne qui propose à ses membres " +
        "des cours certifiants " +
        "et des parcours débouchant sur un métier d\'avenir, réalisés" +
        " en interne, par des écoles," +
        " des universités, ou encore par des entreprises partenaires" +
        " comme Microsoft ou IBM. Jusqu\'en" +
        " 2018, n\'importe quel membre du site pouvait être auteur," +
        "via un outil nommé 'Course Lab'." +
        " De nombreux cours sont issus de la communauté, mais ne sont plus" +
        " mis en avant.",
        "Je te montre?, un dessin ?" +
        " https://maps.google.com/?cid=14940048721031988763",
        "Voilà petit fou! Une autre Question a me soumetre ?"
        ]}
    assert grandPyWork("openclassrooms", app) == result
