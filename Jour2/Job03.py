class Livre:
    def __init__(self, titre, auteur, pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Votre nombre de pages doit être un nombre positif")

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible
        disponible = True

    def vérification(self):

    
    def emprunter(self):

Lv = Livre("Crime and Punishment", "Fyodor Dostoevsky", 527)

print(" ") # juste pour pouvoir lire plus clairement sur Terminal
print(Lv.get_titre())
print(Lv.get_auteur())
print(Lv.get_pages())

Lv.set_titre("The Ingenious Gentleman Don Quixote of La Mancha")
Lv.set_auteur("Miguel de Cervantes")
Lv.set_pages(940)

print(" ")
print(Lv.get_titre())
print(Lv.get_auteur())
print(Lv.get_pages())
print(" ")

