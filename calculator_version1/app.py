def calcular(x,y,op):
    if op == 1: 
        return(x + y)
    elif op == 2:
        return(x - y)
    elif op == 3:
        return(x * y)
    elif op == 4:
        if y == 0:
            return "error no se puede dividir por 0)"
        return x / y
    elif op == 5:
        return(x**y)
    elif op == 6:
        return(x**0.5)
    elif op == 7 :
        return(x/y * 100)
    else:
        return("error operacion invalida")

on = True
while on == True:
    print("Calculadora version 1.1")
    print("escriba dos numeros")
    print("y luego escoja operacion deseada")
    while True:
        try:
            num1 = float(input("escriba el primer numero  "))
            num2 = float(input("escriba el segundo numero  "))
            break
        except ValueError:
            print("error ingrese solamente numeros")

    while True:
        print("Menu de operaciones disponibles")
        print("1 para suma")
        print("2 para resta")
        print("3 para multiplicacion")
        print("4 para division")
        print("5 para Potencias")
        print("6 para Raiz cuadrada")
        print("7 para Porcentaje")


        try:
            op = int(input("escriba operacion deseada  "))
            if op > 0 and op < 8:
                resultado = calcular(num1, num2, op)
                print(f"resultado {resultado:.2f}")
                break
            else:
                print("error ingrese un numero de operacion valido")

        except ValueError:
            print("error la operacion debe ser un numero en lista")

    while True :
        opcion = (input("presione 1 para Continuar, 0 para salir del programa: "))
        if opcion == "1": 
            break
        elif opcion == "0":
            on = False
            break
        else:
            print("opcion Incorrecta")



