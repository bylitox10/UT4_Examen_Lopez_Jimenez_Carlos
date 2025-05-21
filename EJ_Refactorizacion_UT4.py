from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos
    @abstractmethod
    def mostrar(self):
        nombre_receta = int(input("Que receta quieres usar: 1-Vegetariana o 2-No vegetariana"))
        if nombre_receta == 1:
            print(f"Receta vegetariana: {self.nombre}")
            print("Ingredientes:")
        elif nombre_receta == 2:
            print(f"Receta NO vegetariana: {self.nombre}")
            print("Ingredientes:")   
        for ingredientes in self.ingredientes:
            print(f"- {ingredientes}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class RecetaVegetariana(receta,ABC):
    @abstractmethod
    def mostrar(self):
        pass
# Clase para recetas no vegetarianas
class RecetaNoVegetariana(receta,ABC):
    @abstractmethod
    def mostrar(self):
        pass


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

def crear_receta():
    nombre1 = input("Nombre receta")
    ingredientes1 = []
    print("Dime ingredientes y pon fin para terminar.")
    while True:
        ing = input("- ")
        if ing.lower() == "fin":
            break
        ingredientes1.append(ing)
    pasos1 = []
    print("Dime los pasos, escribe fin para terminar: ")
    while True:
        paso = input("- ")
        if paso.lower() == "fin":
            break
        pasos1.append(paso)
    return nombre1, ingredientes1, pasos1

# Función principal

def principal():
    nombre1, ingredientes1, pasos1 = crear_receta()
    tipo = int(input("receta que quieres crear: 1-vegetariana o 2-no vegetariana "))
    if tipo == 1:
        print("Crear receta vegetariana: ")
        #apto_veganos = input("Dime si es para veganos: ")
        receta1 = RecetaVegetariana(nombre1, ingredientes1, pasos1,) #apto_veganos)
    elif tipo == 2:
        print("Crear receta para no vegetarianos: ")
        #no_apto_veganos = input("Dime el punto de la carne: ")
        receta2 = RecetaNoVegetariana(nombre1, ingredientes1, pasos1,) #no_apto_veganos)
    else:
        print("No has indicado el tipo correcto")
    return receta1, receta2


# Ejecutar el programa
if __name__ == "__main__":
    principal()
