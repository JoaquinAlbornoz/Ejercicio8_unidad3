from manpersonal import lista
from personal import docente
from personal import apoyo
from personal import investigador
from personal import docenteinvestigador
from classinter import tesorero,director
def test(): 
    a = lista()
    a.instanciar()
    x = int(input('ingrese el numero de opcion: '))
    while x>0 and x<9:
        match x:
            case 1:
                indice = int(input('ingrese posicion para insertar elemento: '))
                print('ingrese los siguientes datos: ')
                tipo = input('tipo de personal: ')
                cuil = input('cuil: ')
                ape = input('apellido: ')
                nom = input('nombre: ')
                sueldobasico = int(input('sueldo basico: '))
                anti = int(input('antigÜedad: '))
                if tipo == 'docente':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    personal = docente(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra)
                elif tipo == 'apoyo':
                    categoria = input('categoria: ')
                    personal = apoyo(cuil, ape, nom, sueldobasico, anti, categoria)
                elif tipo == 'investigador':
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    personal = investigador(cuil, ape, nom, sueldobasico, anti, areainv, tipoinv)
                elif tipo == 'docenteinvestigador':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    catprog = input('categoría en el programa de incentivos de investigación: ')
                    impextra = int(input('importe extra por docencia e investigación: '))
                    investigacion = input('investigacion: ')
                    personal = docenteinvestigador(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra, areainv, tipoinv, catprog, impextra, investigacion)
                a.InsertarElemento(indice,personal)
            case 2:
                print('ingrese los siguientes datos: ')
                tipo = input('tipo de personal: ')
                cuil = input('cuil: ')
                ape = input('apellido: ')
                nom = input('nombre: ')
                sueldobasico = int(input('sueldo basico: '))
                anti = int(input('antigÜedad: '))
                if tipo == 'docente':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    personal = docente(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra)
                elif tipo == 'apoyo':
                    categoria = input('categoria: ')
                    personal = apoyo(cuil, ape, nom, sueldobasico, anti, categoria)
                elif tipo == 'investigador':
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    personal = investigador(cuil, ape, nom, sueldobasico, anti, areainv, tipoinv)
                elif tipo == 'docenteinvestigador':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    catprog = input('categoría en el programa de incentivos de investigación: ')
                    impextra = int(input('importe extra por docencia e investigación: '))
                    investigacion = input('investigacion: ')
                    personal = docenteinvestigador(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra, areainv, tipoinv, catprog, impextra, investigacion)
                a.AgregarElemento(personal)
            case 3:
                indice = int(input('ingrese posicion para mostrar elemento: '))
                a.mostrarElemento(indice)
            case 4:
                a.docinv()
            case 5:
                a.cont()
            case 6:
                a.most()
            case 7:
                a.catte()
            case 8:
                a.guarda()
            case 9:
                b = tesorero(l=a)
                j = b.optesorero()
                if j == False:
                    cuil=input('Ingrese cuil:')
                    b.gastosSueldoPorEmpleado(cuil)
            case 10:
                c=director(l=a)
                j=c.opdirector()
                op=int(input('1.Modificar basico\n2.Modificar porcentaje por cargo\n3.Modificar porcentaje por categoria\n4.Modificar importe extra.\nIngrese opcion deseada:'))
                while op==1 or op==2 or op==3 or op==4:
                    cuil=input('ingrese cuil')
                    match op:
                        case 1:
                            basico=float(input('ingrese nuevo basico:'))
                            c.modificarBasico(cuil,basico)
                        case 2:
                            b=float(input('ingrese nuevo porcentaje:'))
                            c.modificarPorcentajeporcargo(cuil,b)
                        case 3:
                            b=float(input('ingrese nuevo porcentaje:'))
                            c.modificarPorcentajeporcategoría(cuil,b)
                        case 4:
                            imp=float(input('ingrese nuevo importe:'))
                            c.modificarImporteExtra(cuil,imp)
                    op=int(input('1.Modificar basico\n2.Modificar porcentaje por cargo\n3.Modificar porcentaje por categoria\n4.Modificar importe extra.\nIngrese opcion deseada:'))


        x = int(input('ingrese el numero de opcion: '))

if __name__=='__main__':
    test()