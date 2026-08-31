 Restaurante App — Semana 11 (Persistencia y Relaciones)

**Estudiante:** Kerly Salazar  
**Asignatura:** Programación Orientada a Objetos  
**Universidad:** Universidad Estatal Amazónica  

## Descripción del Sistema
Evolución de la aplicación de consola en Python para la gestión de un restaurante. En esta versión se incorpora la entidad `Venta`, la administración de `stock` en los productos y la persistencia completa en formato JSON para las colecciones de **Productos**, **Usuarios** y **Ventas**.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
