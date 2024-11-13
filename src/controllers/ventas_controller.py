from src.services.ventas_service import calcular_presupuesto_ventas
from src.utils.format_utils import format_currency

def solicitar_datos_producto(nombre_producto):
    print(f"\nIngresando datos para el producto {nombre_producto}")
    unidades = []
    precios = []
    for semestre in ["1er. Semestre", "2do. Semestre"]:
        unidad = int(input(f"Ingrese las unidades a vender en {semestre} para {nombre_producto}: "))
        precio = float(input(f"Ingrese el precio de venta en {semestre} para {nombre_producto}: "))
        unidades.append(unidad)
        precios.append(precio)
    return {"unidades": unidades, "precio": precios}

def mostrar_presupuesto_ventas():
    productos = {}
    for producto in ["CL", "CE", "CR"]:
        productos[producto] = solicitar_datos_producto(producto)
    
    presupuesto = calcular_presupuesto_ventas(productos)
    
    print("\nPresupuesto de Ventas".center(50, "-"))
    print(f"{'Producto':<10} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")
    
    for producto, importes in presupuesto.items():
        if producto.startswith("Total"):
            continue  # Saltar totales para mostrarlos al final
        print(f"{producto:<10} {format_currency(importes[0]):>15} {format_currency(importes[1]):>15} {format_currency(importes[2]):>15}")
    
    # Mostrar totales
    print("-" * 50)
    print(f"{'Total Semestre':<10} {format_currency(presupuesto['Total Semestre'][0]):>15} {format_currency(presupuesto['Total Semestre'][1]):>15}")
    print(f"{'Total Anual':<10} {format_currency(presupuesto['Total Anual']):>15}")
