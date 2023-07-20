class Automovil:
    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color
    
    def avanzar(self):
        print("El coche avanza y es un: " + self.marca)

    def retroceder(self):
        print("El coche retrocede y es de color: " + self.color)
    
if __name__ == "__main__":
    auto = Automovil("BMW", "Azul") #Crea el objeto, se instancia la clase.
    auto.avanzar()
    auto.retroceder()

    auto1 = Automovil("Dodge", "Rojo")
    auto1.retroceder()
    auto1.avanzar()
    