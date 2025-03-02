class Orientacion:
    """Clase que representa una orientación en el laberinto (Norte, Sur, Este, Oeste)."""

     def __init__(self, direccion):
        """Inicializa la orientación con una dirección específica."""
        direcciones_validas = {"norte", "sur", "este", "oeste"}
        if direccion.lower() not in direcciones_validas:
            raise ValueError("Dirección inválida. Usa: 'norte', 'sur', 'este' o 'oeste'.")
        self.direccion = direccion.lower()
