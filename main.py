from flask import Flask, render_template, url_for

# url_for permite acessar o endpoint pelo nome da função

app = Flask(__name__)

@app.route("/") # caminho com link do site
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") # <> mostra que é uma variável
def perfil(usuario): # variável é passada como parâmetro
    return render_template("perfil.html", usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)