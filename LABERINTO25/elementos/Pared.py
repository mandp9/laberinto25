from .ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    
    def entrar(self, alguien):
        """Simula que alguien choca con la pared."""
        return f"{alguien} ha chocado contra una pared."

    def es_pared(self):
        """Sobrescribe el método para indicar que es una pared."""
        return True