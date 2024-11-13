def calcular_gastos_operacion(gastos):
    # Calcular el total de gastos por semestre
    total_gastos_por_semestre = [sum(gastos[categoria][i] for categoria in gastos) for i in range(2)]
    total_gastos_anual = sum(total_gastos_por_semestre)

    return {
        "gastos": gastos,
        "total_gastos_por_semestre": total_gastos_por_semestre,
        "total_gastos_anual": total_gastos_anual
    }
