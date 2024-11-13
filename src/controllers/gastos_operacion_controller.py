from src.services.gastos_operacion_service import calcular_gastos_operacion
from src.utils.format_utils import format_currency

def solicitar_gastos_operacion():
    gastos = {}
    categorias = ["Depreciación", "Sueldos y Salarios", "Varios", "Intereses del Préstamo"]
    
    for categoria in categorias:
        gasto_1er_semestre = float(input(f"Ingrese el gasto de {categoria} para el 1er. Semestre: "))
        gasto_2do_semestre = float(input(f"Ingrese el gasto de {categoria} para el 2do. Semestre: "))
        gastos[categoria] = [gasto_1er_semestre, gasto_2do_semestre]

    # Solicitar las ventas proyectadas para calcular las comisiones
    ventas_1er_semestre = float(input("Ingrese las ventas proyectadas para el 1er. Semestre: "))
    ventas_2do_semestre = float(input("Ingrese las ventas proyectadas para el 2do. Semestre: "))
    comisiones = [ventas_1er_semestre * 0.01, ventas_2do_semestre * 0.01]
    
    gastos["Comisiones"] = comisiones

    return gastos

def mostrar_presupuesto_gastos_operacion():
    # Solicitar datos de gastos de operación
    gastos = solicitar_gastos_operacion()

    # Calcular el presupuesto de gastos de operación
    presupuesto_gastos = calcular_gastos_operacion(gastos)

    # Mostrar resultados
    print("\nPresupuesto de Gastos de Operación".center(60, "-"))
    print(f"{'Descripción':<20} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")
    for categoria, valores in presupuesto_gastos["gastos"].items():
        print(f"{categoria:<20} {format_currency(valores[0]):>15} {format_currency(valores[1]):>15} {format_currency(sum(valores)):>15}")
    
    print("\n" + "-" * 60)
    print(f"{'Total de Gastos de Operación':<20} {format_currency(presupuesto_gastos['total_gastos_por_semestre'][0]):>15} {format_currency(presupuesto_gastos['total_gastos_por_semestre'][1]):>15} {format_currency(presupuesto_gastos['total_gastos_anual']):>15}")
