class Funcionario():
    def __init__(self, nome, idade, cpf, salario, cargo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

        self.ordemPendente = []

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade} - Cargo: {self.cargo} - Salário: {self.salario} - CPF: {self.cpf}'
    
    def novaOrdem(self, ordem):
        indice = len(self.ordemPendente) + 1
        ordemLimpa = (indice, ordem)
        self.ordemPendente.append(ordemLimpa)

    def mostraOrdens(self):
        if self.ordemPendente:
            print(f"Ordens pendentes para {self.nome}:")
            for ordem in self.ordemPendente:
                print(ordem)
        else:
            print(f"Nenhuma ordem pendente para {self.nome}.")

    def concluiOrdem(self):
        opcao = int(input("Ordem concluída: "))
        self.ordemPendente.remove(self.ordemPendente[opcao - 1])

