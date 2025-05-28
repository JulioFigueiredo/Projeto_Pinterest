from flask import render_template, url_for, redirect
from fakepinterest.models import Usuario
from fakepinterest import app, database, bcrypt
# url_for permite acessar o endpoint pelo nome da função
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto

@app.route("/", methods=["GET", "POST"]) # caminho com link do site
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first() # procura o usuário por email
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data): # verifica se existe o usuario e a senha corresponde a senha criptografada
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=formLogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) # vai criptografar a senha 
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario) # adiciona o usuário no db
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id)) # redireciona para a função perfil a partir do username
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<id_usuario>") # <> mostra que é uma variável
@login_required
def perfil(id_usuario): # variável é passada como parâmetro
    if int(id_usuario) == int(current_user.id):
        # usuário está vendo o próprio perfil
        return render_template("perfil.html", usuario=current_user)
    else:    
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user() #  desloga o usuário atual
    return redirect(url_for("homepage"))