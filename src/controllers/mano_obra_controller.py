from src.services.mano_obra_service import calcular_presupuesto_mano_obra
from src.utils.format_utils import format_currency

def solicitar_datos_mano_obra(producto):
    unidades_producir = []
    horas_por_unidad = []
    cuota_por_hora = []

    for semestre in ["1er. Semestre", "2do. Semestre"]:
        unidades = int(input(f"Ingrese las unidades a producir para {producto} en {semestre}: "))
        horas = float(input(f"Ingrese las horas requeridas por unidad para {producto} en {semestre}: "))
        cuota = float(input(f"Ingrese la cuota por hora para {producto} en {semestre}: "))

        unidades_producir.append(unidades)
        horas_por_unidad.append(horas)
        cuota_por_hora.append(cuota)

    return unidades_producir, horas_por_unidad, cuota_por_hora

def mostrar_presupuesto_mano_obra():
    # Solicitar datos para cada producto
    productos = ["CL", "CE", "CR"]
    unidades_producir = {}
    horas_por_unidad = {}
    cuota_por_hora = {}

    for producto in productos:
        unidades, horas, cuota = solicitar_datos_mano_obra(producto)
        unidades_producir[producto] = unidades
        horas_por_unidad[producto] = horas
        cuota_por_hora[producto] = cuota

    # Calcular presupuesto de mano de obra directa
    presupuesto_mano_obra = calcular_presupuesto_mano_obra(unidades_producir, horas_por_unidad, cuota_por_hora)

    # Mostrar resultados
    print("\nPresupuesto de Mano de Obra Directa".center(60, "-"))
    print(f"{'Producto':<10} {'1er. Semestre':>15} {'2do. Semestre':>15} {'Total Anual':>15}")

    for producto, datos in presupuesto_mano_obra.items():
        if producto in ["Total Horas", "Total MOD"]:
            continue
        print(f"\n{producto}")
        print(f"{'Unidades a producir':<20} {datos['unidades_producir'][0]:>10} {datos['unidades_producir'][1]:>10}")
        print(f"{'Horas requeridas':<20} {datos['horas_requeridas'][0]:>10} {datos['horas_requeridas'][1]:>10} {datos['total_horas']:>10}")
        print(f"{'Cuota por hora':<20} ${datos['cuota_por_hora'][0]:>8} ${datos['cuota_por_hora'][1]:>8}")
        print(f"{'Importe de M.O.D.':<20} {format_currency(datos['importe_mod'][0]):>10} {format_currency(datos['importe_mod'][1]):>10} {format_currency(datos['total_importe']):>10}")
    
    # Mostrar totales
    print("\n" + "-" * 60)
    print(f"{'Total de horas requeridas por semestre':<35} {presupuesto_mano_obra['Total Horas'][0]:>10} {presupuesto_mano_obra['Total Horas'][1]:>10} {presupuesto_mano_obra['Total Horas'][2]:>10}")
    print(f"{'Total de M.O.D. por semestre':<35} {format_currency(presupuesto_mano_obra['Total MOD'][0]):>10} {format_currency(presupuesto_mano_obra['Total MOD'][1]):>10} {format_currency(presupuesto_mano_obra['Total MOD'][2]):>10}")
