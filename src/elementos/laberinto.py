from .Contenedor import Contenedor

class Laberinto(Contenedor):
    """Representa el laberinto del juego, compuesto por múltiples habitaciones, elementos y bichos."""

    def __init__(self):
        super().__init__()  # Llama al constructor de Contenedor

    def agregar_habitacion(self, habitacion):
        self.hijos.append(habitacion) 
    
    def eliminar_habitacion(self, habitacion):
        if habitacion in self.hijos:
            self.hijos.remove(habitacion)
        else:
            print("La habitación no existe en el laberinto.")
    
    def entrar(self):
        """Método vacío, sin implementación."""
        pass  # No realiza ninguna acción
        