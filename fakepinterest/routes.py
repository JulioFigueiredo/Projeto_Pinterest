from flask import render_template, url_for
from fakepinterest import app
# url_for permite acessar o endpoint pelo nome da função
from flask_login import login_required # exige que o usuário tenha login
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"]) # caminho com link do site
def homepage():
    formLogin = FormLogin()
    return render_template("homepage.html", form=formLogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)


@app.route("/perfil/<usuario>") # <> mostra que é uma variável
@login_required
def perfil(usuario): # variável é passada como parâmetro
    return render_template("perfil.html", usuario=usuario)