while True: 
    temp = input("Ingrese temperatura (ponga fin para salir): ").lower()

    match temp:
        case "fin":
                    print("fin del programa")
                    break
        case _: 
            if temp.count(".")> 1:
                print("error")
                continue

            if temp == "" or temp == ".":
                print("error")
                continue

            valido = True 
            for c in temp: 
                if c.isdigit() == False and c != ".":
                    valido = False

            if valido == False: 
                print("error")
                continue

            temp = float(temp)
            print(f" temperatura registrada: {temp}")

            if temp < 100.0 or temp > 500.0:
                print("temperatura fuera de rango")
