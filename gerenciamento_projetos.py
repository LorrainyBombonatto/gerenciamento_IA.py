from flask import Blueprint, request, jsonify
import pandas as pd  # type: ignore

# Criar um Blueprint para gerenciamento de projetos
projetos_bp = Blueprint("projetos", __name__)

# DataFrame para armazenar projetos
projetos_df = pd.DataFrame(columns=["id", "nome", "descricao", "status"])


@projetos_bp.route("/projetos", methods=["POST"])
def adicionar_projeto():
    data = request.json
    novo_projeto = {
        "id": len(projetos_df) + 1,
        "nome": data["nome"],
        "descricao": data["descricao"],
        "status": "ativo",
    }
    global projetos_df
    projetos_df = projetos_df.append(novo_projeto, ignore_index=True)
    return jsonify(novo_projeto), 201


@projetos_bp.route("/projetos", methods=["GET"])
def listar_projetos():
    return jsonify(projetos_df.to_dict(orient="records"))


@projetos_bp.route("/projetos/<int:projeto_id>", methods=["PUT"])
def atualizar_projeto(projeto_id):
    data = request.json
    global projetos_df

    if projeto_id <= len(projetos_df):
        projetos_df.at[projeto_id - 1, "nome"] = data.get(
            "nome", projetos_df.at[projeto_id - 1, "nome"]
        )
        projetos_df.at[projeto_id - 1, "descricao"] = data.get(
            "descricao", projetos_df.at[projeto_id - 1, "descricao"]
        )
        return jsonify(projetos_df.iloc[projeto_id - 1].to_dict()), 200

    return jsonify({"error": "Projeto não encontrado"}), 404
