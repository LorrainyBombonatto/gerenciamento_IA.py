def calcular_kpis(vendas, custos):
    """
    Calcula indicadores de desempenho (KPIs).
    :param vendas: Total de vendas
    :param custos: Total de custos
    :return: Dicionário com KPIs
    """
    lucro = vendas - custos
    margem_lucro = (lucro / vendas) * 100 if vendas > 0 else 0
    return {
        'lucro': lucro,
        'margem_lucro': margem_lucro
    }


def gerar_relatorios_vendas(vendas):
    """
    Gera relatórios de vendas.
    :param vendas: Lista de vendas
    :return: Dicionário com total de vendas
    """
    total_vendas = sum(vendas)
    return {
        'total_vendas': total_vendas,
        'numero_vendas': len(vendas)
    }
