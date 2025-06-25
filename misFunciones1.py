def menu():
    print('Menú De compra para el conejo simpatico')
    print('~'*20)
    print("""
    1.- Comprar entrada.
    2.- Cancelar Compra.
    3.- Buscar Compra.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op

def validar_codigo_verificacion(contraz):
    Ma = any(c.isupper() for c in contraz)
    Nro = any(c.isdigit() for c in contraz)
    Sin = ' ' not in contraz
    return len(contraz) == 6 and Ma and Nro and Sin

def Comprar_entrada(diccentra):
        while True:
            nombre = input('Ingrese nombre del comprador: ')
            if nombre.replace(' ','').isalpha():
                break
            else:
                print('El nombre solo debe contener letras. Intente nuevamente')
        
        while True:
            tipo = input('Ingrese tipo de entrada [G: General / V: Vips]: ').upper()
            if tipo == 'G' :
                break
            elif tipo == 'V' :
                break
            else:
                print('Tipo invalido .Intente Nuevamente')
        while True:
            contraseña = input('Ingrese código de verificación: ')
            if validar_codigo_verificacion(contraseña):
                break
            else:
                print('Codigo no valido. Debe teneer 6 caracteres, al menos 1 mayuscula, 1 numero y sin espacios.')
        diccentra[nombre] = [tipo, contraseña]  
        
        print(f'Compra realizada con exito! {nombre}')      
        return diccentra

def cancelar_entrada(diccentra):
    nombre = input('Ingrese el nombre del titular a cancelar: ').strip()
    if nombre in diccentra:
        diccentra[nombre][0]
        del diccentra[nombre]
        print('Compra Cancelada correctamente!')
    else:
        print(f'No se encuentra el nombre con una entrada  ')
    return diccentra 
def buscar_(diccentra):
    if not diccentra:
        print("No hay contactos guardados.")
        return
    
    nombre = input("Ingrese el nombre a buscar: ").strip()
    if nombre in diccentra:
        print(f"usuario encontrado: {nombre}")
    else:    
        print(" Contacto no encontrado.")

    
