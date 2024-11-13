from src.services.clientes_service import calcular_saldo_clientes_flujo_entradas
from src.services.ventas_service import calcular_presupuesto_ventas  # Importamos para reutilizar el cálculo de ventas
from src.utils.format_utils import format_currency

def mostrar_saldo_clientes_flujo_entradas():
    # Obtener el total de ventas de 2016 del presupuesto de ventas
    presupuesto_ventas = calcular_presupuesto_ventas()
    ventas_2016 = presupuesto_ventas["Total Anual"]

    # Solicitar saldo inicial y cobros
    saldo_inicial = float(input("Ingrese el saldo de clientes al 31-Dic-2015: "))
    cobranza_2015 = float(input("Ingrese la cobranza del 2015: "))
    cobranza_2016 = float(input("Ingrese la cobranza del 2016: "))

    # Calcular saldo de clientes y flujo de entradas
    resultado = calcular_saldo_clientes_flujo_entradas(saldo_inicial, ventas_2016, cobranza_2015, cobranza_2016)

    # Mostrar resultados
    print("\nDeterminación del Saldo de Clientes y Flujo de Entradas".center(60, "-"))
    print(f"{'Descripción':<30} {'Importe':>15} {'Total':>15}")
    print(f"{'Saldo de clientes 31-Dic-2015':<30} {format_currency(resultado['saldo_inicial']):>15}")
    print(f"{'Ventas 2016':<30} {format_currency(resultado['ventas']):>15}")
    print(f"{'Total de Clientes 2016':<30} {format_currency(resultado['total_clientes']):>15}\n")

    print("Entradas de Efectivo:")
    print(f"{'Por Cobranza del 2015':<30} {format_currency(resultado['cobranza_2015']):>15}")
    print(f"{'Por Cobranza del 2016':<30} {format_currency(resultado['cobranza_2016']):>15}")
    print(f"{'Total Entradas':<30} {format_currency(resultado['total_entradas']):>15}\n")

    print(f"{'Saldo de Clientes del 2016':<30} {format_currency(resultado['saldo_final']):>15}")
