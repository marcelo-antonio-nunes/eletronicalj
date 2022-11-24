from flask import Flask, request, render_template, redirect
from model.componente import Componente
from sqlitehelper.database import DatabaseHelper as db



app = Flask(__name__)

@app.route('/lista')
def lista():
    dt = db()
    componentes = dt.listar_todos()
    itens=len(componentes)
    return render_template('lista.html',lista=componentes,len=itens)

@app.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    dt = db()
    if request.method == "POST":
        componente = Componente(
            request.form["gaveta"],
            request.form["tipo"],
            request.form["codigo"],
            request.form["quantidade"])
        dt.cria_tabela()
        dt.cadastar_gaveta(componente)
        redirect("/lista")
    return render_template('cadastrar.html',)


@app.route('/saida', methods=['POST','GET'])
def saida():
    dt = db()
    if request.method == "POST":
        g = request.form["gaveta"]
        c = request.form["quantidade"]
        dt.retirar_componentes(g, c)
        redirect("/lista")
    return render_template("saida.html")

@app.route('/entrada', methods=['POST','GET'])
def entrada():
    if request.method == "POST":
        dt = db()
        g = request.form["gaveta"]
        c = request.form["quantidade"]
        dt.adicionar_componentes(g, c)
        return render_template("lista.html")
    else:
        return render_template("entrada.html")



app.run(host='0.0.0.0', port=5000, debug=True)

