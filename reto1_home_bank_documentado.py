# Diccionario que almacena los nombres de usuario y contraseñas
contraseñas = {'Axel' : 'ctn1', 'Paul' : 'ctn2'}

# Función para autenticar al usuario
def autenticar():
    # El usuario tiene 3 intentos para ingresar correctamente su nombre de usuario y contraseña
    for _ in range(3):
        username = input('Ingrese su nombre de usuario: ')
        contraseña = input('Ingrese su contraseña: ')
        # Si el nombre de usuario y la contraseña son correctos, la función retorna el nombre de usuario
        if username in contraseñas and contraseñas[username] == contraseña:
            return username
        print('Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.')
    # Si el usuario falla 3 veces, la función retorna None
    print('Demasiados intentos fallidos. Por favor, inténtelo más tarde.')
    return None

# Diccionario que almacena los nombres de usuario y sus saldos
saldos = {'Axel' : 2000, 'Paul' : 2000}

# Función para depositar dinero en la cuenta del usuario
def depositar(username):
    # El usuario debe ingresar un número entero positivo
    while True:
        cantidad = input('Ingrese la cantidad a depositar: ')
        # Si la cantidad es un número entero positivo, se rompe el bucle
        if cantidad.isdigit() and int(cantidad) > 0:
            break
        print('Entrada inválida. Por favor, ingrese un número entero positivo.')
    saldos[username] += int(cantidad)
    print(f'Depósito exitoso. Su nuevo saldo es {saldos[username]}')

def retirar(username):
    while True:
        cantidad = input('Ingrese la cantidad a retirar: ')
        if cantidad.isdigit() and int(cantidad) > 0 and int(cantidad) <= saldos[username]:
            break
        print('Entrada inválida o saldo insuficiente.')
    saldos[username] -= int(cantidad)
    print(f'Retiro exitoso. Su nuevo saldo es {saldos[username]}')

def consultar_saldo(username):
    print(f'Su saldo es {saldos[username]}')

def transferir(username_origen):
    username_destino = input('Ingrese el nombre de usuario destino: ')
    if username_destino not in saldos:
        print('El usuario no registrado')
        return
    while True:
        cantidad = input('Ingrese la cantidad a transferir: ')
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad > 0 and cantidad <= saldos[username_origen]:
                break
            elif cantidad > saldos[username_origen]:
                print('Saldo insuficiente.')
    saldos[username_origen] -= cantidad
    saldos[username_destino] += cantidad
    print(f'Transferencia exitosa. Su nuevo saldo es {saldos[username_origen]}')

username = autenticar()
if username is None:
    exit()

while True:
    print('1. Depositar')
    print('2. Retirar')
    print('3. Ver saldo')
    print('4. Transferir')
    print('5. Salir')
    opcion = input('Seleccione una opción: ')
    if opcion == '1':
        depositar(username)
    elif opcion == '2':
        retirar(username)
    elif opcion == '3':
        consultar_saldo(username)  
    elif opcion == '4':
        transferir(username)
    elif opcion == '5':
        print('Gracias por utilizar nuestros servicios.')
        break
    else:
        print('Opción no válida. Inténtelo de nuevo.')