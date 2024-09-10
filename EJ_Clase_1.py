print("Introduccion a clases")
class animal:
    edad=3
    raza="chihuas"
    comida="croquetas"
    def come(self):
        print(f"que come el perro "+self.comida)
print(animal)
print("Creando el objeto de la clase animal")
perro=animal()
print(f"edad del perro: {perro.edad}")
print(f"raza del perro: {perro.raza}")
lacomida=perro.come()



