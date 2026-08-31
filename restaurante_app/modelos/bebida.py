from modelos.producto import Producto

class Bebida(Producto):
    """Bebida con presentacion (ml)."""
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, presentacion: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.presentacion = presentacion

    @property
    def presentacion(self) -> str:
        return self._presentacion

    @presentacion.setter
    def presentacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Debe ingresar una presentación válida.")
        self._presentacion = valor.strip()

    def convertir_a_diccionario(self) -> dict:
        datos = super().convertir_a_diccionario()
        datos["presentacion"] = self.presentacion
        datos["tipo"] = "Bebida"
        return datos

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Bebida":
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            presentacion=datos["presentacion"]
        )

    def mostrar_informacion(self) -> str:
        return f"Bebida | {self.codigo} - {self.nombre} ({self.categoria}) $ {self.precio:.2f} [{self.presentacion}]"
