especialidades= [] 
cupos= [] 


while True: 
    print("----------------------")
    print("menú clínica")
    print("----------------------")
    print("1.Ingresar lista de especialidades")
    print("2.Ingresar lista de cupos disponibles por especialidad ")
    print("3.Mostrar agenda")
    print("4.Consultar cupos de una especialidad ")
    print("5.Listar especialidades sin cupo")
    print("6.Agregar especialidad ")
    print("7.Actualizar cupos (reservar / cancelar) ")
    print("8.Salir ")


    indice = input("Que le gustaria hacer (1-8): ")
    while not indice.isdigit() or int(indice) < 1 or int(indice) > 8:
        indice = input("Error. Ingrese una opcion valida (1-8): ")
    

    match indice:

        case "1":
            print("Ingresar lista de especialidades")
        

            cantidad = input("ingrese cuantas especialidades tiene:")
            while not cantidad.isdigit():
                 cantidad = input("ingrese cuantas especialidades tiene (solo numeros):")
            cantidad = int(cantidad)


            for i in range(cantidad):
                especialidad = input("Ingrese que especialidad ofrece la clinica: ").lower().replace(" ", "")
                while not especialidad.isalpha() or especialidad in especialidades:
                    especialidad = input("Ingrese una respuesta valida y que no este repetida: ").lower().replace(" ", "")
                especialidades.append(especialidad)

            print("Especialidades guardadas.")

        case "2":
            print("Ingresar lista de cupos disponibles por especialidad.")

            for i in (especialidades):
                cupo = input(f"Ingrese la cantidad de cupos disponibles para {i}:")

                while not cupo.isdigit():
                    cupo = input(f"Ingrese la cantidad de cupos disponibles para {i+1} (solo numeros)")
                cupo = int(cupo)
                cupos.append(cupo)

            print("Cupos guardados.")

        case "3":
            print("Agenda disponible:")
            for i in range(len(especialidades)):
                print(f"{especialidades[i]} tiene {cupo[i]} cupos.")

           
        case "4":

            disponibilidad = input("Ingrese el nombre de la especialidad: ").lower().replace(" ", "")
            while disponibilidad not in especialidades or  not disponibilidad.isalpha():
                print("Error. Especialidad no disponible.")     
                disponibilidad = input("Ingrese el nombre de la especialidad: ").lower().replace(" ", "")
            lugar_cupo = especialidades.index(disponibilidad)

            if cupos[lugar_cupo] == 0:
                 print("No hay cupos disponibles.")
            else:
                print(f"{disponibilidad} tiene {cupos[lugar_cupo]} cupos dispobibles para {disponibilidad}.")

        case"5":
              print("Especialidades sin cupo: ")

              especialidades_sin_cupo = []

              for i in range(len(cupos)):
                   if cupos[i] == 0:
                        especialidades_sin_cupo.append(especialidades[i])
            
              print(f"especialidades sin cupo:{especialidades_sin_cupo} ")

        case "6":
              print("Agregar especialidad")

              especialidad = input("Ingrese que especialidad quiere agregar: ").lower().replace(" ", "")
              while not especialidad.isalpha() or especialidad in especialidades:
                especialidad = input("Ingrese que especialidad quiere agregar (solo letras): ").lower().replace(" ", "")

              cupo = input(f"Ingrese la cantidad de cupos disponibles para {especialidad}:")

              while not cupo.isdigit():
                cupo = input(f"Ingrese la cantidad de cupos disponibles para {i+1} (solo numeros)")

              cupo = int(cupo)
              especialidades.append(especialidad)
              cupos.append(cupo)
              print("Especialidad agregada!")

        case "7":
            print("Actualizar cupos (reservar / cancelar) ")

            opcion = input("Si quiere resevar (1),quiere cancelar(2): ")
            while not opcion.isdigit():
                opcion = input("Si quiere resevar(1),quiere cancelar(2): ")

            if opcion == "1":
                especialidad = input("que especialidad le gustaria reservar: ").lower().replace(" ", "")
                while not especialidad.isalpha() or especialidad not in especialidades:
                    especialidad = input("que especialidad le gustaria reservar: ").lower().replace(" ", "")

                if especialidad in especialidades:
                    lugar = especialidades.index(especialidad)
                    if cupos[lugar] <= 0:
                        print(f"No hay cupos disponibles para {especialidad}")
                    else: 
                        cupos[lugar] -= 1
                        print("Usted ha reservado un turno!")

            if opcion == "2":
                especialidad = input("que especialidad le gustaria cancelar: ").lower().replace(" ", "")
                while not especialidad.isalpha() or especialidad not in especialidades:
                    especialidad = input("que especialidad le gustaria cancelar: ").lower().replace(" ", "")
                
                if especialidad in especialidades:
                    lugar = especialidades.index(especialidad)
                    cupos[lugar] += 1

                print("Usted ha cancelado su turno!")

        case "8":
            print("Ha finalizado la sesión. Gracias!")
            break



        