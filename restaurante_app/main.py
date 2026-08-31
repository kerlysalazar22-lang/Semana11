from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- RESTAURANTE APP (SEMANA 11) ---")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Modificar producto")
    print("4. Borrar producto")
    print("5. Ver todos los productos")
    print("6. Agregar usuario")
    print("7. Ver usuarios")
    print("8. Realizar venta")
    print("9. Consultar ventas por usuario")
    print("0. Salir")

def pedir(mensaje: str) -> str:
    return input(mensaje).strip()

def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = pedir("Elige opción: ")

        if opcion == "1":
            codigo = pedir("Código del producto: ")
            nombre = pedir("Nombre del producto: ")
            try:
                precio = float(pedir("Precio: "))
                stock = int(pedir("Stock inicial: "))
                producto = Producto(codigo, nombre, precio, stock)
                if restaurante.agregar_producto(producto):
                    print("¡Producto registrado exitosamente!")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            codigo = pedir("Código a buscar: ")
            p = restaurante.buscar_producto(codigo)
            if p:
                print(f"Encontrado: [{p.codigo}] {p.nombre} - ${p.precio:.2f} | Stock: {p.stock}")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = pedir("Código del producto a modificar: ")
            if restaurante.buscar_producto(codigo):
                try:
                    nombre = pedir("Nuevo nombre: ")
                    precio = float(pedir("Nuevo precio: "))
                    stock = int(pedir("Nuevo stock: "))
                    if restaurante.modificar_producto(codigo, nombre, precio, stock):
                        print("Producto modificado correctamente.")
                except ValueError as e:
                    print(f"Error en los datos: {e}")
            else:
                print("El producto no existe.")

        elif opcion == "4":
            codigo = pedir("Código del producto a eliminar: ")
            if restaurante.eliminar_producto(codigo):
                print("Producto eliminado con éxito.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            productos = restaurante.listar_productos()
            if productos:
                print("\nLISTA DE PRODUCTOS:")
                for p in productos:
                    print(f"- [{p.codigo}] {p.nombre} - ${p.precio:.2f} | Stock: {p.stock}")
            else:
                print("No hay productos registrados.")

        elif opcion == "6":
            identificacion = pedir("Identificación del usuario: ")
            nombre = pedir("Nombre completo: ")
            email = pedir("Email: ")
            usuario = Usuario(identificacion, nombre, email)
            if restaurante.agregar_usuario(usuario):
                print("Usuario registrado exitosamente.")
            else:
                print("Error: El usuario ya está registrado.")

        elif opcion == "7":
            usuarios = restaurante.listar_usuarios()
            if usuarios:
                print("\nLISTA DE USUARIOS:")
                for u in usuarios:
                    print(f"- [{u.identificacion}] {u.nombre} ({u.email})")
            else:
                print("No hay usuarios registrados.")

        elif opcion == "8":
            id_usuario = pedir("ID del Usuario comprador: ")
            cod_producto = pedir("Código del Producto a comprar: ")
            try:
                cant = int(pedir("Cantidad: "))
                if restaurante.vender_producto(cod_producto, id_usuario, cant):
                    print("¡Venta realizada y registrada con éxito!")
                else:
                    print("Error: Usuario/Producto inexistente o stock insuficiente.")
            except ValueError:
                print("La cantidad debe ser un número entero válido.")

        elif opcion == "9":
            id_usuario = pedir("Identificación del usuario: ")
            ventas = restaurante.consultar_ventas_usuario(id_usuario)
            if ventas:
                print(f"\nVENTAS REGISTRADAS PARA EL USUARIO {id_usuario}:")
                for v in ventas:
                    prod = restaurante.buscar_producto(v.producto_codigo)
                    nombre_prod = prod.nombre if prod else v.producto_codigo
                    print(f"- Producto: {nombre_prod} (Cód: {v.producto_codigo}) | Cantidad: {v.cantidad}")
            else:
                print("No se encontraron ventas para este usuario.")

        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()