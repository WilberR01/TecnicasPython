class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return
        print(f"Contato com o nome '{nome}' não encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for contato in self.contatos:
                print(contato)


class ConsoleAgenda:
    def __init__(self):
        self.agenda = Agenda()

    def executar(self):
        while True:
            print("\n*** Agenda de Contatos ***")
            print("1. Adicionar Contato")
            print("2. Remover Contato")
            print("3. Listar Contatos")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o telefone do contato: ")
                contato = Contato(nome, telefone)
                self.agenda.adicionar_contato(contato)
                print("Contato adicionado com sucesso.")
            elif opcao == "2":
                nome = input("Digite o nome do contato que deseja remover: ")
                self.agenda.remover_contato(nome)
            elif opcao == "3":
                print("\n--- Lista de Contatos ---")
                self.agenda.listar_contatos()
            elif opcao == "4":
                print("Saindo da agenda.")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
