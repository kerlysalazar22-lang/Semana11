from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from modelos.usuario import Usuario

class Restaurante:
    """Gestiona productos y clientes en memoria."""
    def __init__(self, productos: list[Producto] | None = None) -> None:
        self._productos: list[Producto] = productos if productos is not None else []
        self._clientes: list[Cliente] = []
        self._usuarios: list[Usuario] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip().upper()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, presentacion: str | None = None) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        prod.nombre = nombre
        prod.categoria = categoria
        prod.precio = precio
        if isinstance(prod, Bebida) and presentacion is not None:
            prod.presentacion = presentacion
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        self._productos.remove(prod)
        return True

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def contar_productos(self) -> int:
        return len(self._productos)

    # Clientes y usuarios solo en memoria
    def registrar_cliente(self, cliente: Cliente) -> bool:
        for c in self._clientes:
            if c.identificacion == cliente.identificacion:
                return False
        self._clientes.append(cliente)
        return True

    def listar_clientes(self) -> list[str]:
        return [c.mostrar_informacion() for c in self._clientes]
