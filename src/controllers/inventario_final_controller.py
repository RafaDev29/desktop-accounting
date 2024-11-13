from src.services.inventario_final_service import calcular_inventario_final
from src.utils.format_utils import format_currency

def solicitar_datos_inventario_materiales():
    materiales = {}
    categorias = ["Material A", "Material B", "Material C"]
    
    for categoria in categorias:
        unidades = int(input(f"Ingrese las unidades de {categoria}: "))
        costo_unitario = float(input(f"Ingrese el costo unitario de {categoria}: "))
        materiales[categoria] = {"unidades": unidades, "costo_unitario": costo_unitario}

    return materiales

def solicitar_datos_inventario_productos():
    productos = {}
    categorias = ["Producto CL", "Producto CE", "Producto CR"]

    for categoria in categorias:
        unidades = int(input(f"Ingrese las unidades de {categoria}: "))
        costo_unitario = float(input(f"Ingrese el costo unitario de {categoria}: "))
        productos[categoria] = {"unidades": unidades, "costo_unitario": costo_unitario}

    return productos

def mostrar_inventario_final():
    # Solicitar datos de inventario de materiales
    materiales = solicitar_datos_inventario_materiales()

    # Solicitar datos de inventario de productos terminados
    productos = solicitar_datos_inventario_productos()

    # Calcular el inventario final
    inventario_final = calcular_inventario_final(materiales, productos)

    # Mostrar resultados
    print("\nInventario Final de Materiales".center(60, "-"))
    print(f"{'Descripción':<20} {'Unidades':>10} {'Costo Unitario':>15} {'Costo Total':>15}")
    for nombre, datos in inventario_final["materiales"].items():
        print(f"{nombre:<20} {datos['unidades']:>10} {format_currency(datos['costo_unitario']):>15} {format_currency(datos['costo_total']):>15}")
    
    print(f"\n{'Inventario Final de Materiales':<50} {format_currency(inventario_final['total_inventario_materiales']):>15}")
    
    print("\nInventario Final de Producto Terminado".center(60, "-"))
    print(f"{'Descripción':<20} {'Unidades':>10} {'Costo Unitario':>15} {'Costo Total':>15}")
    for nombre, datos in inventario_final["productos"].items():
        print(f"{nombre:<20} {datos['unidades']:>10} {format_currency(datos['costo_unitario']):>15} {format_currency(datos['costo_total']):>15}")
    
    print(f"\n{'Inventario Final de Producto Terminado':<50} {format_currency(inventario_final['total_inventario_productos']):>15}")
