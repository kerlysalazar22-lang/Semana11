from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = ArchivoServicio.cargar_productos()
        self.usuarios: list[Usuario] = ArchivoServicio.cargar_usuarios()
        self.ventas: list[Venta] = ArchivoServicio.cargar_ventas()

    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self.productos.append(producto)
        ArchivoServicio.guardar_productos(self.productos)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def modificar_producto(self, codigo: str, nuevo_nombre: str, nuevo_precio: float, nuevo_stock: int) -> bool:
        p = self.buscar_producto(codigo)
        if not p:
            return False
        p.nombre = nuevo_nombre
        p.precio = nuevo_precio
        p.stock = nuevo_stock
        ArchivoServicio.guardar_productos(self.productos)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        p = self.buscar_producto(codigo)
        if p:
            self.productos.remove(p)
            ArchivoServicio.guardar_productos(self.productos)
            return True
        return False

    def agregar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion):
            return False
        self.usuarios.append(usuario)
        ArchivoServicio.guardar_usuarios(self.usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        producto.vender(cantidad)
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self.ventas.append(venta)

        ArchivoServicio.guardar_productos(self.productos)
        ArchivoServicio.guardar_ventas(self.ventas)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []
        for venta in self.ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario