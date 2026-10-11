from datetime import datetime

cuentas = []
consecutivo = 1

def crear_cuenta():
    global consecutivo
    anio = datetime.now().year
    codigo = str(anio) + "-" + str(consecutivo)
    consecutivo += 1
    identificacion = input("Identificación: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo: ")
    saldo = float(input("Saldo inicial: "))
    fecha = datetime.now().strftime("%Y-%m-%d")
    cuenta = {
        "codigo": codigo,
        "fecha": fecha,
        "saldo": saldo,
        "identificacion": identificacion,
        "nombre": nombre,
        "correo": correo
    }
    cuentas.append(cuenta)
    print("Cuenta creada:", codigo)

def buscar_codigo(codigo):
    for c in cuentas:
        if c["codigo"] == codigo:
            return c
    return None

def consignar():
    codigo = input("Código de cuenta: ")
    c = buscar_codigo(codigo)
    if c:
        monto = float(input("Monto a consignar: "))
        c["saldo"] += monto
        print("Nuevo saldo:", c["saldo"])
    else:
        print("Cuenta no encontrada")

def retirar():
    codigo = input("Código de cuenta: ")
    c = buscar_codigo(codigo)
    if c:
        monto = float(input("Monto a retirar: "))
        if monto <= c["saldo"]:
            c["saldo"] -= monto
            print("Nuevo saldo:", c["saldo"])
        else:
            print("Saldo insuficiente")
    else:
        print("Cuenta no encontrada")

def consultar_codigo():
    codigo = input("Código de cuenta: ")
    c = buscar_codigo(codigo)
    if c:
        print(c)
    else:
        print("Cuenta no encontrada")

def consultar_identificacion():
    identificacion = input("Identificación del cliente: ")
    encontrados = []
    for c in cuentas:
        if c["identificacion"] == identificacion:
            encontrados.append(c)
    if encontrados:
        for c in encontrados:
            print(c)
    else:
        print("No hay cuentas para esa identificación")

def listar():
    if cuentas:
        for c in cuentas:
            print(c)
    else:
        print("No hay cuentas")

while True:
    print("MENÚ BANCO ADSO 3229426")
    print("1. Crear Cuenta")
    print("2. Consignar Cuenta")
    print("3. Retirar Cuenta")
    print("4. Consultar Cuenta Por Código")
    print("5. Consultar Cuenta por Identificación Cliente")
    print("6. Listar Cuentas")
    print("7. Salir")
    opcion = input("Ingrese Opción (1-7): ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        consignar()
    elif opcion == "3":
        retirar()
    elif opcion == "4":
        consultar_codigo()
    elif opcion == "5":
        consultar_identificacion()
    elif opcion == "6":
        listar()
    elif opcion == "7":
        break
    else:
        print("Opción inválida")