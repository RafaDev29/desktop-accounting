def calcular_importe_venta(unidades, precio):
    return unidades * precio

def calcular_presupuesto_ventas(productos):
    total_por_semestre = [0, 0]
    resultado = {}

    for producto, datos in productos.items():
        importes = []
        for i in range(2):
            importe = calcular_importe_venta(datos["unidades"][i], datos["precio"][i])
            importes.append(importe)
            total_por_semestre[i] += importe
        
        resultado[producto] = importes
        resultado[producto].append(sum(importes))  # Total anual para el producto
    
    resultado["Total Semestre"] = total_por_semestre
    resultado["Total Anual"] = sum(total_por_semestre)

    return resultado
