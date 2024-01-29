import sqlite3
from typing import Type
from model.componente import Componente
from model.placa import Placa

class DatabaseHelper:
    

    def db_execute(func):
        def decorador(*args):
            conn = sqlite3.connect("banco_de_dados/gavetario.db")
            cur = conn.cursor()
            try:
                cur.execute(func(*args))
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                conn.close()
                print(f'Erro {e}')
                return False
        return decorador
    
    @db_execute
    def cadastar_gaveta(self, c:Type[Componente]):
        return "INSERT INTO componente(gaveta, tipo, codigo, quantidade)VALUES('{}','{}','{}','{}')"\
            .format(c.gaveta, c.tipo, c.codigo, c.quantidade)
    
    @db_execute
    def editar_quant(self, id, quantidade):
         if int(quantidade) >= 0:
            return "UPDATE componente SET quantidade ='{}' where id='{}'".format(int(quantidade), id)
         return
    
    @db_execute
    def editar_componentes(self, id_gaveta, c:Type[Componente]):
        return "UPDATE componente SET gaveta='{}', tipo='{}', codigo='{}', quantidade='{}' WHERE id='{}'"\
        .format(c.gaveta, c.tipo, c.codigo, c.quantidade, id_gaveta)
        
    def listar_todos(self):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        query = "SELECT * FROM componente ORDER BY gaveta"
        result = cur.execute(query)
        return result

    def busca_componente(self, c:Type[Componente]):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        query = "SELECT * FROM componente WHERE codigo LIKE ? or tipo LIKE ? or gaveta LIKE ? ORDER BY gaveta"
        params = ["%"+c+"%", "%"+c+"%", "%"+c+"%"]
        result = cur.execute(query, params)
        return result.fetchall()

    def seleciona_registro(self, id):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        result = cur.execute('SELECT * FROM componente WHERE id = ?', (id,))
        return result.fetchone()
    
####################################################################################
################################# Placas ###########################################
    
    @db_execute
    def cadastar_placas(self, p:Type[Placa]):
        return "INSERT INTO placas(caixa, marca, modelo, tipo, codigo, quantidade, foto)VALUES('{}','{}','{}','{}','{}','{}','{}')"\
        .format(p.caixa, p.marca, p.modelo, p.tipo, p.codigo, p.quantidade, p.foto)
    
    @db_execute
    def editar_placa(self, p:Type[Placa]):
        return "UPDATE placas SET caixa=?, marca='{}', modelo='{}', tipo='{}', codigo='{}', quantidade='{}' WHERE id='{}'"\
        .format(p.caixa, p.marca, p.modelo, p.tipo, p.codigo, p.quantidade, p.id)
    

    @db_execute    
    def editar_quant_p(self, id, quantidade_p):
        print(f"\nCheguei aqui\n com Id: {id}, e Quntidade:{quantidade_p}\n")
        if int(quantidade_p) >= 0:
            return "UPDATE placas SET quantidade ='{}' where id='{}'".format(int(quantidade_p), id)
        return
            
    @db_execute
    def editar_caixa(self, id_placa, p:Type[Placa]):
        return "UPDATE placas SET caixa='{}', marca='{}', modelo='{}',tipo='{}', codigo='{}', quantidade='{}', foto='{}' WHERE id='{}'"\
        .format(p.caixa, p.marca, p.modelo, p.tipo, p.codigo, p.quantidade, p.foto, id_placa)
    
    def busca_placas(self):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        query = "SELECT * FROM placas"
        cur.execute(query)
        result = cur.fetchall()
        return result
    
    def busca_placa(self, p):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        query = "SELECT * FROM placas WHERE  caixa LIKE ? or marca LIKE ? or modelo LIKE ? or codigo LIKE ? or tipo LIKE ? ORDER BY caixa"
        params = ["%"+p+"%", "%"+p+"%", "%"+p+"%", "%"+p+"%", "%"+p+"%"]
        cur.execute(query, params)
        result = cur.fetchall()
        return result
    
    def seleciona_registro_p(self, id):
        con = sqlite3.connect("banco_de_dados/gavetario.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM placas WHERE id = ?', (id,))
        result = cur.fetchone()
        return result
