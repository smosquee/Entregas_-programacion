
saldo_inicial = int(50000)
while True: 
    
    print("------------------------------")
    print("Cajero Automatico")
    print("------------------------------")
    print("1) Consultar saldo")
    print("2) Ingresar dinero")
    print("3) Retirar dinero")
    print("4) Salir")


    opcion = input("Seleccioná una opción (1 - 4): ")
    while not opcion:
        opcion = input("Seleccioná una opción (1 - 4): ")


    match opcion: 
        case 1:
            print("consultar saldo")
            print(f"Su saldo actual es de {saldo_inicial}")

        case 2:
            print("Ingresar dinero")
            ingreso = input("Cuanto dinero desea ingresar: ")
            while not ingreso:
                ingreso = input("Cuanto dinero desea ingresar: ")
            ingreso = int(ingreso)
            saldo_inicial += ingreso
            print(f"El saldo queda en {saldo_inicial}")

        case 3: 
            print("Retirar dinero")
            retiro = input(f"Cuanto dinero desea retirar (saldo actual de: {saldo_inicial}): ")
            while not retiro:
                retiro = input(f"Cuanto dinero desea retirar (saldo actual de: {saldo_inicial}): ")
            retiro = int(retiro)
            if retiro > saldo_inicial: 
                print("saldo insuficiente")
            else:
                saldo_inicial -= retiro
                print(f"El saldo queda en {saldo_inicial}")

        case 4: 
            print("El programa ha finalizado.")
            break

