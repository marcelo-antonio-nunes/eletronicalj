from flask import Flask, request, render_template, redirect, url_for, flash
from model.componente import Componente
from model.placa import Placa
from sqlitehelper.database import DatabaseHelper as db
import subprocess
import sqlite3


app = Flask(__name__)
app.secret_key = 'SiTGBNzZ'


# ----------------------------------------------busca
@app.route('/busca', methods=['POST'])
def busca():
    dt = db()
    componente = request.form['componente']
    lista = dt.busca_componente(componente)
    return render_template('lista.html', lista=lista)
# ----------------------------------------------fim

# ----------------------------------------------page inicial


@app.route('/', methods=['GET',])
def index():
    dt = db()
    return render_template('index.html')
# ---------------------------------------------fim

# ---------------------------------------------- lista todos as gavetas


@app.route('/lista')
def lista():
    dt = db()
    componentes = dt.listar_todos()
    return render_template('lista.html', lista=componentes.fetchall())
# ---------------------------------------------- cria nova gaveta


@app.route('/cadastrar', methods=['GET',])
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/novo', methods=['POST'])
def novo():
    if request.form['acao'] == 'cadastrar':
        componente = Componente(
            request.form["gaveta"],
            request.form["tipo"],
            request.form["codigo"],
            request.form["quantidade"],
            request.form["fotoC"])
        print(f"Foto -> {request.form['fotoC']}")
        if componente.gaveta == "" or\
                componente.tipo == "" or\
                componente.codigo == "" or\
                componente.quantidade == "":
            return redirect(url_for('lista'))
        else:
            dt = db()
            result = dt.cadastar_gaveta(componente)
            if result == False:
                return render_template('erro_modal.html')
            dt.listar_todos()
            return redirect(url_for('lista'))
# ----------------------------------------- fim

# ------- adicionar componente ----------------


@app.route('/entrada', methods=['GET',])
def entrada():
    return render_template("entrada.html")
# ---- seleciona o registro atual ----


def registro_atual():
    dt = db()
    id = request.form['id']
    dt = db()
    registro = dt.seleciona_registro(id)
    return registro
# -------fim--------------------------

# --------seleciona a gaveta metodo para ação----------


@app.route('/seleciona', methods=['POST'])
def seleciona():
    if request.form['acao'] == "editar":
        registro = registro_atual()
        return render_template('editar.html', registro=registro)
    elif request.form['acao'] == "retirar":
        registro = registro_atual()
        return render_template('saida.html', registro=registro)
    elif request.form['acao'] == "adicionar":
        registro = registro_atual()
        return render_template('entrada.html', registro=registro)


@app.route('/altera_quantidade', methods=['POST', 'GET'])
def altera_quantidade():
    dt = db()
    dt.editar_quant(request.form['id'],  request.form['quantidade'])
    return redirect(url_for('lista'))


@app.route('/atualizar', methods=['POST'])
def atualizar():
    id = request.form["id"]
    componente = Componente(
        request.form["gaveta"],
        request.form["tipo"],
        request.form["codigo"],
        request.form["quantidade"],
        request.form["foto"])
    dt = db()
    result = dt.editar_componentes(id, componente)
    if result == False:
        flash("Ja existe essa gaveta!")
        return render_template('erro_modal.html')
    return redirect(url_for('lista'))
##########################################################
######################### PLACAS #########################
##########################################################


@app.route('/placas', methods=['POST'])
def placas():
    return render_template("cadastrar_placa.html")


@app.route('/nova_placa', methods=['POST'])
def adicionar_placa():
    placa = Placa(
        request.form['caixa'],
        request.form['marca'],
        request.form['modelo'],
        request.form['tipo'],
        request.form['codigo'],
        request.form['quantidade'],
        request.form['foto']
    )
    print(f"Foto -> {request.form['foto']}")
    dt = db()
    result = dt.cadastar_placas(placa)
    if result == False:
        flash("Ja existe essa caixa!")
        return render_template('erro_modal.html')
    return redirect('lista_placas')


@app.route('/listar_caixas')
def listarcaixas():
    dt = db()
    lista = dt.busca_placas()
    return render_template('lista_placas.html', lista=lista)


@app.route('/lista_placas')
def lista_placa():
    dt = db()
    lista = dt.busca_placas()
    return render_template('lista_placas.html', lista=lista)


@app.route('/busca_placa', methods=['POST'])
def busca_p():
    dt = db()
    placa = request.form["pc"]
    lista = dt.busca_placa(placa)
    return render_template('lista_placas.html', lista=lista)


@app.route('/altera_quantidade_p', methods=['POST', 'GET'])
def altera_quantidadep():
    dt = db()
    print(f"\nId {request.form['id']} e Quantidade {request.form['quantidade_p']}\n")
    dt.editar_quant_p(request.form['id'],  request.form['quantidade_p'])
    return redirect('lista_placas')


@app.route('/seleciona_p', methods=['POST'])
def selecionap():
    if request.form['acao'] == "editar_p":
        registro = registro_atual_p()
        return render_template('editar_placa.html', registro=registro)
    elif request.form['acao'] == "retirar_p":
        registro = registro_atual_p()
        return render_template('retirar_placa.html', registro=registro)
    elif request.form['acao'] == "adicionar_p":
        registro = registro_atual_p()
        return render_template('adicionar_placa.html', registro=registro)


def registro_atual_p():
    dt = db()
    id = request.form['id']
    dt = db()
    registro_p = dt.seleciona_registro_p(id)
    return registro_p


@app.route('/atualizar_caixa', methods=['POST'])
def atualizar_caixa():
    id = request.form["id"]
    placas = Placa(
        request.form["caixa"],
        request.form["marca"],
        request.form["modelo"],
        request.form["tipo"],
        request.form["codigo"],
        request.form["quantidade"],
        request.form["foto"])
        
    dt = db()
    result = dt.editar_caixa(id, placas)
    if result == False:
        flash("Ja existe essa caixa!")
        return render_template('erro_modal.html')
    return redirect('lista_placas')
#====================================================

#-------- Led -------------------------------------

# Configuração do SQLite
DATABASE = 'banco_de_dados/gavetario.db'

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect(DATABASE)

# Rota para a página de cadastro
@app.route('/cadastrar_led', methods=['GET', 'POST'])
def cadastrar_led():
    if request.method == 'POST':
        modelo_tv = request.form['modelo_tv']
        quantidade = request.form['quantidade']
        
        # Insere os dados no banco de dados
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO led (modelo_tv, quantidade) VALUES (?, ?)", (modelo_tv, quantidade))
        connection.commit()
        connection.close()

    return render_template('cadastrar_led.html')

# Rota para a página de busca
@app.route('/buscar_led', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        modelo_tv = request.form['modelo_tv']

        # Busca no banco de dados pelo modelo de TV
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM led WHERE modelo_tv=?", (modelo_tv,))
        result = cursor.fetchall()
        connection.close()

        if result:
            return render_template('buscar_led.html', result=result)
        else:
            return render_template('buscar_led.html', not_found=True)

    return render_template('buscar_led.html')

# Rota para a página de baixa ou adição

# Rota para editar o LED
@app.route('/editar_led/<int:id>', methods=['POST'])
def editar_led(id):
    if request.method == 'POST':
        nova_quantidade = request.form['quantidade']
        novo_modelo_tv = request.form['modelo_tv']

        # Atualiza a quantidade no banco de dados
        connection = connect_db()
        cursor = connection.cursor()
        # cursor.execute("UPDATE led SET quantidade = ?, modelo_tv= ?,  WHERE id = ?" (nova_quantidade,novo_modelo_tv, id))
        cursor.execute("UPDATE led SET quantidade = ?, modelo_tv = ? WHERE id = ?", (nova_quantidade, novo_modelo_tv, id))

        connection.commit()
        connection.close()

    # Redireciona de volta para a página de busca após a edição
    return redirect(url_for('buscar'))
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def realizar_backup():
    # Substitua 'caminho_para_backup.py' pelo caminho real do seu script de backup
    subprocess.run(["python", "backup.py"])

# Rota para lidar com a solicitação de backup
@app.route('/backup', methods=['POST'])
def backup():
    senha_digitada = request.form.get('senha')

    # Verifica se a senha está correta
    if senha_digitada == 'eletronica@leo':
        realizar_backup()
        return 'Backup realizado com sucesso!'
    else:
        return 'Senha incorreta. Backup não realizado.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
