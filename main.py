from classVenta import Venta
from productos import Inventario

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Pedro")
venta.set_productos(["Producto1", "Producto2", "Producto3"])
venta.set_total(150.75)

venta.mostrar_detalle()

#Blackpoint se va a ejecutar hasta esa linea roja, y solo se


inventario = Inventario()

inventario.agregar_producto('Producto1', 3, 36)
inventario.agregar_producto('Producto2', 4, 240)
inventario.agregar_producto('Producto3', 5, 225)  # No permitido

inventario.sumar_precios_unitarios()