from src.controllers.ventas_controller import mostrar_presupuesto_ventas
from src.controllers.clientes_controller import mostrar_saldo_clientes_flujo_entradas
from src.controllers.produccion_controller import mostrar_presupuesto_produccion
from src.controllers.materiales_controller import mostrar_presupuesto_materiales
from src.controllers.compras_controller import mostrar_presupuesto_compras

if __name__ == "__main__":
    print("Calculando Presupuesto de Ventas...")
    mostrar_presupuesto_ventas()

    print("\nCalculando Saldo de Clientes y Flujo de Entradas...")
    mostrar_saldo_clientes_flujo_entradas()

    print("\nCalculando Presupuesto de Producción...")
    mostrar_presupuesto_produccion()

    print("\nCalculando Presupuesto de Requerimiento de Materiales...")
    mostrar_presupuesto_materiales()

    print("\nCalculando Presupuesto de Compra de Materiales...")
    mostrar_presupuesto_compras()