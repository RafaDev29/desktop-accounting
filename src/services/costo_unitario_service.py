def calcular_costo_unitario(materiales, mano_obra, gif):
    # Calcular el costo unitario de cada material
    costo_unitario_materiales = sum(material["costo"] * material["cantidad"] for material in materiales.values())
    costo_unitario_mano_obra = mano_obra["costo"] * mano_obra["cantidad"]
    costo_unitario_gif = gif["costo"] * gif["cantidad"]

    # Costo total unitario
    costo_unitario_total = costo_unitario_materiales + costo_unitario_mano_obra + costo_unitario_gif

    return {
        "costo_unitario_materiales": costo_unitario_materiales,
        "costo_unitario_mano_obra": costo_unitario_mano_obra,
        "costo_unitario_gif": costo_unitario_gif,
        "costo_unitario_total": costo_unitario_total
    }
