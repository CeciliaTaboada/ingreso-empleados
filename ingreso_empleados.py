import time

def comprobar(dato):
    while dato == '':
        print('ocurrio un error')
        dato = input('ingrese el dato nuevamente')
    return dato

def guardar(persona, tipo):
    fecha = time.asctime()
    datos = f'{fecha} - {persona} - {tipo} \n'
    f = open('registro.txt', 'a')
    f.write(datos)
    f.close()

def mostrar():
    try:
        f = open('registro.txt', 'r')
        eventos = f.readlines()
        f.close()
        if len(eventos) < 5:
            for r in eventos:
                print(' - '+ r.strip())
        else:
            for r in eventos[-5:]:
                print(' - '+ r.strip())
    except FileNotFoundError:
        print('No hay registros para mostrar')

while True:
    print('Menú\n1)Ingreso de empleado\n2)Egreso de empleado\n3)Ver los ultimos 5 registros\n4)Salir del sistema')
    opcion=input('>>>')
    match(opcion):
        case '1':
            nombre = input('nombre del empleado que ingresa: ')
            nombre = comprobar(nombre)
            guardar(nombre, 'ingreso')
        case '2':
            nombre = input('nombre del empleado que egresa: ')
            nombre = comprobar(nombre)
            guardar(nombre, 'egreso')
        case '3':
            print("-" * 8 +" Los últimos 5 registros " + "-" * 8 +"\n")
            mostrar()
            print("\n"+"-" * 40)
        case '4':
            print('Gracias por usar nuestro programa!')
            break
        case _:
            print('error de opcion'+ '\n\n'+ 'toque ENTER para continuar')
