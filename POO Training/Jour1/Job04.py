class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
        
    def SePresenter(self):
        return f"{self.prenom} {self.nom}"

Pe1 = Personne(nom="Doe", prenom="John")
Pe2 = Personne(nom="Dupond", prenom="Jean")

print("Je suis", Pe1.SePresenter())
print("Je suis", Pe2.SePresenter())