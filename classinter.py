from insterface import ITesorero,IDirector
from zope.interface import implementer
from manpersonal import lista
from personal import docente,apoyo,docenteinvestigador,investigador
@implementer(ITesorero)
class tesorero():
    def __init__(self, usuario = 'uTesorero', contraseña = 'ag@74ck',l=lista()):
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__lista=l
    
    def gastosSueldoPorEmpleado(self,cuil):
        a=self.__lista.busq(cuil)
        if a!=None:
            print(f'Sueldo:{a.getsueldo()}')
        else:
            print('No se encontro')
    
    def optesorero(self): 
        j = True
        usuario = input('ingrese nombre de usuario o ingrese "salir" para terminar: ')
        while j and usuario != 'salir':
            if usuario == self.__usuario:
                contraseña = input('ingrese la contraseña: ')
                if contraseña == self.__contraseña:
                    j = False
                else:
                    print('contraseña incorrecta: ')
            else:
                print('usuraio incorrecto')
        return j

@implementer(IDirector)
class director():
    def __init__(self, usuario = 'uDirector', contraseña = 'ufC77#!1',l=lista()):
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__lista=l

    def opdirector(self):
        j = True
        usuario = input('ingrese nombre de usuario o ingrese "salir" para terminar: ')
        while j and usuario != 'salir':
            if usuario == self.__usuario:
                contraseña = input('ingrese la contraseña: ')
                if contraseña == self.__contraseña:
                    j = False
                else:
                    print('contraseña incorrecta: ')
            else:
                print('usuraio incorrecto')
        return j
    
    def modificarBasico(self,cuil, nuevoBasico):
        a=self.__lista.busq(cuil)
        if a!=None:
            a.set_sueldo_basico(nuevoBasico)
        else:
            print('cuil incorrecto o no encontrado')
    
    def modificarPorcentajeporcargo(self,cuil, nuevoPorcentaje):
        a=self.__lista.busq(cuil)
        if a!=None:
            if isinstance(a,docente):
                p=float(input('ingrese nuevo porcentaje a multiplicar'))
                docente.set_cargo(p)
            elif isinstance(a,docenteinvestigador):
                p=float(input('ingrese nuevo porcentaje a multiplicar'))
                docenteinvestigador.set_cargo(p)
            else:
                print('No es docente o docente investigador')
        else:
            print('No se encontro')
    
    def modificarPorcentajeporcategoría(self,cuil, nuevoPorcentaje):
        a=self.__lista.busq(cuil)
        if a!=None:
            if isinstance(a,apoyo):
                apoyo.set_cargo(nuevoPorcentaje)
            else:
                print('No es de apoyo')
        else:
            print('No se encontro')
    
    def modificarImporteExtra(self,cuil, nuevoImporteExtra):
        a=self.__lista.busq(cuil)
        if a!=None:
            if isinstance(a,docenteinvestigador):
                a.set_imp(nuevoImporteExtra)
            else:
                print('No es docente investigador')
        else:
            print('cuil incorrecto o no se encontro')