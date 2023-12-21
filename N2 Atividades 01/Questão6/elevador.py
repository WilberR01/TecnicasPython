class Elevador:
    def __init__(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.andar_atual = 0
        self.pessoas_presentes = 0

    def entrar(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
        else:
            print("O elevador está cheio. Não é possível entrar mais pessoas.")

    def sair(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
        else:
            print("O elevador está vazio. Não é possível remover pessoas.")

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print("O elevador já está no último andar. Não é possível subir mais.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print("O elevador já está no térreo. Não é possível descer mais.")

    
    def get_andar_atual(self):
        return self.andar_atual

    def get_pessoas_presentes(self):
        return self.pessoas_presentes

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def set_total_andares(self, total_andares):
        self.total_andares = total_andares

