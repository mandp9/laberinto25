from abc import ABC, abstractmethod

class ElementoMapa(ABC):
   
    """clase base para los elementos del mapa."""
    
    def entrar(self):
        """Método abstracto que deben implementar las subclases."""
        pass
    def es_pared(self):
        """Sobrescribe el método para indicar que sí es una pared."""
        return False

    def es_puerta(self):
        """Sobrescribe el método para indicar que sí es una puerta."""
        return False
    
    def obtener_padre(self):
        """Devuelve el padre del elemento en la jerarquía del laberinto."""
        return self._padre

    def establecer_padre(self, padre):
        """Asigna un padre al elemento."""
        self._padre = padre