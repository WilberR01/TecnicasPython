class triangulo:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.Lados = [self.A, self.B, self.C]
        pass
           
    def testaT(self):
        if self.A < self.B + self.C and self.B < self.C + self.A and self.C < self.B + self.A:
            return True
        else:
            print('Este não é um triângulo válido')
            return False
            
    def calcularPerimetro(self):
        if triangulo.testaT(self):
            print(sum(self.Lados));
        
    def MaiorLado(self):
        if triangulo.testaT(self):
            print(max(self.Lados));
        
