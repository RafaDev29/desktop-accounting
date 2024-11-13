from src.services.gastos_indirectos_service import calcular_gastos_indirectos_fabricacion
from src.utils.format_utils import format_currency

def solicitar_gastos_indirectos():
    gastos = {}
    categorias = ["Depreciación", "Seguros", "Mantenimiento", "Energéticos", "Varios"]
    
    for categoria in categorias:
        gasto_1er_semestre = float(input(f"Ingrese el gasto de {categoria} para el 1er. Semestre: "))
        gasto_2do_semestre = float(input(f"Ingrese el gasto de {categoria} para el 2do. Semestre: "))
        gastos[categoria] = [gasto_1er_semestre, gasto_2do_semestre]

    return gastos

def mostrar_presupuesto_gastos_indirectos():
    # Solicitar datos de gastos indirectos
    gastos = solicitar_gastos_indirectos()

    # Ingresar el total de horas de MOD anual (del cálculo anterior de MOD)
    total_horas_mod_anual = float(input("Ingrese el total de horas M.O.D. anual: "))

    # Calcular el presupuesto de GIF
    presupuesto_gif = calcular_gastos_indirectos_fabricacion(gastos, total_horas_mod_anual)

    # Mostrar resultados
    print("\nPresupuesto de Gastos Indirectos de Fabricación".center(60, "-"))
    print(f"{'Descripción':<20} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")
    for categoria, valores in presupuesto_gif["gastos"].items():
        print(f"{categoria:<20} {format_currency(valores[0]):>15} {format_currency(valores[1]):>15} {format_currency(sum(valores)):>15}")
    
    print("\n" + "-" * 60)
    print(f"{'Total G.I.F. por semestre':<20} {format_currency(presupuesto_gif['total_gif_por_semestre'][0]):>15} {format_currency(presupuesto_gif['total_gif_por_semestre'][1]):>15} {format_currency(presupuesto_gif['total_gif_anual']):>15}")
    print(f"\n{'Coeficiente para determinar el costo por hora de GIF':<50}")
    print(f"{'Total de G.I.F.':<35} {format_currency(presupuesto_gif['total_gif_anual']):>15}")
    print(f"{'Total horas M.O.D. Anual':<35} {total_horas_mod_anual:>15,.2f}")
    print(f"{'= Costo por Hora de G.I.F.':<35} {format_currency(presupuesto_gif['costo_por_hora_gif']):>15}")
