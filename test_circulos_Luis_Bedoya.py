import math
import unittest
import circulos

class Test_Circulos(unittest.TestCase):
	def test_area(self):
		resultado = circulos.Radio_circulo(2)
		self.assertEqual(resultado,12.566370614359172)

if __name__=='__main__':
	unittest.main()