import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob  # Importando a biblioteca TextBlob


# Baixar recursos necessários do NLTK
nltk.download('punkt')  # Adicionando o download do recurso punkt_tab
nltk.download('punkt')


# nltk.download('punkt_tab')  # Adicionando o download do recurso punkt_tab
def analyze_sentiment(text):  # Nova função para análise de sentimentos
    """
    Analisa o sentimento do texto e retorna a polaridade.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Retorna a polaridade do sentimento


def process_text(text):
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """

    """
    Processa o texto de entrada e retorna uma lista de palavras tokenizadas.
    """
    tokens = word_tokenize(text)
    return tokens  # Retorna a lista de palavras tokenizadas


# Exemplo de uso da função process_text
if __name__ == "__main__":
    sample_text = "Olá! Como posso ajudar você hoje?"
tokens = process_text(sample_text)
print("Palavras tokenizadas:", tokens)
