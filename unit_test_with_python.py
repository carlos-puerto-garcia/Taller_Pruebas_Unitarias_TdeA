import unittest
import volesf
import ejemplo
import FactorialNum

#crear casos de prueba para las funciones
# para eso debemos crear una clase

class Testvol_esf(unittest.TestCase):
    # Escribimos el metodo
    def test_vol_esf(self):
        result=volesf.vol_esf(3)
        self.assertEqual(result,113.04)

        #113.04
#Integra tus casos de prueba
class Testejemplo_add(unittest.TestCase):
    # Escribimos el metodo
    def test_ejemplo_add(self):
        result=ejemplo.add(7,3)
        self.assertEqual(result,10)
        
class TestFactorial(unittest.TestCase):
    'escribimos el metodo nombre del archivo'
    def test_func_factorial(self):
        result=FactorialNum.Factorial(10)
        'validamos que sean iguales'
        self.assertEqual(result,3628800)        

if __name__ == '__main__':
    unittest.main()

