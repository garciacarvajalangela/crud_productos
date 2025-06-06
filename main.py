import json
import os

DB_FILE = 'productos.json'

def cargar_productos():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def guardar_productos(productos):
    with open(DB_FILE, 'w') as f:
        json.dump(productos, f, indent=4)

def crear_producto(producto):
    productos = cargar_productos()
    if any(p["id"] == producto["id"] for p in productos):
        raise ValueError("ID duplicado")
    productos.append(producto)
    guardar_productos(productos)

def leer_producto(product_id):
    productos = cargar_productos()
    return next((p for p in productos if p["id"] == product_id), None)

def actualizar_producto(product_id, nuevos_datos):
    productos = cargar_productos()
    for producto in productos:
        if producto["id"] == product_id:
            producto.update(nuevos_datos)
            guardar_productos(productos)
            return
    raise ValueError("Producto no encontrado")

def eliminar_producto(product_id):
    productos = cargar_productos()
    nuevos = [p for p in productos if p["id"] != product_id]
    if len(nuevos) == len(productos):
        raise ValueError("Producto no encontrado")
    guardar_productos(nuevos)
