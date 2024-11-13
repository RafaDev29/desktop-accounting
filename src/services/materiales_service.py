def calcular_requerimiento_materiales(unidades_a_producir, requerimientos_materiales):
    resultado = {}

    for producto, unidades in unidades_a_producir.items():
        material_requerido = {}
        for material, requerimiento in requerimientos_materiales[producto].items():
            total_material = [unidades[i] * requerimiento[i] for i in range(2)]
            total_anual = sum(total_material)
            material_requerido[material] = total_material + [total_anual]

        resultado[producto] = material_requerido

    # Sumar totales de materiales
    total_materiales = {material: [0, 0, 0] for material in ["A", "B", "C"]}
    for producto, materiales in resultado.items():
        for material, cantidades in materiales.items():
            total_materiales[material][0] += cantidades[0]
            total_materiales[material][1] += cantidades[1]
            total_materiales[material][2] += cantidades[2]

    resultado["Total Requerimientos"] = total_materiales
    return resultado
