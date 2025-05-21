from flask import render_template, url_for
from fakepinterest import app
# url_for permite acessar o endpoint pelo nome da função


@app.route("/") # caminho com link do site
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") # <> mostra que é uma variável
def perfil(usuario): # variável é passada como parâmetro
    return render_template("perfil.html", usuario=usuario)