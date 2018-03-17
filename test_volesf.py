import unittest
import volesf

#crear casos de prueba para las funciones
# para eso debemos crear una clase

class Testvol_esf(unittest.TestCase):
    # Escribimos el metodo
    def test_vol_esf(self):
        result=volesf.vol_esf(3)
        self.assertEqual(result,113.04)

        #113.04


if __name__ == '__main__':
    unittest.main()

