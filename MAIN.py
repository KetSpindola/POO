from ESPECIES import Gato, Cachorro
import os

def limpatelapausa():
    print("")
    input("Enter para continuar..")
    os.system('cls')

def limpatela():
    os.system('cls')  

def menu1():
    print("Bem vindo(a)! Aqui você pode criar e interagir com um animal.")
    print("-------------------------------------------------------------")
    print("Escolha uma opção de animal:")
    print("Opção 1: Gato")
    print("Opção 2: Cachorro")
    print("-------------------")
    opcao = int(input("R= "))
    if opcao == 1:
        opcao = "Gato"
    if opcao == 2:
        opcao = "Cachorro"
    limpatelapausa()
    print(f"Você escolheu {opcao}! Agora, informe mais alguns detalhes (Obrigatórios):")
    print("------------------------------")
    raca = input(f"Qual é a raça do {opcao}? ")
    return opcao,raca

def menu2():
    print("\nSe deseja incluir mais alguma informação sobre o animal, segue opções abaixo:")
    print("-----------------------------------------------------------------------------")
    print("0- Pular/Sair")
    print("1 -Definir peso")
    print("2 -Definir altura")
    print("3- Definir cor")
    print("4- Definir idade")
    print("5- Definir brinquedo favorito")
    print("6- Definir alimento favorito")
    print("------------------------------")
    retorno = int(input("R= "))
    return retorno

def variaveis_obr(animal):
    nome = input(f"Qual é o nome do {animal}? ")
    dono = input(f"Qual é o dono(a) do {animal}? ")
    return dono,nome

def variaveis_div(animal,objeto,escolha,raca):
    dono = nome = peso = altura = idade = brinquedo = peso = alimento = None
    while True:
        print(f"Resumo de informações obtidas:")
        print(f"- Tipo {escolha}")
        print(f"- Raça {raca}")
        print(f"- Nome {nome}")
        print(f"- Dono(a) {dono}")
        opcoes = menu2()
        match opcoes:
            case 0:
                print("Você escolheu sair/pular.")
                limpatelapausa()
                return
            case 1:
                peso = input("Peso: ")
                objeto.peso = peso
                print(f"- Peso definido em {peso}")
            case 2:
                altura = input("Altura: ")
                objeto.altura = altura
                print(f"- Altura definida em {altura}")
            case 3:
                cor = input("Cor: ")
                objeto.cor = cor
                print(f"- Cor definida em {cor}")
            case 4:
                idade = input("Idade: ")
                objeto.idade = idade
                print(f"- Idade definida em {idade}")
            case 5:
                brinquedo = input("Brinquedo: ")
                objeto.brinquedo = brinquedo
                print(f"- Brinquedo favorito definido em {brinquedo}")
            case 6:
                alimento = input("Alimento: ")
                objeto.alimento = alimento
                print(f"- Alimento favorito definido em {alimento}")
        limpatelapausa()

def menu3():
    print("Agora você pode interagir com o seu animal!")
    print("Escolha uma opção:")
    print("------------------")
    print("0- Pular/Sair")
    print("1- Alimentar o animal")
    print("2- Hidratar o animal")
    print("3- Brincar com o animal")
    print("4- Botar o animal para dormir")
    print("5- Ver a identidade do animal")
    print("-----------------------------")
    retorno = int(input("R= "))
    return retorno

def acoes(objeto):
    while True:
        limpatela()
        opcao = menu3()
        limpatelapausa()
        match opcao:
            case 0:
                return
            case 1:
                objeto.comer()
            case 2:
                objeto.beber()
            case 3:
                objeto.brincar()
            case 4:
                objeto.dormir()
            case 5:
                objeto.identidade()
        limpatelapausa()


def main():
    limpatela()
    escolha,raca = menu1()
    dono,nome = variaveis_obr(escolha)
    limpatelapausa()


    objeto = Gato(dono,nome,raca)

    variaveis_div(escolha,objeto,escolha,raca)
    acoes(objeto)

if __name__ == "__main__":
    main()
