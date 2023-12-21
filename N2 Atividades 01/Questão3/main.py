from jogador import JogadorFutebol

jogador1 = JogadorFutebol("Cristiano Ronaldo", "Ataque", "05/02/1985", "Portugal", 187, 83)
print(jogador1.mostrar_dados_jogador())
print(f"Idade: {jogador1.calcular_idade()} anos")
print(f"Anos restantes para aposentadoria: {jogador1.calcular_anos_para_aposentadoria()}")
