import unittest
import volesf
import ejemplo
import FactorialNum
import edad
import Numpar
import resta
import val_positivo
import math
import media
import circulos_Luis_Bedoya


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

'''diego ubarnes martinez'''
class testedad(unittest.TestCase):
    '''escribimos el metodo '''
    def test_edad(self):
        result= edad.edad(2000)
        self.assertEqual(result,18)

        #18

class TestNumpar(unittest.TestCase):
    # Escribimos el metodo
    def test_num_par(self):
        result=Numpar.numpar(2)
        self.assertEqual(result,"Este numero es par")

class testPositivo(unittest.TestCase):
    # Código para validar si un número es positivo - Jhony Andrés Angulo
    def test_positivo(self):
        num = int(input("Ingrese un número a evaluar:\n"))
        val = val_positivo.positivo(num)
        self.assertEqual(val,"Positivo")

class Testresta(unittest.TestCase):
    # Escribimos el metodo
    def test_resta(self):
        result=resta.menos(7,3)
        self.assertEqual(result,5)


class testImpares(unittest.TestCase):
    #escribimos el metodo
    def test_Impares(self):
        numero = input("ingrese un nùmero : ")
        result=Impares.Impares(numero)
        self.assertGreater(result, 5)        


class Test_Circulos(unittest.TestCase):
    def test_area(self):
        resultado = circulos.Radio_circulo(2)
        self.assertEqual(resultado,12.566370614359172)
		
class Testmedia(unittest.TestCase):
    # Escribimos el metodo
    def test_media(self):
        result=media.medida_media(3,5)
        self.assertEqual(result,4)


if __name__ == '__main__':
    unittest.main()

