class Perro:
    # Atributos de la clase  perro
    especie = "Canis lupus familiaris"
    0
    # Constructor de la clase perro
    def __init__ (self, nombre,raza = ("Caramelo"), edad = 0): 
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    # Metodo para imprimir los datos del perro
    def imprimeDatos(self):
        print("Nombre:",self.nombre)
        print("Raza:",self.raza)
        print("Edad:",self.edad)
        print("Especie",self.especie)
        
def main():
    # Crear un objeto de la clase perro
    perro1 = Perro("Firulais","Labrador",5)
    perro1.imprimeDatos()
    perro2 = Perro("Rex","Pastor Aleman",3)
    perro2.imprimeDatos()
    print("Informacion del perro 2: ",perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Max,","Bulldog",2)
    perro3.imprimeDatos()
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimeDatos()
    perro2.raza = "Pastor Belga"
    perro2.imprimeDatos()
    perro5 = Perro("Raya","Siames",1)
    perro5.especie = "Felis catus"
    perro5.imprimeDatos
    
if __name__ == "__main__":
    main()