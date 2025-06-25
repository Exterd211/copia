import misFunciones1 as fc

opcion = ''
usuarios = {}
cupos_ninos = 1
cupos_adulto = 1

while opcion != '4':
    opcion = fc.menu()
    if opcion == '4':
        print('Programa Terminado.')
    elif opcion == '1':
        print('Matricular Nuevo Usuario')
        usuarios = fc.Comprar_entrada(usuarios)
        print(usuarios)
    elif opcion == '2':
        print('Cancelar Matrícula')
        usuarios = fc.cancelar_entrada(usuarios)
        print(usuarios)
    elif opcion == '3':
        print('Cupos disponibles')
        fc.buscar_(usuarios)
    else:
        print('Error: Opción NO Existe')

