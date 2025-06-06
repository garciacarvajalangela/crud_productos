import unittest
import main
import os

class TestCRUD(unittest.TestCase):

    def setUp(self):
        """Limpia el archivo de productos antes de cada prueba."""
        main.guardar_productos([])

    # --- CREAR PRODUCTO ---

    def test_crear_producto_exitoso(self):
        producto = {
            "id": 1,
            "nombre": "Camiseta",
            "descripcion": "Blanca",
            "precio": 10000,
            "cantidad": 5
        }
        main.crear_producto(producto)
        productos = main.cargar_productos()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0]["nombre"], "Camiseta")

    def test_crear_producto_id_duplicado(self):
        producto = {"id": 1, "nombre": "Camiseta", "descripcion": "Blanca", "precio": 10000, "cantidad": 5}
        main.crear_producto(producto)
        with self.assertRaises(ValueError):
            main.crear_producto(producto)

    # --- LEER PRODUCTO ---

    def test_leer_producto_exitoso(self):
        producto = {"id": 2, "nombre": "Zapatos", "descripcion": "Cuero", "precio": 30000, "cantidad": 2}
        main.crear_producto(producto)
        resultado = main.leer_producto(2)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Zapatos")

    def test_leer_producto_no_existente(self):
        self.assertIsNone(main.leer_producto(999))

    # --- ACTUALIZAR PRODUCTO ---

    def test_actualizar_producto_exitoso(self):
        main.crear_producto({"id": 3, "nombre": "Gorra", "descripcion": "Azul", "precio": 5000, "cantidad": 10})
        main.actualizar_producto(3, {"precio": 6000})
        producto = main.leer_producto(3)
        self.assertEqual(producto["precio"], 6000)

    def test_actualizar_producto_no_existente(self):
        with self.assertRaises(ValueError):
            main.actualizar_producto(999, {"precio": 5000})

    # --- ELIMINAR PRODUCTO ---

    def test_eliminar_producto_exitoso(self):
        main.crear_producto({"id": 4, "nombre": "Bolso", "descripcion": "Cuero", "precio": 20000, "cantidad": 1})
        main.eliminar_producto(4)
        self.assertIsNone(main.leer_producto(4))

    def test_eliminar_producto_no_existente(self):
        with self.assertRaises(ValueError):
            main.eliminar_producto(888)

if __name__ == '__main__':
    unittest.main()

# --- PRUEBA DE COMMIT A GITHUB ---