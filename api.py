from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
from textblob import TextBlob  # Importando a biblioteca TextBlob
import sqlite3

# Baixar recursos necessários do NLTK
# from nltk import download
# download('punkt')

app = Flask(__name__)

# Lista para armazenar os custos (temporário)
custos = []


def connect_db():
    """Conecta ao banco de dados SQLite."""
    conn = sqlite3.connect('gerenciamento_ia.db')
    return conn


@app.route('/login', methods=['POST'])
def login():
    """Autentica o usuário."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Aqui você deve verificar as credenciais do usuário
    if username == "admin" and password == "senha":  # Exemplo de verificação
        return jsonify({'message': 'Login bem-sucedido!'}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas!'}), 401


@app.route('/definicao_margem', methods=['POST'])
def definicao_margem():
    """Define a margem de lucro."""
    data = request.json
    margem = data.get('margem')

    return jsonify({'message': 'Margem de lucro definida com sucesso!',
                    'margem': margem}), 201


@app.route('/cadastro_custos', methods=['POST'])
def cadastro_custos():
    """Cadastra os custos recebidos."""
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO custos (material, mao_de_obra, custo_entrega, custo_total)
        VALUES (?, ?, ?, ?)
    ''', (data['material'], data['mao_de_obra'], data['custo_entrega'], data[
        'custo_total']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Custos cadastrados com sucesso!'}), 201


@app.route('/listar_custos', methods=['GET'])
def listar_custos():
    """Lista todos os custos armazenados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM custos')
    rows = cursor.fetchall()
    conn.close()
    # Formatar os dados para retorno
    custos_list = []
    for row in rows:
        custos_list.append({
            'id': row[0],
            'material': row[1],
            'mao_de_obra': row[2],
            'custo_entrega': row[3],
            'custo_total': row[4]
        })
    return jsonify(custos_list), 200


@app.route('/excluir_custo/<int:custo_id>', methods=['DELETE'])
def excluir_custo(custo_id):
    """Remove um custo existente."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM custos WHERE id = ?', (custo_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Custo excluído com sucesso!'}), 200


@app.route('/calculo_preco', methods=['POST'])
def calculo_preco():
    """Calcula o preço de venda com base nos custos e na margem de lucro."""
    data = request.json
    custo_total = data.get('custo_total')
    margem = data.get('margem')
    # Cálculo do preço de venda
    preco_venda = custo_total + (custo_total * (margem / 100))
    return jsonify({'preco_venda': preco_venda}), 201


@app.route('/process_text', methods=['POST'])
def process_text():
    """Processa o texto recebido e retorna os tokens."""
    data = request.json
    print("Dados recebidos:", data)  # Exibe os dados recebidos
    text = data.get('text', '')
    tokens = word_tokenize(text)
    return jsonify({'tokens': tokens}), 200


@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    """Analisa o sentimento do texto recebido."""
    data = request.json
    text = data.get('text', '')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Calcula a polaridade
    return jsonify({'polarity': polarity})


@app.route('/status', methods=['GET'])
def status():
    """Retorna o status do serviço."""
    return jsonify({'status': 'running'})


@app.route('/welcome', methods=['GET'])
def welcome():
    """Retorna uma mensagem de boas-vindas."""
    return jsonify({'message': 'Bem-vindo ao serviço Flask!'})


if __name__ == "__main__":
    app.run(debug=True)
