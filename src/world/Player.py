import os
from Pokemao import *
import math
from Utils import TextColors


class Player:
    pokemaos = []

    def __init__(self, name, pokemaos):
        self.name = name
        self.pokemaos.append(pokemaos)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def insertPokemao(self, pokemao):
        if (len(self.pokemaos) > 2):
            print("Você já possui o limite máximo de 3 Pokemaos, se desfaça de um pokemon para adquirir outro")
            return
        self.pokemaos.append(pokemao)
        return True

    def openMenu(self, playerName):
        os.system("cls||clear")
        print(f"Jogador {playerName} você acaba de abrir sua pokedex.\nO que você deseja fazer agora?")
        print(f"\n1 - Visualizar Pokemaos\n2 - Duelar por Ginásios\n3 - Capturar Pokemaos\n4 - Sair")

    def presentPokemaos(self):
        os.system("cls||clear")
        print("--- Lista de Pokemaos ---")
        for x in self.pokemaos:
            print(x.name)
        input("Enter para voltar")

    def initialMsg(self):
        os.system("cls||clear")
        print("Qual pokemao você deseja utilizar?")

    def presentationPokemonList(self):
        for index, x in enumerate(self.pokemaos):
            print(f"{index + 1} - ", x.name)

    def choicePokemon(self, pokemaoRandom):
        option = input("Opção: ")
        os.system("cls||clear")
        print(f"Seu pokemao escolhido foi: ",
              self.pokemaos[int(option) - 1].color + self.pokemaos[
                  int(option) - 1].name + TextColors.ENDC)
        print(f'--- Você acaba de encontrar o pokemon: ', pokemaoRandom.color + pokemaoRandom.name + TextColors.ENDC)
        input("Enter para iniciar a tentativa de capturar o pokemao")
        return option

    def battle(self, option):
        getWinner = random.randint(0, 100)
        if getWinner > 0 & getWinner < 74:
            self.pokemaos[int(option) - 1].experience += 35
            os.system("cls||clear")
            print(f"Seu pokemao ganhou 35 de Experiência: ", self.pokemaos[int(option) - 1].color + self.pokemaos[
                int(option) - 1].name + "++" + TextColors.ENDC)
            input("Enter para continuar")
            os.system("cls||clear")
            self.pokemaos[int(option) - 1].level = math.floor(self.pokemaos[int(option) - 1].experience / 100)
            print(
                f"Seu pokemão {self.pokemaos[int(option) - 1].color}  {self.pokemaos[int(option) - 1].name}{TextColors.ENDC}\nestá no level: " + f"{self.pokemaos[int(option) - 1].color} {self.pokemaos[int(option) - 1].level} {TextColors.ENDC} e com " + f"{self.pokemaos[int(option) - 1].color} {self.pokemaos[int(option) - 1].experience} {TextColors.ENDC} de XP")
            return True
        else:
            print("Seu pokemao foi derrotado, tente novamente")
            return False

    def capturePokemao(self, pokemaoRandom):
        self.initialMsg()
        self.presentationPokemonList()
        option = self.choicePokemon(pokemaoRandom)
        winner = self.battle(option)
        if winner:
            capture = input("Deseja capturar este pokemon?\n1 - Sim\n2 - Não")
            if int(capture) == 1:
                captured = self.insertPokemao(pokemaoRandom)
                if captured:
                    print("Pokemon Capturado com sucesso")
            else:
                print("Você poderá capturar mais pokemaos durante a sua jornada")

    def GenerateRandomPokemonToCapture(self):
        result = ""
        os.system("cls||clear")
        print("--- É Hora de Capturar Pokemaos ---")
        pokemaoRandom = generateRandomPokemon(Levels.BOSS.name)
        self.capturePokemao(pokemaoRandom)
        input("Enter para voltar")

    def pokedex(self, optionUser):
        while optionUser != 4:
            match optionUser:
                case "1":
                    self.presentPokemaos()
                case "2":
                    os.system("cls||clear")
                    print("--- É hora de Duelar ---")
                    input("Enter para voltar")
                case "3":
                    self.GenerateRandomPokemonToCapture()
                case _:
                    os.system("cls||clear")
                    print("Fim de jogo")
                    break;
            self.openMenu(self.name)
            optionUser = input("Opção: ")
