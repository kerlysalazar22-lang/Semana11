from modelos.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, identificacion: str, nombre: str, telefono: str = "") -> None:
        super().__init__(identificacion, nombre)
        self.telefono = telefono.strip() if telefono else ""

    def mostrar_informacion(self) -> str:
        tel = f" - Tel: {self.telefono}" if self.telefono else ""
        return f"Cliente: {self.nombre} (ID: {self.identificacion}){tel}"
