import unittest
from decimal import Decimal
from main import esAprobado

class TestEsAprobadoValidas(unittest.TestCase):
    def test_suspensos(self):
        self.assertEqual(esAprobado(Decimal("2")), False)

    def test_aprobados(self):
        self.assertEqual(esAprobado(Decimal("7.3")), True)

class TestEsAprobadoInvalidas(unittest.TestCase):
    def test_por_debajo_del_rango(self):
        with self.assertRaises(ValueError):
            esAprobado(Decimal("-5"))

    def test_por_encima_del_rango(self):
        with self.assertRaises(ValueError):
            esAprobado(Decimal("15"))

    def test_valor_no_numerico(self):
        with self.assertRaises(ValueError):
            esAprobado(None)
        with self.assertRaises(ValueError):
            esAprobado("siete")

if __name__ == '__main__':
    unittest.main(verbosity=2)
