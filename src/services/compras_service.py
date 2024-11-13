def calcular_presupuesto_compras(requerimientos, inventario_inicial, inventario_final, precios_compra):
    resultado = {}

    for material, req_material in requerimientos.items():
        total_materiales = [
            req_material[0] + inventario_final[material][0] - inventario_inicial[material][0],
            req_material[1] + inventario_final[material][1] - inventario_inicial[material][1]
        ]
        compras = total_materiales
        total_anual = sum(compras)
        costo_semestre = [compras[i] * precios_compra[material][i] for i in range(2)]
        total_costo = sum(costo_semestre)

        resultado[material] = {
            "requerimiento": req_material,
            "inventario_final": inventario_final[material],
            "total_materiales": total_materiales,
            "inventario_inicial": inventario_inicial[material],
            "compras": compras,
            "precio": precios_compra[material],
            "costo_semestre": costo_semestre,
            "total_costo": total_costo
        }

    # Calcular el total de compras por semestre y anual
    total_compras = [sum([resultado[m]["costo_semestre"][i] for m in resultado]) for i in range(2)]
    total_compras_anual = sum(total_compras)
    resultado["Total Compras"] = total_compras + [total_compras_anual]

    return resultado
