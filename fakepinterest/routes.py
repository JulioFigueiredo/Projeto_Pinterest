from flask import render_template, url_for
from fakepinterest.models import Usuario
from fakepinterest import app, database, bcrypt
# url_for permite acessar o endpoint pelo nome da função
from flask_login import login_required # exige que o usuário tenha login
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto

@app.route("/", methods=["GET", "POST"]) # caminho com link do site
def homepage():
    formLogin = FormLogin()
    return render_template("homepage.html", form=formLogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) # vai criptografar a senha 
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario) # adiciona o usuário no db
        database.session.commit()
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<usuario>") # <> mostra que é uma variável
@login_required
def perfil(usuario): # variável é passada como parâmetro
    return render_template("perfil.html", usuario=usuario)