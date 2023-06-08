import json
from personal import docente
from personal import apoyo
from personal import investigador
from personal import docenteinvestigador
from zope.interface import Interface, implementer
from insterface import Icoleccion
from nodo import Nodo

@implementer(Icoleccion)
class lista():
    __comienzo:Nodo
    __actual:Nodo
    __tope:int
    __indice:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope=0
        self.__indice=0
    def __iter__(self):
        self.__actual=self.__comienzo
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def instanciar(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 3\\ejercicio8\\personal.json', 'r') as f:
            datos = json.load(f)
            for variable in datos:
                if variable['tipo'] == 'docente':
                    personal = docente(variable['cuil'], variable['ape'], variable['nom'], variable['sueldobasico'], variable['anti'], variable['carre'], variable['cargo'], variable['catedra'])
                elif variable['tipo'] == 'apoyo':
                    personal = apoyo(variable['cuil'], variable['ape'], variable['nom'], variable['sueldobasico'], variable['anti'], variable['categoria'])
                elif variable['tipo'] == 'investigador':
                    personal = investigador(variable['cuil'], variable['ape'], variable['nom'], variable['sueldobasico'], variable['anti'], variable['areainv'], variable['tipoinv'])
                    if variable['tipo'] == 'docenteinvestigador':
                        personal = docenteinvestigador(variable['cuil'], variable['ape'], variable['nom'], variable['sueldobasico'], variable['anti'], variable['carre'], variable['cargo'], variable['catedra'], variable['areainv'], variable['tipoinv'], variable['catprog'], variable['impextra'], variable['investigacion'])
                self.AgregarElemento(personal)

    def InsertarElemento(self, indice,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo is None or indice<=0:
            self.__comienzo=nodo
        else:
            nodo_actual = self.__comienzo
            nodo_anterior = None
            i = 0
            while nodo_actual is not None and i < indice:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                i += 1
            nodo_anterior.setSiguiente(nodo)
            nodo.setSiguiente(nodo_actual)
        self.__actual=nodo
        self.__tope+=1

    def AgregarElemento(self,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            nodo_actual = self.__comienzo
            while nodo_actual.getSiguiente() is not None:
                nodo_actual = nodo_actual.getSiguiente()
            nodo_actual.setSiguiente(nodo)
        self.__actual=nodo
        self.__tope+=1
        

    def mostrarElemento(self, indice):
        aux=self.__comienzo
        i=0
        while aux!=None and i<indice:
            i+=1
            aux=aux.getSiguiente()
        if i==indice:
            n=aux.getDato()
        else:
            n=None
        return n 

    def docinv(self):
        carrera = input('ingrese carrera: ')
        l=[]
        for instancia in self:
            if isinstance(instancia, docenteinvestigador):
                if instancia.getcarrera() == carrera:
                    l.append(instancia)
        l.sort()
        for i in l:
            print(i.getdatos())

    def cont(self):
        contadordi = 0
        contadori = 0
        areainv = input('ingrese el area de investigacion para buscar:')
        for instancia in self:
            if isinstance(instancia, (docenteinvestigador, investigador)):
                if instancia.getareainv() == areainv:
                    if instancia.gettipo() == 'docente investigador':
                        contadordi += 1
                    elif instancia.gettipo() == 'investigador':
                        contadori += 1
        print(f'la cantidad de docentes investigadores es: {contadordi}\nla cantidad de investigadores es: {contadori}')

    def most(self):
        lista = []
        for variable in self:
            if isinstance(variable,(docente, apoyo, investigador, docenteinvestigador)):
                nombre = variable.getnom()
                apellido = variable.getape()
                tipo = variable.gettipo()
                sueldo = variable.getsueldo()
                instancia = (nombre, apellido, tipo, sueldo)
                lista.append(instancia)
        lista.sort()
        for i in lista:
            if isinstance(i,docente):
                print(f'{i}, Cargo: {docente.gettipo()}')
            elif isinstance(i, apoyo):
                print(f'{i}, Cargo:{apoyo.gettipo()}')
            elif isinstance(i, investigador):
                print(f'{i}, Cargo: {investigador.gettipo()}')
            elif isinstance(i, docenteinvestigador):
                print(f'{i}, Cargo: {docente.gettipo()}')

    def catte(self):
        coste = 0
        categoria = input('ingrese categoria: ')
        for instancia in self:
            if isinstance(instancia, docenteinvestigador):
                if instancia.getcatprog() == categoria:
                    print(f'{instancia.getnom()} {instancia.getape()} {instancia.getimpextra()}')
                    coste += instancia.getimpextra()
        print(coste)

    def guarda(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 3\\ejercicio8\\personal.json', 'w') as f:
                    datos = []
                    for elemento in self:
                        datos.append(elemento.__dict__)
                    json.dump(datos, f)

    def busq(self,cuil):
        aux=self.__comienzo
        while aux!=None and aux.getDato().getcuil()!=cuil:
            aux=aux.getSiguiente()
        if aux!=None:
            return aux.getDato()
        else:
            return aux


