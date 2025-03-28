def calcular_fluxo_caixa(receitas, despesas):
    """
    Calcula o fluxo de caixa.
    :param receitas: Lista de receitas
    :param despesas: Lista de despesas
    :return: Fluxo de caixa total
    """
    return sum(receitas) - sum(despesas)


def analise_custos_despesas(custos, despesas):
    """
    Analisa custos e despesas.
    :param custos: Lista de custos
    :param despesas: Lista de despesas
    :return: Dicionário com total de custos e despesas
    """
    return {
        'total_custos': sum(custos),
        'total_despesas': sum(despesas)
    }


def gerar_relatorios_financeiros(fluxo_caixa, analise):
    """
    Gera relatórios financeiros.
    :param fluxo_caixa: Fluxo de caixa total
    :param analise: Análise de custos e despesas
    :return: Relatório financeiro
    """
    return {
        'fluxo_caixa': fluxo_caixa,
        'analise': analise
    }
