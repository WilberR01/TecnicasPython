class Carro:
    def __init__(self, nome, marca, statusMotor=False, statusMovimento=False):
        self.nome = nome
        self.marca = marca
        self.statusMotor=statusMotor
        self.statusMovimento=statusMovimento

    def StartStop(self):
        if self.statusMotor:
            print ('Desligando motor')
            self.statusMotor = False
        else: 
            print('Ligando motor')
            self.statusMotor = True
    
    def Movimento(self):
        if not self.statusMotor:
            print ('O carro está desligado, primeiro ligue o motor')
        else:
            if self.statusMovimento:
                print ('O carro já está em movimento')
            else:
                self.statusMovimento = True
                print ('Arrancando...')

    def Info(self):
        if self.statusMotor:
            print ('Motor Ligado')
        else: 
            print('Motor desligado')
        if self.statusMovimento:
            print ('Veiculo em movimento')
        else:
            print (' Veiculo parado')
