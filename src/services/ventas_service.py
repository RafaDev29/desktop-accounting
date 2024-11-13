presupuesto_cache = None  # Variable para almacenar el resultado del cálculo

def calcular_presupuesto_ventas(productos=None):
    global presupuesto_cache
    if presupuesto_cache is not None and productos is None:
        return presupuesto_cache  # Usar el resultado almacenado si ya existe

    if productos is None:
        raise ValueError("Debe proporcionar datos de productos para calcular el presupuesto de ventas")

    total_por_semestre = [0, 0]
    resultado = {}

    for producto, datos in productos.items():
        importes = []
        for i in range(2):
            importe = datos["unidades"][i] * datos["precio"][i]
            importes.append(importe)
            total_por_semestre[i] += importe
        
        resultado[producto] = importes
        resultado[producto].append(sum(importes))  # Total anual para el producto
    
    resultado["Total Semestre"] = total_por_semestre
    resultado["Total Anual"] = sum(total_por_semestre)

    presupuesto_cache = resultado  # Almacenar el resultado en cache
    return resultado
