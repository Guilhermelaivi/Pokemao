class Player:
    age = 31 
    pokemaos = []
    def __init__(self,name,pokemaos):
        self.name = name
        self.pokemaos.append(pokemaos) 

    def insertPokemao(self,pokemao):
        print(len(self.pokemaos))
        if len(self.pokemaos) == 3:  
            print("Você alcançou o limite máximo de 3 Pokemãos!") 
            return
        self.pokemaos.append(pokemao)


       