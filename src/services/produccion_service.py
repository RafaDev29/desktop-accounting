def calcular_presupuesto_produccion(ventas, inventario_inicial, inventario_final):
    resultado = {}

    for producto, datos in ventas.items():
        unidades_vender = datos["unidades"]
        unidades_producir = []

        for i in range(2):
            total_unidades = unidades_vender[i] + inventario_final[producto][i]
            producir = total_unidades - inventario_inicial[producto][i]
            unidades_producir.append(producir)

        resultado[producto] = {
            "unidades_vender": unidades_vender,
            "inventario_final": inventario_final[producto],
            "total_unidades": [unidades_vender[i] + inventario_final[producto][i] for i in range(2)],
            "inventario_inicial": inventario_inicial[producto],
            "unidades_producir": unidades_producir,
            "total_anual": sum(unidades_producir)
        }

    return resultado
