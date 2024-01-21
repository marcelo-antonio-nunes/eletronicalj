class Componente:
    def __init__(self, gaveta, tipo, codigo, quantidade):
        self.gaveta = gaveta.upper()
        self.tipo = tipo.upper()
        self.codigo = codigo.upper()
        self.quantidade = quantidade.upper()