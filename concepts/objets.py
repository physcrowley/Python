# on crée des objets dans python avec le mot-clé "class"
# ce qu'on définit dans le bloc class peut être réutiliser en créant
# des objets de ce type dans nos programmes, comme jimmy et nancy dans
# l'exemple plus bas

class Personne:
    # constructeur > méthode spéciale pour initialiser une instance de l'objet
    def __init__(self):
        self.name = ""      # liste des attributs champs avec leurs 
        self.age = 0        # valeurs initiales par défaut
        self.genre = ""     # Cet objet a donc les champs name, age et genre


    # Une façon rusée de créer des objet en spécifiant les valeurs pour
    # chaque attribut de l'objet au départ, adapté de l'idée présentée
    # sur stackoverflow ici : 
    #   https://stackoverflow.com/a/141777
    @classmethod
    def avec_valeurs(this_class, n, a, g):
        temp = this_class()    # créer une instance temporaire vide en appelant __init__
        temp.name = n          # assigner les valeurs
        temp.age = a
        temp.genre = g
        return temp            # retourner l'objet avec les valeurs spécifiées


    # méthodes > les comportements possibles avec l'objet
    def parler(self):
        print("Allô! Je m'appelle", self.name)
    
    def grandir(self):
        self.age += 1


# notre script pour tester le code plus haut
if __name__ == "__main__":
    jimmy = Personne()
    jimmy.parler()
    jimmy.name = "Jimmy"
    jimmy.parler()

    nancy = Personne.avec_valeurs("Nancy", 17, "Femelle")
    nancy.parler()
