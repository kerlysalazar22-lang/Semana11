import json
from pathlib import Path
from modelos.producto import Producto
from modelos.bebida import Bebida

class ArchivoServicio:
    """Persistencia de productos en JSON."""
    def __init__(self, ruta: str = "datos/productos.json") -> None:
        self.ruta = Path(ruta)

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                contenido = json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Advertencia: productos.json dañado, se inicia vacío.")
            return []
        except PermissionError:
            print("Sin permisos para leer productos.json.")
            return []

        if not isinstance(contenido, list):
            print("Formato incorrecto: se esperaba una lista.")
            return []

        lista: list[Producto] = []
        for reg in contenido:
            if not isinstance(reg, dict):
                continue
            try:
                if reg.get("tipo") == "Bebida":
                    # compatibilidad con 'tamano' o 'presentacion'
                    pres = reg.get("presentacion", reg.get("tamano", ""))
                    obj = Bebida(reg["codigo"], reg["nombre"], reg["categoria"], reg["precio"], pres)
                else:
                    obj = Producto(reg["codigo"], reg["nombre"], reg["categoria"], reg["precio"])
                lista.append(obj)
            except KeyError:
                print(f"Registro incompleto omitido: {reg.get('codigo','?')}")
            except ValueError as e:
                print(f"Registro inválido omitido: {e}")
        return lista

    def guardar_productos(self, productos: list[Producto]) -> bool:
        datos = [p.convertir_a_diccionario() for p in productos]
        try:
            self.ruta.parent.mkdir(parents=True, exist_ok=True)
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("Sin permisos para escribir productos.json.")
            return False
