import os


class TextColors:
    ENDC = '\033[0m'

def clearTerminal():
    input("Aperte Enter para continuar")
    os.system("cls||clear")


def openMenu(playerName):
    print(f"Jogador {playerName} você acaba de abrir sua pokedex.\nO que você deseja fazer agora?")
    print(f"\n1 - Visualizar Pokemaos\n2 - Duelar por Ginásios\n3 - Capturar Pokemaos\n4 - Sair")


def getNameOfPlayer():
    playerName = input("Defina seu nome:\n")
    os.system("cls||clear")
    return playerName



def infoInitialPokemons():
    print("Você precisa de pokemãos, para isso é necessário capturá-los")
    print("Ao obter 3 pokemãos, você poderá disputar batalhas em prol de se tornar um líder pokemão")
    clearTerminal()


def initializeWorld():
    os.system("cls||clear")
    print(
        "------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")


def intialStoryWithFirstPokemon(playerName, initialPokemaos, Pokemao, Player):
    print(
        "Agora você começará sua jornada no mundo pokemão.\nNote que você já começa com um pokemão e poderá capturar mais ao longo de sua jornada!")
    initialPokemao = initialPokemaos()
    pokemaoSorted = Pokemao.definitionPokemao(initialPokemao)

    player = Player(playerName, pokemaoSorted)
    clearTerminal()
    print(
        f"Mestre pokemão {player.name}, seu pokemão inicial é: " + f"{player.pokemaos[0].color} {player.pokemaos[0].name} {TextColors.ENDC}")
    clearTerminal()
    openMenu(player.name)




# Pokemao1 = Pokemao(PokemaoNamesAndTypes.CHARMAODER, 0, 0)
# Pokemao2 = Pokemao(PokemaoNamesAndTypes.MAOSAURO, 0, 0)


# player2 = Player("player2", Pokemao1)
# player2.insertPokemao(Pokemao2)
# print(player2.name + "\nPokemons:\n", player2.pokemaos[0].name + "\n", player2.pokemaos[1].name )

# player2.insertPokemao(Pokemao3)
#
# print(player2.name,player2.pokemaos[0].name, player2.pokemaos[1].name,player2.pokemaos[2].name)