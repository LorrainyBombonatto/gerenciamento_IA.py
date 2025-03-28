def criar_orcamento(nome, valor):
    """
    Cria um orçamento.
    :param nome: Nome do orçamento
    :param valor: Valor do orçamento
    :return: Dicionário com informações do orçamento
    """
    return {
        'nome': nome,
        'valor': valor,
        'gasto': 0
    }


def monitorar_orcamento(orçamento, gasto):
    """
    Monitora o orçamento.
    :param orçamento: Dicionário do orçamento
    :param gasto: Valor gasto
    :return: Dicionário atualizado do orçamento
    """
    orçamento['gasto'] += gasto
    return orçamento


def comparar_orcamentos(orçamento_planejado, orçamento_real):
    """
    Compara orçamentos planejados e reais.
    :param orçamento_planejado: Dicionário do orçamento planejado
    :param orçamento_real: Dicionário do orçamento real
    :return: Dicionário com comparação
    """
    return {
        'diferença': orçamento_planejado['valor'] - orçamento_real['gasto']
    }
