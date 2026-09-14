total = int(0)
ticket = []
hamburguesa = 4500
papas = 2000
bebida = 1500
while True:
    print("------------------------------")
    print("Bienvenido, Nuestro Menu: ")
    print("------------------------------")
    print("1) Agregar hamburguesa")
    print("2) Agregar papas fritas")
    print("3) Agregar bebida")
    print("4) Pagar")
    print("5) cancelar pedid0")

    opcion = int(input("Seleccioná una opción (1 - 4): "))
    while not opcion:
        opcion = int(input("Seleccioná una opción (1 - 4): "))

    match opcion:
        case 1: 
            print("Agregar Hamburguesa")
            print("Precio de la hamburguesa: 4500")
            total += hamburguesa
            ticket.append(f"hamburguesa:{hamburguesa}")
            print(f"Precio actual:{total} ")

        case 2:
            print("Agregar Papas fritas")
            print("Precio de las papas: 2000")
            total += papas
            ticket.append(f"papas:{papas}")
            print(f"Precio actual:{total} ")

        case 3:                 
            
            print("Agregar Bebida")
            print("Precio de la bebida: 1500")
            total += bebida
            ticket.append(f"bebida: {bebida}")
            
            print(f"Precio actual:{total} ")

        case 4:
            print("confirmar pago:")
            print(f"Su pedido: {ticket}")
            efectivo = input(f"El total a pagar es {total},ingrese el pago: ")

            while not efectivo.isdigit():
                  efectivo = input(f"Error,ingrese solo numero,el total a pagar es {total},ingrese el pago: ")

            efectivo = int(efectivo)
            while efectivo < total:
                 efectivo = int(input(f"El total a pagar es {total},ingrese el pago correcto: "))
            vuelto = efectivo - total 
            print(f"Perfecto,su vuelto es de {vuelto}")
            total = 0
            ticket = []

        case 5: 
            print("Orden finalizada")
            break   

        case _:
            print("invalido")
