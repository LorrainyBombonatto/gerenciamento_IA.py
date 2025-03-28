def calcular_custos_projetos(custos):
    """
    Calcula custos de projetos.
    :param custos: Lista de custos do projeto
    :return: Total de custos do projeto
    """
    return sum(custos)


def analise_viabilidade(custos, receita_esperada):
    """
    Análise de viabilidade de projetos.
    :param custos: Lista de custos do projeto
    :param receita_esperada: Receita esperada do projeto
    :return: Dicionário com análise de viabilidade
    """
    total_custos = sum(custos)
    viabilidade = receita_esperada >= total_custos
    return {
        'total_custos': total_custos,
        'viabilidade': viabilidade
    }
