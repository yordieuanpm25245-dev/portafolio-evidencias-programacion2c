import unittest 
from cuenta import Cuenta

class TestCuenta(unittest.TestCase): 
    def setUp(self):
        """
        Se ejecuta antes de cada prueba   
        """
        self.cuenta = Cuenta("Fulanito Perez Mengano", "001")
        
# ---------- PRUEBAS DEL CONSTRUCOR ------------
    
    def test_validacion_saldo(self):
        self.assertEqual(self.cuenta.saldo,0,"El saldo inicial deberia ser 0 por defecto")
        
    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente,"Fulanito Perez Mengano", "El nombre del cliente no es correcto")
        
# ---------- PRUEBAS DE DEPOSITO ----------------
    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser de 500.00")
        
    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo,0,"El saldo actual deberia ser 0")
    
    #Test para validar deposito en 0
    def test_deposito_en_0(self):
        result = self.cuenta.deposito(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo,0,"El saldo debe ser mayor a 0")

    #1. test para validar retiro con cantidad 0
    def test_retiro_en_0(self):
        result = self.cuenta.retirar(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo,0,"Saldo insuficiente")
    
    #2. test para validar retiro con cantidad negativa
    def test_retiro_cantidad_negativa(self):
        result = self.cuenta.retirar(-100)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo,0,"El saldo no puede ser valorado")
    #3. test para validar cantidad mayor al saldo
    def test_retiro_dinero_valido(self):
        result = self.cuenta.retirar(300)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo,0,"Se retiraron 300.00")

if __name__ == "__main__":
    unittest().main