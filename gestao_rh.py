def calcular_folha_pagamento(salarios):
    """
    Calcula a folha de pagamento.
    :param salarios: Lista de salários
    :return: Total da folha de pagamento
    """
    return sum(salarios)


def gestao_beneficios(beneficios):
    """
    Gestão de benefícios e encargos.
    :param beneficios: Dicionário com benefícios
    :return: Dicionário com total de benefícios
    """
    total_beneficios = sum(beneficios.values())
    return {
        'total_beneficios': total_beneficios,
        'detalhes': beneficios
    }
