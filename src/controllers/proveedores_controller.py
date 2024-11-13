from src.services.proveedores_service import calcular_saldo_proveedores
from src.utils.format_utils import format_currency

def mostrar_saldo_proveedores():
    # Datos necesarios
    saldo_inicial = 33500  # Saldo de Proveedores al 31-Dic-2015
    compras = 2141010      # Compras totales para 2016 (del presupuesto de compras)
    pago_2015 = 33500      # Pago de Proveedores del 2015 (100%)
    pago_2016_porcentaje = 0.5  # 50% de las compras de 2016

    # Calcular saldo de proveedores y flujo de salidas
    resultado = calcular_saldo_proveedores(saldo_inicial, compras, pago_2015, pago_2016_porcentaje)

    # Mostrar resultados
    print("\nDeterminación del saldo de Proveedores y Flujo de Salidas".center(60, "-"))
    print(f"{'Descripción':<30} {'Importe':>15} {'Total':>15}")
    print(f"{'Saldo de Proveedores 31-Dic-2015':<30} {format_currency(resultado['saldo_inicial']):>15}")
    print(f"{'Compras 2016':<30} {format_currency(resultado['compras']):>15}")
    print(f"{'Total de Proveedores 2016':<30} {format_currency(resultado['total_proveedores_2016']):>15}\n")

    print("Salidas de Efectivo:")
    print(f"{'Por Proveedores del 2015':<30} {format_currency(resultado['pago_2015']):>15}")
    print(f"{'Por Proveedores del 2016':<30} {format_currency(resultado['pago_2016']):>15}")
    print(f"{'Total de Salidas 2016':<30} {format_currency(resultado['total_salidas']):>15}\n")

    print(f"{'Saldo de Proveedores del 2016':<30} {format_currency(resultado['saldo_final']):>15}")
