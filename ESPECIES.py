from ANIMAIS import Animal

class Gato(Animal):
    def __init__(self,dono,nome,raca):
        super().__init__(dono,nome)
        self.raca = raca
        self.alimento = "Whiskas"

    def identidade(self):
        print(f"Gato {self.nome} - Raça {self.raca}")
        super().identidade()

    def som(self):
        super().som()
        print("Miau, miau...")

class Cachorro(Animal):
    def __init__(self,dono,nome,raca):
        super().__init__(dono,nome)
        self.raca = raca
        self.alimento = "Pedigree"

    def identidade(self):
        print(f"Cachorro {self.nome} - Raça {self.raca}")
        super().identidade()

    def som(self):
        super().som()
        print("Au, au...")