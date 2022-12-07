class Player:
    age = 31
    pokemaos = []
    def __init__(self,name,pokemaos):
        self.name = name
        self.pokemaos.append(pokemaos)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insertPokemao(self, pokemao):
        if(len(self.pokemaos) > 2):
            print("Você já possui o limite máximo de 3 Pokemaos, se desfaça de um pokemon para adquirir outro")
            return
        self.pokemaos.append(pokemao)