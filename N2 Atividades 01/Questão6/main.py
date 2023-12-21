from elevador import *

elevador = Elevador(10, 5)

print(f"Andar atual: {elevador.get_andar_atual()}")
print(f"Pessoas presentes: {elevador.get_pessoas_presentes()}")

elevador.entrar()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.sair()
elevador.descer()
elevador.subir()
elevador.subir()
elevador.descer()


print(f"Andar atual: {elevador.get_andar_atual()}")
print(f"Pessoas presentes: {elevador.get_pessoas_presentes()}")
