from .contenedor import Contenedor

class Habitacion(Contenedor):
    """Representa una habitación dentro del laberinto."""

    def __init__(self, num):
        super().__init__()  # Llama al constructor de Contenedor
        self.num = num  # Identificador único de la habitación
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    
    def entrar(self):
        """Método sobrescrito de 'ElementoMapa' para indicar que se ha entrado en la habitación."""
        print(f"Estás en la habitación {self.num}.")

    def es_habitacion(self):
        return True

    @property
    def norte(self):
        return self._norte

    @norte.setter
    def norte(self, nueva_habitacion):
        self._norte = nueva_habitacion
    
    @property
    def sur(self):
        return self._sur

    @sur.setter
    def sur(self, nueva_habitacion):
        self._sur = nueva_habitacion
    
    @property
    def este(self):
        return self._este

    @este.setter
    def este(self, nueva_habitacion):
        self._este = nueva_habitacion

    @property
    def oeste(self):
        return self._oeste

    @oeste.setter
    def oeste(self, nueva_habitacion):
        self._oeste = nueva_habitacion