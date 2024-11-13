def calcular_presupuesto_mano_obra(unidades_producir, horas_por_unidad, cuota_por_hora):
    resultado = {}

    for producto, unidades in unidades_producir.items():
        horas_requeridas = [unidades[i] * horas_por_unidad[producto][i] for i in range(2)]
        total_horas = sum(horas_requeridas)
        importe_mod = [horas_requeridas[i] * cuota_por_hora[producto][i] for i in range(2)]
        total_importe = sum(importe_mod)

        resultado[producto] = {
            "unidades_producir": unidades,
            "horas_requeridas": horas_requeridas,
            "total_horas": total_horas,
            "cuota_por_hora": cuota_por_hora[producto],
            "importe_mod": importe_mod,
            "total_importe": total_importe
        }

    # Calcular el total de horas y MOD por semestre y anual
    total_horas_semestre = [sum([resultado[p]["horas_requeridas"][i] for p in resultado]) for i in range(2)]
    total_horas_anual = sum(total_horas_semestre)
    total_mod_semestre = [sum([resultado[p]["importe_mod"][i] for p in resultado]) for i in range(2)]
    total_mod_anual = sum(total_mod_semestre)

    resultado["Total Horas"] = total_horas_semestre + [total_horas_anual]
    resultado["Total MOD"] = total_mod_semestre + [total_mod_anual]

    return resultado
