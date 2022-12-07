class Player:
    age = 31 
    def __init__(self,name,pokemaos):
        self.name = name
        self.pokemaos = pokemaos

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)