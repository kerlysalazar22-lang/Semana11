class Usuario:
    def __init__(self, identificacion: str, nombre: str) -> None:
        if not identificacion or not identificacion.strip():
            raise ValueError("Identificación requerida.")
        if not nombre or not nombre.strip():
            raise ValueError("Nombre requerido.")
        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.nombre} (ID: {self.identificacion})"
