import unittest
from unittest import TestCase
from main import Calculadora


class TestCalculadora(TestCase):
    def test_somar(self):
        self.assertEqual(Calculadora.somar(3, 2), 5)

    def test_subtrair(self):
        self.assertEqual(Calculadora.subtrair(3, 2), 1)

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(3, 2), 6)

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(3, 2), 1.5)


if __name__ == '__main__':
    unittest.main()
