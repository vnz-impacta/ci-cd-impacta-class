from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá mundo! Essa aplicação está em atualização por Vinicius Nunes Zorzetti."