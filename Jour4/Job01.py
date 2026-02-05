class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        self.age += 1

class Eleve(Personne):
    def __init__(self, age):
        super().__init__(age)
    
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self, age):
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matiere, age):
        self.__matiere = matiere
        super().__init__(age)

    def enseigner(self):
        print("Le cours va commencer")

Pe = Personne(14)
El = Eleve(14)

El.afficherAge(age=Eleve)