from zope.interface import Interface
class Icoleccion(Interface):
    def InsertarElemento(indice,elemento):
        pass
    def AgregarElemento(elemento):
        pass
    def mostrarElemento(indice):
        pass
class ITesorero(Interface):
    def gastosSueldoPorEmpleado(cuil):
        pass
class IDirector(Interface):
    def modificarBasico(cuil, nuevoBasico):
        pass
    def modificarPorcentajeporcargo(cuil, nuevoPorcentaje):
        pass
    def modificarPorcentajeporcategoría(cuil, nuevoPorcentaje):
        pass
    def modificarImporteExtra(cuil, nuevoImporteExtra):
        pass