class Ville:
    def __init__(self, nom_ville, nombre):
        self.__nom_ville = nom_ville
        self.__nombre = nombre

    def get_nom_ville(self):
        return self.__nom_ville
    
    def set_nom_ville(self, nom_ville):
        self.__nom_ville = nom_ville

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def implementer_population(self, ):


class Personne:
    def __init__(self, nom_personne, age, objet_ville):
        self.__nom_personne = nom_personne
        self.__age = age
        self.__objet_ville = objet_ville

    def get_nom_personne(self):
        return self.__nom_personne
    
    def set_nom_personne(self, nom_personne):
        self.__nom_personne = nom_personne

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_objet_ville(self):
        return self.__objet_ville
    
    def set_objet_ville(self, objet_ville):
        self.__objet_ville = objet_ville

    def ajouterPopulation(self):









Vi2 = Ville("Paris", 1000000)
Vi3 = Ville("Marseille", 861635)

Pe1 = Personne("John", "45 ans", "Habitant à Paris.")
Pe2 = Personne("Myrtille", "4 ans", "Habitant à Paris.")
Pe3 = Personne("Chloé", "18 ans", "Habitant à Marseille.")