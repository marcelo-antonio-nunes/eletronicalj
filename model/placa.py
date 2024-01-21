

class Placa:
    def __init__(self, caixa, marca, modelo, tipo, codigo, quantidade, foto):
        self.caixa = caixa.upper()
        self.marca = marca.upper()
        self.modelo = modelo.upper()
        self.tipo = tipo.upper()
        self.codigo = codigo.upper()
        self.quantidade = quantidade
        self.foto =  foto
