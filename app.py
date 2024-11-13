from src.controllers.ventas_controller import mostrar_presupuesto_ventas
from src.controllers.clientes_controller import mostrar_saldo_clientes_flujo_entradas
from src.controllers.produccion_controller import mostrar_presupuesto_produccion
from src.controllers.materiales_controller import mostrar_presupuesto_materiales
from src.controllers.compras_controller import mostrar_presupuesto_compras
from src.controllers.proveedores_controller import mostrar_saldo_proveedores
from src.controllers.mano_obra_controller import mostrar_presupuesto_mano_obra
from src.controllers.gastos_indirectos_controller import mostrar_presupuesto_gastos_indirectos
from src.controllers.gastos_operacion_controller import mostrar_presupuesto_gastos_operacion
from src.controllers.costo_unitario_controller import  mostrar_costo_unitario_producto
from src.controllers.inventario_final_controller import mostrar_inventario_final

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
    
    print("\nDeterminación del Saldo de Proveedores y Flujo de Salidas...")
    mostrar_saldo_proveedores()
    
    print("\nCalculando Presupuesto de Mano de Obra Directa...")
    mostrar_presupuesto_mano_obra()
    
    print("Calculando Presupuesto de Gastos Indirectos de Fabricación...")
    mostrar_presupuesto_gastos_indirectos()
    
    print("Calculando Presupuesto de Gastos de Operación...")
    mostrar_presupuesto_gastos_operacion()
    
    print("Calculando Determinación del Costo Unitario de Productos Terminados...")
    mostrar_costo_unitario_producto()
    print("Calculando Valuación de Inventarios Finales...")
    mostrar_inventario_final()