from src.services.costo_unitario_service import calcular_costo_unitario
from src.utils.format_utils import format_currency

def solicitar_datos_producto(producto):
    materiales = {}
    categorias = ["Material A", "Material B", "Material C"]
    
    for categoria in categorias:
        costo = float(input(f"Ingrese el costo de {categoria} para {producto}: "))
        cantidad = float(input(f"Ingrese la cantidad de {categoria} para {producto}: "))
        materiales[categoria] = {"costo": costo, "cantidad": cantidad}

    mano_obra = {
        "costo": float(input(f"Ingrese el costo de Mano de Obra para {producto}: ")),
        "cantidad": float(input(f"Ingrese la cantidad de Mano de Obra para {producto}: "))
    }

    gif = {
        "costo": float(input(f"Ingrese el costo de Gastos Indirectos de Fabricación (GIF) para {producto}: ")),
        "cantidad": float(input(f"Ingrese la cantidad de GIF para {producto}: "))
    }

    return materiales, mano_obra, gif

def mostrar_costo_unitario_producto():
    productos = ["CL", "CE", "CR"]

    for producto in productos:
        print(f"\nCalculando Costo Unitario para el Producto {producto}")
        materiales, mano_obra, gif = solicitar_datos_producto(producto)

        # Calcular el costo unitario
        costo_unitario = calcular_costo_unitario(materiales, mano_obra, gif)

        # Mostrar resultados
        print(f"\nCosto Unitario del Producto {producto}".center(50, "-"))
        print(f"{'Descripción':<30} {'Costo':>10} {'Cantidad':>10} {'Costo Unitario':>15}")
        
        for nombre, material in materiales.items():
            costo = material["costo"]
            cantidad = material["cantidad"]
            costo_unitario_material = costo * cantidad
            print(f"{nombre:<30} {format_currency(costo):>10} {cantidad:>10,.2f} {format_currency(costo_unitario_material):>15}")

        print(f"{'Mano de Obra':<30} {format_currency(mano_obra['costo']):>10} {mano_obra['cantidad']:>10,.2f} {format_currency(costo_unitario['costo_unitario_mano_obra']):>15}")
        print(f"{'Gastos Indirectos de Fabricación':<30} {format_currency(gif['costo']):>10} {gif['cantidad']:>10,.2f} {format_currency(costo_unitario['costo_unitario_gif']):>15}")
        print(f"\n{'Costo Unitario Total':<50} {format_currency(costo_unitario['costo_unitario_total']):>15}")
