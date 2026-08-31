from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n=== CAFETERIA APP - Semana 10 ===")
    print("1. Agregar producto")
    print("2. Agregar bebida")
    print("3. Consultar producto")
    print("4. Modificar producto")
    print("5. Borrar producto")
    print("6. Ver todos los productos")
    print("7. Agregar cliente")
    print("8. Ver clientes")
    print("0. Salir")

def pedir(mensaje: str) -> str:
    return input(mensaje).strip()

def guardar(servicio: ArchivoServicio, resto: Restaurante):
    if not servicio.guardar_productos(resto.listar_productos()):
        print("No se pudo guardar.")

def main():
    servicio = ArchivoServicio("datos/productos.json")
    productos = servicio.cargar_productos()
    resto = Restaurante(productos)
    print(f"Se cargaron {resto.contar_productos()} productos desde datos/productos.json")

    while True:
        mostrar_menu()
        op = pedir("Elige opción: ")
        if op == "1":
            print("\n-- Agregar producto --")
            try:
                codigo = pedir("Código: ")
                nombre = pedir("Nombre: ")
                categoria = pedir("Categoría: ")
                precio = float(pedir("Precio: "))
                prod = Producto(codigo, nombre, categoria, precio)
                if resto.registrar_producto(prod):
                    print(f"Producto '{nombre}' agregado.")
                    guardar(servicio, resto)
                else:
                    print(f"Ya existe código {codigo}.")
            except ValueError as e:
                print(e)
        elif op == "2":
            print("\n-- Agregar bebida --")
            try:
                codigo = pedir("Código: ")
                nombre = pedir("Nombre: ")
                categoria = pedir("Categoría: ")
                precio = float(pedir("Precio: "))
                presentacion = pedir("Presentación (ej: 500ml): ")
                beb = Bebida(codigo, nombre, categoria, precio, presentacion)
                if resto.registrar_producto(beb):
                    print(f"Bebida '{nombre}' agregada.")
                    guardar(servicio, resto)
                else:
                    print(f"Ya existe código {codigo}.")
            except ValueError as e:
                print(e)
        elif op == "3":
            codigo = pedir("Código a buscar: ")
            p = resto.buscar_producto(codigo)
            print(p.mostrar_informacion() if p else "No encontrado.")
        elif op == "4":
            print("\n-- Modificar producto --")
            codigo = pedir("Código: ")
            p = resto.buscar_producto(codigo)
            if not p:
                print("No existe.")
                continue
            try:
                nombre = pedir(f"Nuevo nombre [{p.nombre}]: ") or p.nombre
                categoria = pedir(f"Nueva categoría [{p.categoria}]: ") or p.categoria
                precio_txt = pedir(f"Nuevo precio [{p.precio}]: ")
                precio = float(precio_txt) if precio_txt else p.precio
                pres = None
                if isinstance(p, Bebida):
                    pres = pedir(f"Nueva presentación [{p.presentacion}]: ") or p.presentacion
                if resto.actualizar_producto(codigo, nombre, categoria, precio, pres):
                    print("Actualizado.")
                    guardar(servicio, resto)
            except ValueError as e:
                print(e)
        elif op == "5":
            codigo = pedir("Código a borrar: ")
            if resto.eliminar_producto(codigo):
                print("Eliminado.")
                guardar(servicio, resto)
            else:
                print("No existe.")
        elif op == "6":
            lista = resto.listar_productos()
            if not lista:
                print("Sin productos.")
            else:
                for prod in lista:
                    print(prod.mostrar_informacion())
        elif op == "7":
            print("\n-- Agregar cliente --")
            try:
                cid = pedir("ID: ")
                nom = pedir("Nombre: ")
                tel = pedir("Teléfono (opcional): ")
                cli = Cliente(cid, nom, tel)
                if resto.registrar_cliente(cli):
                    print("Cliente agregado.")
                else:
                    print("ID duplicado.")
            except ValueError as e:
                print(e)
        elif op == "8":
            clientes = resto.listar_clientes()
            print("\n".join(clientes) if clientes else "Sin clientes.")
        elif op == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
