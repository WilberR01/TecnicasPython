#EXERCÍCIO 1

"""

from viajante import *

N = input("Bom dia! Qual o seu nome?\n")
opcao = int(input(f"Olá {N} pra onde deseja viajar?\n1-Marrocos\n2-Paris\n3-Nova Zelândia\n"))
pessoa1 = CadastroViagem(N, opcao)
if pessoa1.RegistraDestino() == "Opção inválida.":
     print("Tente novamente.")
     pass
else:
    print(f"Sua viagem para {pessoa1.RegistraDestino()} está agendada")

"""

#EXERCICIO 2

"""

from bibliotecario import *


nome = input("Bem Vindo, qual o seu nome?\n")
usuario1 = Cadastro(nome)
print("Escolha um livro:\n")
usuario1.mostraCatalogo()
opcao = int(input())
if usuario1.validaEscolha(opcao) == 0:
    pass
else:
    print(f"Você escolheu {usuario1.escolheLivro(opcao)}Boa leitura!")

"""
#EXERCICIO 3

"""

from feira import Cadastro

nome = input("Bem vindo à nossa feira virtual!\nDigite seu nome: ")
usuario1 = Cadastro(nome)
usuario1.mostraCatalogo()
opcao = int(input("Escolha sua fruta: "))
if usuario1.validaEscolha(opcao) == 0:
    print("Opção inválida. Tente novamente.")
    pass
else:
    print(f"Ótimo {usuario1.nome}, a seguinte fruta está no seu carrinho: {usuario1.escolheFruta(opcao)}")

"""

#EXERCÍCIO 4

"""

from agenda import *

usuario1 = ConsoleAgenda()
usuario1.executar()

"""

#EXERCICIO 5

"""

from academico import *

sistema1 = Sistema()
sistema1.iniciar()

"""