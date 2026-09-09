from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/validacao", methods=["GET", "POST"])
def validacao():

    resultado = None

    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        idade = int(request.form["idade"])

        if idade >= 18:
            votar = "Pode votar"
            dirigir = "Pode dirigir"
        elif idade >= 16:
            votar = "Pode votar"
            dirigir = "Não pode dirigir"
        else:
            votar = "Não pode votar"
            dirigir = "Não pode dirigir"

        resultado = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "votar": votar,
            "dirigir": dirigir
        }

    return render_template("validacao.html", resultado=resultado)


app.run(debug=True)