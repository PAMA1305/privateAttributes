class Inventario:
    def __init__(self):
        self.productos = {}
        self.limite_productos = {'Producto1', 'Producto2', 'Producto3'}

    def agregar_producto(self, producto, cantidad, precio_unitario):
        if producto not in self.limite_productos:
            print(f"No se puede agregar {producto}. Solo se permiten: {', '.join(self.limite_productos)}.")
            return


        if producto in self.productos:
            self.productos[producto]['cantidad'] += cantidad
        else:
            self.productos[producto] = {
                'cantidad': cantidad,
                'precio_unitario': precio_unitario
            }
        print(f"Producto {producto} agregado. Cantidad: {cantidad}, Precio unitario: {precio_unitario}.")

    def mostrar_inventario(self):
        for producto, info in self.productos.items():
            print(f"Producto: {producto}, Cantidad: {info['cantidad']}, Precio unitario: {info['precio_unitario']}")

    def sumar_precios_unitarios(self):
        total_precios = sum(info['precio_unitario'] for info in self.productos.values())
        print(f"Suma de precios unitarios: {total_precios}")