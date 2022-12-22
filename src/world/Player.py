import os

class Player:
    age = 31 
    pokemaos = []
    def __init__(self,name,pokemaos):
        self.name = name
        self.pokemaos.append(pokemaos) 

    def presentPokemaos(self):
        os.system("cls||clear")
        print("--- Pokemão List ---")
        for pokemao in self.pokemaos:
            print(pokemao)
        input("Backspace to return") 
        

    def pokedex(self,optionUser):
        while optionUser != 4:
            match optionUser:
                case "1":
                    self.presentPokemaos()
                case "2":
                    print("it's time to duel")
                case "3":
                    print("it's time to capture pokemaos")
                case _:
                    os.system("cls||clear")
                    print("End game!")
                    break    
        

    def insertPokemao(self,pokemao):
        print(len(self.pokemaos))
        if len(self.pokemaos) == 3:  
            print("Você alcançou o limite máximo de 3 Pokemãos!") 
            return
        self.pokemaos.append(pokemao)


       