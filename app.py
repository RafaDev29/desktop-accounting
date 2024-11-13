from src.controllers.ventas_controller import mostrar_presupuesto_ventas
from src.controllers.clientes_controller import mostrar_saldo_clientes_flujo_entradas

if __name__ == "__main__":
    print("Calculando Presupuesto de Ventas...")
    mostrar_presupuesto_ventas()

    print("\nCalculando Saldo de Clientes y Flujo de Entradas...")
    mostrar_saldo_clientes_flujo_entradas()
