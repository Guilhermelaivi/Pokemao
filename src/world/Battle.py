import os
from Utils import TextColors
import random


class Battle:


    def initialMsg(self):
        os.system("cls||clear")
        print("Qual pokemao você deseja utilizar?")

    def presentationPokemonList(self, player):
        for index, x in enumerate(player.pokemaos):
            print(f"{index + 1} - ", x.name)

    def choicePokemon(self, player, pokemaoRandom):

        print(f"Seu pokemao escolhido foi: ",
              player.pokemaos[int(self.option) - 1].color + player.pokemaos[
                  int(self.option) - 1].name + TextColors.ENDC)
        print(f'--- Você acaba de encontrar o pokemon: ', pokemaoRandom.color + pokemaoRandom.name + TextColors.ENDC)
        input("Enter para iniciar a tentativa de capturar o pokemao")

    # def battleOnCapturePokemao(self, player):
    #     getWinner = random.randint(0, 100)
    #     if getWinner > 0 & getWinner < 74:
    #         player.pokemaos[int(self.option) - 1].experience += 35
    #         os.system("cls||clear")
    #         print(f"Seu pokemao ganhou 20 de Experiência: ",
    #               player.pokemaos[int(self.option) - 1].color + player.pokemaos[
    #                   int(self.option) - 1].name + "++" + TextColors.ENDC)
    #         print(f"EXP ATUUAL: ", player.pokemaos[int(self.option) - 1].color + player.pokemaos[
    #             int(self.option) - 1].name + TextColors.ENDC + " " + str(
    #             player.pokemaos[int(self.option) - 1].experience) + " XP")
    #         input("Enter para continuar")
    #         if player.pokemaos[int(self.option) - 1].experience > 100:
    #             os.system("cls||clear")
    #             print("EVOLUIU!!!!!!")
    #             player.pokemaos[int(self.option) - 1].level += 1
    #             print(
    #                 f"Seu pokemão {player.pokemaos[int(self.option) - 1].color}  {player.pokemaos[int(self.option) - 1].name}{TextColors.ENDC}\nEvoluiu para o level: " + f"{player.pokemaos[0].color} {player.pokemaos[0].level} {TextColors.ENDC} e com " + f"{player.pokemaos[0].color} {player.pokemaos[0].experience} {TextColors.ENDC} de XP")
    #     else:
    #         print("Seu pokemao foi derrotado, tente novamente")

    def __init__(self, player, pokemaoRandom):
        self.initialMsg()
        self.presentationPokemonList(player.pokemaos)
        self.choicePokemon(player, pokemaoRandom)
        self.battleOnCapturePokemao(player)
