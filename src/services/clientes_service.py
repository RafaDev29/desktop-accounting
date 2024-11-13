def calcular_saldo_clientes_flujo_entradas(saldo_inicial, ventas, cobranza_2015, cobranza_2016):
    total_clientes = saldo_inicial + ventas
    total_entradas = cobranza_2015 + cobranza_2016
    saldo_final = total_clientes - total_entradas
    return {
        "saldo_inicial": saldo_inicial,
        "ventas": ventas,
        "total_clientes": total_clientes,
        "cobranza_2015": cobranza_2015,
        "cobranza_2016": cobranza_2016,
        "total_entradas": total_entradas,
        "saldo_final": saldo_final
    }
