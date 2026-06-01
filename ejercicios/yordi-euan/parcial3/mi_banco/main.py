from banco import Banco
from cuenta import Cuenta

def main():
   # Sistema bancario simple


    cuentas = {}

    while True:

        print("\n/// BANCO ///")
        print("1. Aperturar nueva cuenta")
        print("2. Ver clientes")
        print("3. Depositar a una cuenta")
        print("4. Retirar de una cuenta")
        print("5. Transferencia entre cuentas")
        print("6. Buscar cuenta")
        print("7. Eliminar una cuenta")
        print("8. Salir")
        opcion = input("Elige una opción: ")

        # Aperturar cuenta

        if opcion == "1":
            cuenta = input("Número de cuenta: ")
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))
            cuentas[cuenta] = [nombre, saldo]
            print("Cuenta creada.")
            
        # Ver clientes

        elif opcion == "2":
            for cuenta, datos in cuentas.items():
                print("Cuenta:", cuenta)
                print("Cliente:", datos[0])
                print("Saldo:", datos[1])

        # Depositar

        elif opcion == "3":
            cuenta = input("Número de cuenta: ")
            if cuenta in cuentas:
                dinero = float(input("Cantidad a depositar: "))
                cuentas(cuenta)[1] += dinero
                print("Depósito exitoso.")
            else:
                print("Cuenta no encontrada.")

        # Retirar

        elif opcion == "4":
            cuenta = input("Número de cuenta: ")
            if cuenta in cuentas:
                dinero = float(input("Cantidad a retirar: "))
                if dinero <= cuentas(cuenta)[1]:
                    cuentas(cuenta)[1] -= dinero
                    print("Retiro exitoso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Cuenta no encontrada.")

        # Transferencia

        elif opcion == "5":
            origen = input("Cuenta origen: ")
            destino = input("Cuenta destino: ")
            dinero = float(input("Cantidad: "))

            if origen in cuentas and destino in cuentas:
                if dinero <= cuentas[origen][1]:
                    cuentas[origen][1] -= dinero
                    cuentas[destino][1] += dinero
                    print("Transferencia realizada.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Cuenta no encontrada.")


        # Buscar cuenta

        elif opcion == "6":
            cuenta = input("Número de cuenta: ")
            if cuenta in cuentas:
                print("Cliente:", cuentas[cuenta][0])
                print("Saldo:", cuentas[cuenta][1])
            else:
                print("Cuenta no encontrada.")


        # Eliminar cuenta

        elif opcion == "7":
            cuenta = input("Número de cuenta: ")
            if cuenta in cuentas:
                del cuentas[cuenta]
                print("Cuenta eliminada.")
            else:
                print("Cuenta no encontrada.")


        # Salir

        elif opcion == "8":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")
            
if __name__ == "__main__":
    main()