from .ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    
    """Representa una puerta que conecta dos habitaciones en el laberinto."""

    def __init__(self, lado1, lado2):
        """Inicializa la puerta entre dos habitaciones y la deja cerrada."""
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2
    
    @property
    def abierta(self):
        """Getter: Devuelve si la puerta está abierta o cerrada."""
        return self._abierta

    @abierta.setter
    def abierta(self, estado):
        """Setter: Modifica el estado de la puerta."""
        if isinstance(estado, bool):  # Solo permite True o False
            self._abierta = estado
        else:
            raise ValueError("El estado de 'abierta' debe ser un booleano (True o False).")

    def es_puerta(self):
        """Devuelve True indicando que este objeto es una puerta."""
        return True
    
    def abrir(self):
        """Abre la puerta."""
        self._abierta = True

    def cerrar(self):
        """Cierra la puerta."""
        self._abierta = False

def entrar(self, alguien):
        """Permite que alguien entre por la puerta si está abierta."""
        if self.abierta:
            return f"{alguien} ha pasado por la puerta."
        return f"{alguien} no puede entrar, la puerta está cerrada."
