# verificar si un numero es mayor que otro


print("----------------------------------")
print("------------MAYOR O MENOR---------")
print("----------------------------------")

#input
valor1 = int(input("INGRESE EL VALOR 1: "))
valor2 = int(input("INGRESE EL VALOR 2: "))
valor3 = int(input("INGRESE EL VALOR 3: "))
print("-------------------------------")
print("-------------------------------")

#condicion o validacion
print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if (valor1>valor2):
    r = valor1
else:
    r = valor2

if (r>valor3):
    print("El numero " + str(r) + " es el numero mayor de todos")
else:
    print("El numero " + str(valor3) + " es el numero mayor de todos")


print("-------------------------------")
print("-------------------------------")