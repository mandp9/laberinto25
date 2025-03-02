from abc import abstractmethod
from .elementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    """Contenedor es el Composite. Es un EM que tiene hijos."""

    def __init__(self):
        """Inicializa el contenedor con una lista de hijos y un diccionario de orientaciones."""
        super().__init__()
        self.hijos = []  
        self.orientaciones = {}  # Diccionario de direcciones (Norte, Sur, Este, Oeste)
    
    @property
    def hijos(self):
        """Getter para obtener la lista de hijos del contenedor."""
        return self._hijos

    @hijos.setter
    def hijos(self, nuevos_hijos):
        """Setter para actualizar la lista de hijos. Solo permite listas."""
        if isinstance(nuevos_hijos, list):
            self._hijos = nuevos_hijos
        else:
            raise TypeError("hijos debe ser una lista de elementos.")


    def agregar_hijo(self, hijo):
        """Agrega un hijo al contenedor y establece su padre."""
        hijo.padre = self  # Establece el contenedor actual como el padre del hijo
        self.hijos.append(hijo) 

    @property
    def orientaciones(self):
        """Getter para obtener la lista de orientaciones del contenedor."""
        return self._orientaciones

    @orientaciones.setter
    def orientaciones(self, nuevas_orientaciones):
        """Setter para actualizar la lista de orientaciones. Solo permite listas."""
        if isinstance(nuevas_orientaciones, list):
            self._orientaciones = nuevas_orientaciones
        else:
            raise TypeError("orientaciones debe ser una lista de elementos.")
    def eliminar_hijo(self, hijo):
        if hijo in self.hijos:
            self.hijos.remove(hijo) 
        else:
            print("No existe ese objeto en los hijos del contenedor.")  

    def agregar_orientacion(self, orientacion):
        self.orientaciones.append(orientacion)  # Añade la orientación a la lista

    def obtener_elemento_or(self, una_or):
        return una_or.obtener_elemento_or_en(self)

    def es_habitacion(self):
        return False

    @abstractmethod
    def poner_elemento(self, elemento, contenedor):
        """
        Método abstracto para colocar un elemento en un contenedor.
        Debe ser implementado por subclases.
        """
        pass

    def poner_en_orientacion(self, orientacion, elemento):
        """
        Agrega un elemento en una orientación específica dentro del contenedor.
        Si la orientación ya existe, delega la colocación al objeto correspondiente.
        """
        if orientacion in self._orientaciones:
            self._orientaciones[orientacion].poner_elemento(elemento, self)
        else:
            raise ValueError(f"La orientación '{orientacion}' no está definida en este contenedor.")