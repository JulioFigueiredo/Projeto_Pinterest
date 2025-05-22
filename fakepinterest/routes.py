from flask import render_template, url_for
from fakepinterest import app
# url_for permite acessar o endpoint pelo nome da função
from flask_login import login_required # exige que o usuário tenha login

@app.route("/") # caminho com link do site
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") # <> mostra que é uma variável
@login_required
def perfil(usuario): # variável é passada como parâmetro
    return render_template("perfil.html", usuario=usuario)