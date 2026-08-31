# Restaurante App — Semana 10

**Estudiante:** Kerly Keila Salazar Franco — 2do Semestre Programación Orientada a Objetos (UEA)  
**Semana:** 10 — Manipulación de archivos y manejo de excepciones

Aplicación de consola para gestionar el menú de un restaurante con persistencia en `datos/productos.json`.

## Estructura

```
restaurante_app/
├── datos/productos.json
├── modelos/producto.py, bebida.py, cliente.py, usuario.py
├── servicios/restaurante.py, archivo_servicio.py
├── main.py
└── README.md
```

## Cómo funciona la persistencia

- Al iniciar, `main.py` crea `ArchivoServicio` y ejecuta `cargar_productos()` con `with open(..., encoding="utf-8")` y `json.load`.
- Si el archivo no existe o está dañado, inicia con lista vacía (maneja `FileNotFoundError`, `JSONDecodeError`, `PermissionError`).
- Cada registro se valida; si falta una clave (`KeyError`) o un valor es inválido (`ValueError`) se omite con mensaje.
- Tras **agregar / modificar / borrar**, se llama a `guardar_productos()` que usa `with open(..., "w", encoding="utf-8")` y `json.dump(..., indent=4, ensure_ascii=False)`.
- Solo productos y bebidas se guardan; clientes quedan en memoria (semana 10).

## Flujo requerido

Registrar → cerrar programa → volver a abrir → los productos siguen → modificar/eliminar → persiste.

## Ejecución

```bash
python main.py
```
