from flask import Flask, request, render_template, redirect
from model.componente import Componente
from sqlitehelper.database import DatabaseHelper as db


app = Flask(__name__)


# ----------------------------------------------busca
@app.route('/busca',methods=['POST'])
def busca():
    dt = db()
    componente = request.form['componente']
    lista = dt.busca_componente(componente)
    return render_template('lista.html', lista=lista)
    
# ----------------------------------------------fim

# ----------------------------------------------page inicial
@app.route('/',methods=['GET',])
def index():
    dt = db()
    dt.cria_tabela()
    return render_template('index.html')
# ---------------------------------------------fim


# ---------------------------------------------- lista todos as gavetas
@app.route('/lista')
def lista():
    dt = db()
    componentes = dt.listar_todos()
    itens = len(componentes)
    return render_template('lista.html', lista=componentes, len=itens)

# ---------------------------------------------- cria nova gaveta


@app.route('/cadastrar', methods=['GET',])
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/novo', methods=['POST',])
def novo():
    componente = Componente(
        request.form["gaveta"],
        request.form["tipo"],
        request.form["codigo"],
        request.form["quantidade"])
    if componente.gaveta == "" or\
       componente.tipo == "" or\
       componente.codigo == "" or\
       componente.quantidade == "":
        return redirect('/lista')
    else:
        dt = db()
        dt.cadastar_gaveta(componente)
        return redirect('/lista')

#----------------------------------------- fim


# --------------------------------------- adicionar componente
@app.route('/entrada', methods=['GET',])
def entrada():
    return render_template("entrada.html")


@app.route('/adicionar', methods=['POST',])
def adicionar():
    dt = db()
    g = request.form["gaveta"]
    c = request.form["quantidade"]
    dt.adicionar_componentes(g, c)
    return redirect('/lista')
# --------------------------------------- fim

# --------------------------------------- retirar componente


@app.route('/saida', methods=['GET',])
def saida():
    return render_template("saida.html")


@app.route('/retirar', methods=['POST',])
def retirar():
    dt = db()
    g = request.form["gaveta"]
    c = request.form["quantidade"]
    dt.retirar_componentes(g, c)
    return redirect("/lista")
# ------------------------------------fim


app.run(host='0.0.0.0', port=5000, debug=True)
