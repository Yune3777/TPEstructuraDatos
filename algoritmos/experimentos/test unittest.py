import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import unittest
from servicios.catalogo import Catalogo

class TestCatalogo(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()
        self.catalogo.cargar_desde_json("datos/dataset_10.json")
    
    def test_buscar_por_nombre(self):
        resultado = self.catalogo.buscar("metallica")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Metallica")

    def test_buscar_devuelve_none_si_no_existe(self):
        self.assertIsNone(self.catalogo.buscar("no-existe"))
    
    def test_listar_devuelve_todos(self):
        self.assertTrue(len(self.catalogo.listar()) > 0)
    
    def test_filtrar_por_genero(self):
        resultados = self.catalogo.filtrar("pop")
        self.assertTrue(all(p.genero.lower() == "pop" for p in resultados))

if __name__ == "__main__":
    unittest.main()