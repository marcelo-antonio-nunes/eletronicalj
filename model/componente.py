class Componente:
    def __init__(self, gaveta, tipo, codigo, quantidade, foto):
        self.gaveta = gaveta.upper()
        self.tipo = tipo.upper()
        self.codigo = codigo.upper()
        self.quantidade = quantidade.upper()
        self.foto = foto.upper()