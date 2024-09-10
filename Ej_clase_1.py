print("Introduccion a clases")
print("")

class Animal:
    edad = 6
    raza = "chihuahua"
    comida = "Croquetas"
    def come(self):
        print(f"El perro come "+self.comida)

print(Animal)
print("Creando el objeto de la clase Animal")
perro = Animal()
print(f"La edad del perro es: {perro.edad}")
print(f"La raza del perro es: {perro.raza}")
perro.come()
