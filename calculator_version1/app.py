def calcular(x,y,op):
    if op == 1: 
        return(x + y)
    elif op == 2:
        return(x - y)
    elif op == 3:
        return(x * y)
    elif op == 4:
        return(x / y)
    else:
        return("error operacion invalida")

print("Calculadora version 1")
print("escriba dos numeros")
print("y luego escoja operacion deseada")
num1 = float(input("escriba el primer numero  "))
num2 = float(input("escriba el segundo numero  "))
print("Menu de operaciones disponibles")
print("1 para suma")
print("2 para resta")
print("3 para multiplicacion")
print("4 para division")
op = int(input("escriba operacion deseada  "))

resultado = calcular(num1,num2,op)
print (f"el resultado es {resultado}")
