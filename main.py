# Código do Gerenciamento de Projetos
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return "Bem-vindo ao Gerenciamento de Projetos!"


@app.route("/api/projetos", methods=["GET"])
def get_projetos():
    """
    Retorna a lista de projetos.
    """
    projetos = [
        {
            "id": 1,
            "nome": "Projeto A",
            "data_inicio": datetime(2023, 1, 1).isoformat(),
            "data_fim": datetime(2023, 12, 31).isoformat(),
        },
        {
            "id": 2,
            "nome": "Projeto B",
            "data_inicio": datetime(2023, 2, 1).isoformat(),
            "data_fim": datetime(2023, 11, 30).isoformat(),
        },
    ]
    return jsonify(projetos)


if __name__ == "__main__":

    app.run(debug=True)
