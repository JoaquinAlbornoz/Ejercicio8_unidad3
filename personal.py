from abc import ABC

class personal(ABC):
    def __init__(self, cuil, ape, nom, sueldobasico, anti):
        self.__cuil = cuil
        self.__ape = ape
        self.__nom = nom
        self.__sueldobasico = sueldobasico
        self.__anti = anti
    def __gt__(self,other):
        if type(self)==type(other):
            if self.getape()!=other.getape():
                return self.getnom()>other.getnom()
            else:
                return self.getape()>other.getape()
        else:
            if self.getape()!=other:
                return self.getnom()>other
            else:
                return self.getape()>other

    def __str__(self):
        x = f'{self.__nom} {self.__ape} {self.__cuil} {self.__sueldobasico} {self.__anti}'
        return x

    def getnom(self):
        return self.__nom
    
    def getcuil(self):
        return self.__cuil

    def getape(self):
        return self.__ape

    def getsueldobasico(self):
        return self.__sueldobasico
    
    def set_sueldo_basico(self,s):
        self.__sueldobasico=s

    def getanti(self):
        return self.__anti

class docente(personal):
    __tipo='docente'
    __psimple=1.10
    __psemi=1.20
    __pex=1.50
    def __init__(self, cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra):
        super().__init__(cuil, ape, nom, sueldobasico, anti)
        self.__carre = carre
        self.__cargo = cargo
        self.__catedra = catedra

    @classmethod
    def gettipo(cls):
        return cls.__tipo

    def getcarrera(self):
        return self.__carre

    def getcargo(self):
        return self.__cargo
    @classmethod
    def set_cargo(cls,p):
        i=int(input('Ingrese cargo del 1 al 3:'))
        match i:
            case 1:
                cls.__psimple=p
            case 2:
                cls.__psemi=p
            case 3:
                cls.__pex=p


    def getsueldo(self):
        sueldo = self.getsueldobasico() * ((self.getanti() + 100) / 100)
        if self.__cargo == 'simple':
            sueldo += self.getsueldobasico() * self.__psimple
        elif self.__cargo == 'semiexcluisvo':
            sueldo += self.getsueldobasico() * self.__psemi
        elif self.__cargo == 'exclusivo':
            sueldo += self.getsueldobasico() * self.__pex
        return sueldo

class apoyo(personal):
    __tipo = 'apoyo'
    __ps=1.10
    __pse=1.20
    __pex=1.30
    def __init__(self, cuil, ape, nom, sueldobasico, anti, categoria):
        super().__init__(cuil, ape, nom, sueldobasico, anti)
        self.__categoria = categoria

    @classmethod
    def gettipo(cls):
        return cls.__tipo
    @classmethod
    def set_cargo(cls,p):
        i=int(input('Ingrese cargo del 1 al 3:'))
        match i:
            case 1:
                cls.__ps=p
            case 2:
                cls.__pse=p
            case 3:
                cls.__pex=p

    def getsueldo(self):
        categoria = int(self.__categoria)
        sueldo = self.getsueldobasico() * ((self.getanti() + 100) / 100)
        if categoria <= 10:
            sueldo += self.getsueldobasico() * self.__ps
        elif categoria <= 20 and categoria > 10:
            sueldo += self.getsueldobasico() * self.__pse
        elif categoria == 21 or categoria == 22:
            sueldo += self.getsueldobasico() * self.__pex
        return sueldo

class investigador(personal):
    __tipo = 'investigador'
    def __init__(self, cuil, ape, nom, sueldobasico, anti, areainv, tipoinv):
        super().__init__(cuil, ape, nom, sueldobasico, anti)
        self.__areainv = areainv
        self.__tipoinv = tipoinv

    def getareainv(self):
        return self.__areainv
    
    @classmethod
    def gettipo(cls):
        return cls.__tipo
    def getsueldo(self):
        sueldo = self.getsueldobasico() * ((self.getanti() + 100) / 100)
        return sueldo

class docenteinvestigador(docente, investigador):
    __tipo = 'docente investigador'
    def __init__(self, cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra, areainv, tipoinv, catprog, impextra, investigacion):
        docente.__init__(self, cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra)
        investigador.__init__(self, cuil, ape, nom, sueldobasico, anti, areainv, tipoinv)
        self.__catprog = catprog
        self.__impextra = impextra
        self.__investigacion = investigacion
    @classmethod
    def gettipo(cls):
        return cls.__tipo

    def getdatos(self):
        return f'{self.__cuil} {self.__ape} {self.__nom} {self.__sueldobasico} {self.__anti} {self.__carre} {self.__cargo} {self.__catedra} {self.__areainv} {self.__tipoinv} {self.__catprog} {self.__impextra} {self.__investigacion}'
        

    def getcarrera(self):
        return self.__carre
    def set_imp(self,o):
        self.__impextra=o
    
    @classmethod
    def set_cargo(cls,p):
        i=int(input('Ingrese cargo del 1 al 3:'))
        match i:
            case 1:
                cls.__psimple=p
            case 2:
                cls.__psemi=p
            case 3:
                cls.__pex=p

    def getsueldo(self):
        sueldo = self.getsueldobasico() * ((self.getanti() + 100) / 100) + self.__impextra
        if self.getcargo() == 'simple':
            sueldo += self.getsueldobasico() * self.__psimple
        elif self.getcargo() == 'semiexcluisvo':
            sueldo += self.getsueldobasico() * self.__psemi
        elif self.getcargo() == 'exclusivo':
            sueldo += self.getsueldobasico() * self.__pex
        return sueldo

    def getcatprog(self):
        return self.__catprog

    def getimpextra(self):
        return self.__impextra

