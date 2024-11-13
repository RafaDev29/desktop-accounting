from src.services.compras_service import calcular_presupuesto_compras
from src.utils.format_utils import format_currency

def mostrar_presupuesto_compras():
    # Datos de ejemplo: requerimientos de materiales y precios de compra
    requerimientos = {
        "A": [42200, 34460],
        "B": [21100, 17230],
        "C": [492500, 372500]
    }
    inventario_final = {
        "A": [5000, 3000],
        "B": [3000, 2500],
        "C": [2000, 1800]
    }
    inventario_inicial = {
        "A": [5000, 5000],
        "B": [3000, 3000],
        "C": [2000, 2000]
    }
    precios_compra = {
        "A": [10.00, 12.00],
        "B": [2.00, 3.00],
        "C": [1.00, 2.00]
    }

    # Calcular presupuesto de compras
    presupuesto_compras = calcular_presupuesto_compras(requerimientos, inventario_inicial, inventario_final, precios_compra)

    # Mostrar resultados
    print("\nPresupuesto de Compra de Materiales".center(60, "-"))
    print(f"{'Material':<10} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")

    for material, datos in presupuesto_compras.items():
        if material == "Total Compras":
            continue
        print(f"\nMaterial {material}")
        print(f"{'Requerimiento':<20} {datos['requerimiento'][0]:>10} {datos['requerimiento'][1]:>10}")
        print(f"{'Inventario Final':<20} {datos['inventario_final'][0]:>10} {datos['inventario_final'][1]:>10}")
        print(f"{'Total de Materiales':<20} {datos['total_materiales'][0]:>10} {datos['total_materiales'][1]:>10}")
        print(f"{'Inventario Inicial':<20} {datos['inventario_inicial'][0]:>10} {datos['inventario_inicial'][1]:>10}")
        print(f"{'Material a Comprar':<20} {datos['compras'][0]:>10} {datos['compras'][1]:>10}")
        print(f"{'Precio de Compra':<20} ${datos['precio'][0]:>8} ${datos['precio'][1]:>8}")
        print(f"{'Total en $':<20} {format_currency(datos['costo_semestre'][0]):>10} {format_currency(datos['costo_semestre'][1]):>10} {format_currency(datos['total_costo']):>10}")
    
    # Mostrar total de compras
    print("\n" + "-" * 60)
    print(f"{'Total de Compras':<20} {format_currency(presupuesto_compras['Total Compras'][0]):>15} {format_currency(presupuesto_compras['Total Compras'][1]):>15} {format_currency(presupuesto_compras['Total Compras'][2]):>15}")
