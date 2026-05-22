class Cafetera:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler_cafe()
        print("Cafe listo")
        
    def __hervir_agua(self):
        print("Hirviendo el agua")
        
    def __moler_cafe(self):
        print("Moliendo cafe")
        
def main():
    cafetera = Cafetera()
    cafetera.preparar_cafe()
    
if __name__ == "__main__":
    main()