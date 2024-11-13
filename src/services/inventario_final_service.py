def calcular_inventario_final(materiales, productos):
    # Calcular el inventario final de materiales
    inventario_materiales = {}
    total_inventario_materiales = 0
    for nombre, datos in materiales.items():
        costo_total = datos["unidades"] * datos["costo_unitario"]
        inventario_materiales[nombre] = {
            "unidades": datos["unidades"],
            "costo_unitario": datos["costo_unitario"],
            "costo_total": costo_total
        }
        total_inventario_materiales += costo_total

    # Calcular el inventario final de productos terminados
    inventario_productos = {}
    total_inventario_productos = 0
    for nombre, datos in productos.items():
        costo_total = datos["unidades"] * datos["costo_unitario"]
        inventario_productos[nombre] = {
            "unidades": datos["unidades"],
            "costo_unitario": datos["costo_unitario"],
            "costo_total": costo_total
        }
        total_inventario_productos += costo_total

    return {
        "materiales": inventario_materiales,
        "total_inventario_materiales": total_inventario_materiales,
        "productos": inventario_productos,
        "total_inventario_productos": total_inventario_productos
    }
