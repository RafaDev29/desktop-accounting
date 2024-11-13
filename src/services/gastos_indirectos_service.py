def calcular_gastos_indirectos_fabricacion(gastos, total_horas_mod_anual):
    # Calcular el total de GIF por semestre
    total_gif_por_semestre = [sum(gastos[categoria][i] for categoria in gastos) for i in range(2)]
    total_gif_anual = sum(total_gif_por_semestre)

    # Cálculo del costo por hora de GIF
    costo_por_hora_gif = total_gif_anual / total_horas_mod_anual

    return {
        "gastos": gastos,
        "total_gif_por_semestre": total_gif_por_semestre,
        "total_gif_anual": total_gif_anual,
        "costo_por_hora_gif": costo_por_hora_gif
    }
