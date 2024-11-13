def calcular_saldo_proveedores(saldo_inicial, compras, pago_2015, pago_2016_porcentaje):
    # Total de proveedores para 2016
    total_proveedores_2016 = saldo_inicial + compras

    # Cálculo de salidas de efectivo
    pago_2016 = compras * pago_2016_porcentaje
    total_salidas = pago_2015 + pago_2016

    # Saldo final de proveedores
    saldo_final = total_proveedores_2016 - total_salidas

    return {
        "saldo_inicial": saldo_inicial,
        "compras": compras,
        "total_proveedores_2016": total_proveedores_2016,
        "pago_2015": pago_2015,
        "pago_2016": pago_2016,
        "total_salidas": total_salidas,
        "saldo_final": saldo_final
    }
