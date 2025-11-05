import unittest
import numpy as np

# Datos del ejercicio
edades = [23, 45, 12, 67, 34, 89, 22, 10]

# Valores esperados
media_esperada = 37.75
desviacion_esperada = 26.09477917132084   # desviación estándar (poblacional)

class TestEstadisticas(unittest.TestCase):

    def test_media(self):
        self.assertAlmostEqual(np.mean(edades), media_esperada, places=5)

    def test_desviacion_estandar(self):
        self.assertAlmostEqual(np.std(edades), desviacion_esperada, places=5)

    def test_std_un_valor(self):
        self.assertEqual(np.std([50]), 0.0)


if __name__ == "__main__":
    unittest.main()