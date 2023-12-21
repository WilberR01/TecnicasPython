from datetime import datetime

class JogadorFutebol:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def set_posicao(self, posicao):
        self.posicao = posicao

    def get_posicao(self):
        return self.posicao

    def calcular_idade(self):
        hoje = datetime.now()
        idade = hoje.year - self.data_nascimento.year
        if hoje.month < self.data_nascimento.month or (hoje.month == self.data_nascimento.month and hoje.day < self.data_nascimento.day):
            idade -= 1
        return idade

    def calcular_anos_para_aposentadoria(self):
        if self.posicao == "Defesa":
            aposentadoria = 40
        elif self.posicao == "Meio-campo":
            aposentadoria = 38
        elif self.posicao == "Ataque":
            aposentadoria = 35
        else:
            aposentadoria = 0
        idade_atual = self.calcular_idade()
        anos_para_aposentar = aposentadoria - idade_atual
        if anos_para_aposentar > 0:
            return anos_para_aposentar
        else:
            return "O jogador já se aposentou."

    def mostrar_dados_jogador(self):
        return f"Nome: {self.nome}\nPosição: {self.posicao}\nData de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}\nNacionalidade: {self.nacionalidade}\nAltura: {self.altura} cm\nPeso: {self.peso} kg"

