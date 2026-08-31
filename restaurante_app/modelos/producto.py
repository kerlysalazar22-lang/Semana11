class Producto:
    """Producto del menu del restaurante."""
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Debe ingresar un código válido.")
        self._codigo = valor.strip().upper()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Debe ingresar un nombre válido.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Debe ingresar una categoría válida.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            v = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser numérico.")
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        self._precio = round(v, 2)

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "tipo": "Producto"
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"]
        )

    def mostrar_informacion(self) -> str:
        return f"Producto | {self.codigo} - {self.nombre} ({self.categoria}) $ {self.precio:.2f}"
