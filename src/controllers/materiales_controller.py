from src.services.materiales_service import calcular_requerimiento_materiales
from src.services.produccion_service import calcular_presupuesto_produccion
from src.utils.format_utils import format_currency

def mostrar_presupuesto_materiales():
    # Unidades a producir (estas deberían ser calculadas en el presupuesto de producción)
    unidades_a_producir = {
        "CL": [12000, 6500],
        "CE": [13500, 10800],
        "CR": [7000, 7500]
    }

    # Requerimientos de materiales por unidad de producto
    requerimientos_materiales = {
        "CL": {"A": [1.0, 1.0], "B": [0.5, 0.5], "C": [10.0, 10.0]},
        "CE": {"A": [1.2, 1.2], "B": [0.6, 0.6], "C": [25.0, 25.0]},
        "CR": {"A": [2.0, 2.0], "B": [1.0, 1.0], "C": [5.0, 5.0]}
    }

    # Calcular requerimiento de materiales
    presupuesto_materiales = calcular_requerimiento_materiales(unidades_a_producir, requerimientos_materiales)

    # Mostrar resultados
    print("\nPresupuesto de Requerimiento de Materiales".center(60, "-"))
    print(f"{'Producto':<10} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")

    for producto, materiales in presupuesto_materiales.items():
        if producto == "Total Requerimientos":
            continue
        print(f"\n{producto} - Unidades a producir: {unidades_a_producir[producto][0]}, {unidades_a_producir[producto][1]}")
        for material, cantidades in materiales.items():
            print(f"Material {material:<10} {cantidades[0]:>15} {cantidades[1]:>15} {cantidades[2]:>15}")
    
    # Mostrar totales por material
    print("\n" + "-" * 60)
    print(f"{'Total de Requerimientos':<20} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")
    for material, totales in presupuesto_materiales["Total Requerimientos"].items():
        print(f"Material {material:<10} {totales[0]:>15} {totales[1]:>15} {totales[2]:>15}")
