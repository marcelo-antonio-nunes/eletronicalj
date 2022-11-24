import sqlite3



class DatabaseHelper:
    def __init__(self):
        self.conn = sqlite3.connect("./gavetario.db")
        self.cursor = self.conn.cursor()
    
    def cria_tabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS componente(\
            gaveta VARCHAR(10) NOT NULL, tipo VARCHAR(20) NOT NULL,\
                codigo VARCHAR(10) NOT NULL,\
                    quantidade INTEGER NOT NULL);")
    
    def cadastar_gaveta(self,c):
        self.cursor.execute("INSERT INTO componente(gaveta, tipo, codigo, quantidade)\
            VALUES(?,?,?,?)",([c.gaveta, c.tipo, c.codigo, c.quantidade]))
        self.conn.commit()

    def adicionar_componentes(self, gaveta, quantidade):
        quantidade_na_gaveta = self.cursor.execute("select quantidade from componente WHERE gaveta=?",[gaveta]).fetchone()[0]
        nova_quantidade =int(quantidade_na_gaveta) + int(quantidade)
        self.cursor.execute("UPDATE componente SET quantidade =? where gaveta=?",\
            [nova_quantidade,gaveta])
        self.conn.commit()


    def retirar_componentes(self, gaveta, quantidade):
        quantidade_na_gaveta = int(self.cursor.execute("select quantidade from componente WHERE gaveta=?",[gaveta]).fetchone()[0])
        if quantidade_na_gaveta >= int(quantidade):
            nova_quantidade = quantidade_na_gaveta - int(quantidade)
            self.cursor.execute("UPDATE componente SET quantidade =? where gaveta=?",\
                [nova_quantidade,gaveta])
            self.conn.commit()
            return
        print("gaveta vazia!")

    
    
    def listar_todos(self):
        result = self.cursor.execute("SELECT * FROM componente")
        return result.fetchall()
        
        


