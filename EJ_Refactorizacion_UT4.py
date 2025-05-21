from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        pass


# Clase para recetas vegetarianas
class RecetaVegetariana(receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingredientes in self.ingredientes:
            print(f"- {ingredientes}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas no vegetarianas
class RecetaNoVegetariana(receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingredientes in self.ingredientes:
            print(f"- {ingredientes}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


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

# Función principal
def principal():
    receta_vegetariana = RecetaVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta_no_vegetariana = RecetaNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta_vegetariana)
    utilidades.imprimir_receta(receta_no_vegetariana)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in receta_vegetariana.ingredientes:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in receta_no_vegetariana.ingredientes:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
