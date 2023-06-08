class Nodo:
    __siguiente: object
    def __init__(self, personal):
        self.__auto=personal
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__auto