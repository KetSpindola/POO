import time

class Animal():
    def __init__(self,dono,nome):
        #Obrigatorias
        self.dono = dono 
        self.nome = nome 
        #Opcionais
        self.peso = None 
        self.altura = None 
        self.idade = None 
        self.brinquedo = None 
        self.cor = None 
        self.alimento = None 

        #Ideias de funções:
        #BANHO
        #FREBE
        #VACINA
        #REMEDIOS
        #DOENTE

    def identidade(self):
        print("Informações gerais:")
        print("-------------------")
        print(f"- Dono: {self.dono}")
        print(f"- Nome: {self.nome}")
        if self.altura is not None:
            print(f"- Altura: {self.altura}")
        if self.peso is not None:
            print(f"- Peso: {self.peso}")
        if self.idade is not None:
            print(f"- Idade: {self.idade}")
        if self.cor is not None:
            print(f"- Cor: {self.cor}")
        if self.brinquedo is not None:
            print(f"- Brinquedo favorito: {self.brinquedo}")
        if self.alimento is not None:
            print(f"- Alimento favorito: {self.alimento}")

    def comer(self):
        print("Alimentando o Animal:")
        print("---------------------------")
        print(f"{self.dono} esta servindo a ração do animal...")
        time.sleep(1)
        if self.alimento is not None:
            print(f"Incluindo o alimento favorito... {self.alimento}")
        self.som()
        time.sleep(2)
        print(f"{self.nome} esta comendo...")
        time.sleep(2)
        print(f"{self.nome} esta alimentado!")

    def beber(self):
        print("Hidratando o Animal:")
        print("---------------------------")
        print(f"{self.nome} esta indo até o pote de água...")
        time.sleep(2)
        print(f"{self.nome} esta bebendo a água...")
        time.sleep(2)
        print(f"{self.nome} esta hidratado!")

    def brincar(self):
        print("Brincando com o Animal:")
        print("---------------------------")
        if self.brinquedo is not None:
            self.som()
            print(f"{self.dono} foi buscar o {self.brinquedo}")
            time.sleep(2)
            print(f"{self.dono} esta brincando com {self.raca} {self.nome}!")
            time.sleep(2)
            print(f"Os dois brincaram bastante, hora de descansar!")
        else:
            print("Primeiro, defina um brinquedo para o Animal.")
    
    def dormir(self):
        print("Descansando o animal:")
        print("---------------------------")
        print(f"{self.nome} esta indo até a sua cama.")
        time.sleep(2)
        print(f"{self.nome} acordou e esta descansado!")

    def som(self):
        print(f"O animal esta murmurando...")