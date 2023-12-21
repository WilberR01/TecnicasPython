class Usuario:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Gerenciamento:
    def __init__(self):
        self.usuarios = []
    
    def cadastraUsuario(self, usuario):
        self.usuarios.append(usuario)

    def removerUsuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                self.usuarios.remove(usuario)
                return
        print(f"Usuario com o nome '{nome}' não encontrado no sistema.")
    
    def listarUsuarios(self):
        if not self.usuarios:
            print("O sistema está limpo")
        else:
            for usuario in self.usuarios:
                print(usuario)

class Aluno(Usuario):
    def __init__(self, nome, cpf, idade, curso):
        super().__init__(nome, cpf, idade)
        self.curso = curso

    def __str__(self) -> str:
        return f"Aluno: {self.nome} \n- Idade: {self.idade} \n- Curso: {self.curso} \n- CPF: {self.cpf}"

class Professor(Usuario):
    def __init__(self, nome, cpf, idade, graduacao):
        super().__init__(nome, cpf, idade)
        self.graduacao = graduacao

    def __str__(self) -> str:
        return f"Docente: {self.nome} \n- Idade: {self.idade}\n- Graduação: {self.graduacao} \n- CPF: {self.cpf}"
    
class Sistema:
    def __init__(self):
        self.sistema = Gerenciamento()

    def iniciar(self):
        while True:
            print("\nGERENCIAMENTO ACADÊMICO")
            print("1. Adicionar Usuário")
            print("2. Remover Usuário")
            print("3. Listar Usuários")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n1-Cadastrar Aluno\n2-Cadastrar Professor")
                subOpcao = input("Opção: ")

                if subOpcao == "1":
                    nome = input("Digite o nome do aluno: ")
                    cpf = input("Digite o cpf do aluno: ")
                    idade = input("Digite o idade do aluno: ")
                    curso = input("Digite o curso do aluno: ")
                    novoAluno = Aluno(nome, cpf, idade, curso)
                    self.sistema.cadastraUsuario(novoAluno)
                    print("Aluno adicionado com sucesso.")
                elif subOpcao == "2":
                    nome = input("Digite o nome do professor: ")
                    cpf = input("Digite o cpf do professor: ")
                    idade = input("Digite o idade do professor: ")
                    graduacao = input("Digite a graduacao do professor: ")
                    novoProfessor = Professor(nome, cpf, idade, graduacao)
                    self.sistema.cadastraUsuario(novoProfessor)
                    print("Professor adicionado com sucesso.")
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
                    
            elif opcao == "2":
                nome = input("Digite o nome do usuário que deseja remover: ")
                self.sistema.removerUsuario(nome)
            elif opcao == "3":
                print("\n--- Lista de Usuários ---")
                self.sistema.listarUsuarios()
            elif opcao == "4":
                print("Saindo do Sistema")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
