#funciones
#realizar un menu calculadora, pide ingresar dos numero y luego seleccionar la operacion que desea

def mostrarOpciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    operacion = input("seleccione la opcion: ")
    return operacion
def sumar(num1,num2):
    print(f"La operacion de la suma es: {num1+num2} ")
    
def restar(num1,num2):
    print(f"La operacion de la resta es: {num1-num2}")
    
def multiplicar(num1,num2):
    print(f"La operacion de la multiplicacion es: {num1*num2} ")
    
def dividir(num1,num2):
    print(f"La operacion de la division es {num1/num2}")
    
operacion= ""
while operacion != "5":
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print("Selecciona la opcion que deseas")
    operacion = mostrarOpciones()
    if operacion == "1":
        sumar(num1,num2)
    if operacion == "2":
        restar(num1,num2)
    if operacion == "3":
        multiplicar(num1,num2)
    if operacion == "4":
        dividir(num1,num2)
        
#############################################################################
#realizar una calculadora de dos cifras
#donde el usuario ingrese la operacion que desea
# input => 20*5
# print => 100
#vacia esperando una nueva operacion hasta que escribamos salir sea en mayusculas minuscular o mixtas

def menu():
    operacion= ""
    while operacion != "salir".lower(): #creo menu
        print("Ingrese una operacion matematica (ej 2+4, 2*4, 2/4 ,etc)")
        operacion = input("Escriba: ") #ingreso por consola la operacion
        numero = "" #variable vacia que almacena numero
        for caracter in operacion: #itero cada letra o caracter de la expresion
            if caracter.isdigit(): # si es un numero
                numero += caracter #lo guardo y acumulo
            if not caracter.isdigit(): #si no es un numero
                operador = caracter # obtengo el operador
                num2 = numero #guardo anterior numero
                numero = "" #limpio para guardar el segundo numero
        if operador == '+':
            print(f"el resultado es {int(num2)+int(numero)}")   
        if operador == '-':
            print(f"el resultado es {int(num2)-int(numero)}") 
        if operador == '*':
            print(f"el resultado es {int(num2)*int(numero)}") 
        if operador == '/':
            print(f"el resultado es {int(num2)/int(numero)}")      
        
    
menu()

#############################################################################
#realizar una calculadora de dos cifras
#donde el usuario ingrese la operacion que desea
# input => 20*5
# print => 100
#vacia esperando una nueva operacion hasta que escribamos salir sea en mayusculas minuscular o mixtas
#utliizar funciones, bucles, condicionales, todo tipos de variables

"""
practicando a mi manera
def operacion():
    def sumar(num1,num2):
        return num1+num2
    def restar(num1,num2):
        return num1-num2
    def multiplicar(num1,num2):
        return num1*num2
    def dividir(num1,num2):
        if num2 != 0:
            return num1/num2
        else:
            return "Error: No se puede dividir entre cero"""