class Cuenta:
    
    def __init__(self, cliente, cuenta, saldo = 0):
        """ 
        Inicializa una cuenta bancaria
        
        Args:
            cliente(str): Nombre del cliente propietario de la cuenta.
            cuenta(str): Numero de la cuenta bancaria.
            saldo(float, optional): Saldo inicial de la cuenta.
                Por defecto es 0
        """
        
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
        
    def deposito (self, cantidad):
        """
        Realiza un deposito a la cuenta.
        
        Args: 
            cantidad(float): Cantidad de dinero a depositar.
            
        Returns:
            bool: True si el deposito fue exitoso,
            False si la cantidad es invalida.
        """
        
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False 
    
    def retirar (self, cantidad):
        """
        Retira dinero de la cuenta si hay saldo suficiente.
        
        Args: 
            cantidad(float): Cantidad de dinero a retirar.
        
        Returns:
            bool: True si el retiro fue exitoso,
            False si la cantidad es invalida o no hay saldo insuficiente.
        """
        # verifica que la cantidad sea valida y que exista saldo suficiente
        if cantidad > 0 and cantidad <= self.saldo:
            # resta la cantidad del saldo actual    
            self.saldo -= cantidad
            # indica que el retiro fue exitoso
            return True
        # indica que el retiro no pudo realizarse
        return False

def main():
    pass

if __name__ == "__main__":
    main()  