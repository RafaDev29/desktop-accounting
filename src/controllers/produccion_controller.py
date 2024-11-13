from src.services.produccion_service import calcular_presupuesto_produccion
from src.services.ventas_service import calcular_presupuesto_ventas
from src.utils.format_utils import format_currency

def solicitar_inventario(producto):
    inventario_final = []
    inventario_inicial = []

    for semestre in ["1er. Semestre", "2do. Semestre"]:
        inventario_f = int(input(f"Ingrese el inventario final para {producto} en {semestre}: "))
        inventario_i = int(input(f"Ingrese el inventario inicial para {producto} en {semestre}: "))
        inventario_final.append(inventario_f)
        inventario_inicial.append(inventario_i)

    return inventario_inicial, inventario_final

def mostrar_presupuesto_produccion():
    # Obtener ventas del servicio de ventas
    presupuesto_ventas = calcular_presupuesto_ventas()

    # Extraer las unidades a vender de cada producto
    ventas = {
        "CL": {"unidades": presupuesto_ventas["CL"][:2]},
        "CE": {"unidades": presupuesto_ventas["CE"][:2]},
        "CR": {"unidades": presupuesto_ventas["CR"][:2]},
    }

    # Solicitar inventarios
    inventario_inicial = {}
    inventario_final = {}

    for producto in ["CL", "CE", "CR"]:
        inventario_i, inventario_f = solicitar_inventario(producto)
        inventario_inicial[producto] = inventario_i
        inventario_final[producto] = inventario_f

    # Calcular presupuesto de producción
    presupuesto_produccion = calcular_presupuesto_produccion(ventas, inventario_inicial, inventario_final)

    # Mostrar resultados
    print("\nPresupuesto de Producción".center(60, "-"))
    print(f"{'Producto':<10} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")

    for producto, datos in presupuesto_produccion.items():
        print(f"{producto} - Unidades a Producir")
        print(f"{'Unidades a Vender':<20} {datos['unidades_vender'][0]:>10} {datos['unidades_vender'][1]:>10}")
        print(f"{'Inventario Final':<20} {datos['inventario_final'][0]:>10} {datos['inventario_final'][1]:>10}")
        print(f"{'Total de Unidades':<20} {datos['total_unidades'][0]:>10} {datos['total_unidades'][1]:>10}")
        print(f"{'Inventario Inicial':<20} {datos['inventario_inicial'][0]:>10} {datos['inventario_inicial'][1]:>10}")
        print(f"{'Unidades a Producir':<20} {datos['unidades_producir'][0]:>10} {datos['unidades_producir'][1]:>10} {datos['total_anual']:>10}")
        print("-" * 60)
