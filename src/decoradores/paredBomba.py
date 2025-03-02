from ..elementos.pared import Pared

class ParedBomba(Pared):
    """Pared especial que explota cuando alguien intenta cruzarla."""
    def __init__(self, activa=False):
        super().__init__()
        self._activa = activa
    
    @property
    def activa(self):
        return self._activa

    @activa.setter
    def activa(self, estado):
        if isinstance(estado, bool):
            self._activa = estado
        else:
            raise TypeError("El estado de 'activa' debe ser un booleano.")

    def entrar(self):
        if self._activa:
            print("💥 ¡BOOM! Has chocado con una pared bomba y ha explotado.")  # Simula el Transcript
        else:
            print("🚧 Has chocado con una pared bomba, pero no está activa.") 