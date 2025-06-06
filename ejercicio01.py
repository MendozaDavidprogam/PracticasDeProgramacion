"""
operadores
"""

# Operadores aritmeticos
print(f"suma de 10 + 10 es igual a : {10 + 10}") # Suma
print(f"resta de 10 - 5 es igual a : {10 - 5}") # Resta
print(f"division de 20 / 2 es igual a : {20 / 2}") # Division
print(f"multiplicacion de 10 * 10 es igual a : {10 * 10}") # Multiplicacion
print(f"modulo de 20 % 2 es igual a : {20 % 2}") # Modulo  Nota: es lo qu queda de la division
print(f"exponente de 10 ** 2 es igual a : {10 ** 2}") # Exponente
print(f"division entera de 20 // 3 es igual a : {20 // 3}") # Division entera

# Operadores de comparacion
print(f"igualdad 10 == 2 es: {10 == 2}") # Igualdad
print(f"desigualdad 10 != 2 es: {10 != 2}") # Desigualdad
print(f"mayor 10 > 2 es: {10 > 2}") # Mayor
print(f"menor 10 < 2 es: {10 < 2}") # Menor
print(f"mayor o igual que 10 >= 11 es : {10 >= 11}") #Mayor igual que 
print(f"menor o igual que 10 <= 11 es : {10 <= 11}") #Menor igual que 

# Operadores logicos
print(f"AND o &&: 20 + 5 == 25 AND 5 - 2 == 3 : {20 + 5 == 25 and 5 - 2 == 3}")
print(f"OR o ||: 20 + 5 == 25 AND 5 - 2 == 3 : {20 + 5 == 25 or 5 - 2 == 3}")
print(f"NOT o !: 10 + 5 == 14 : {not 10 + 5 == 14}")

# Operadores de asignacion
number = 10 # Asignacion
print(number)
number += 1 # Suma y Asignacion
print(number)
number -= 1 # Resta y Asignacion
print(number)
number *= 2 # Multiplicacion y Asignacion
print(number)
number /= 2 # Division y Asignacion
print(number)
number %= 2 # Modulo y Asignacion
print(number)
number **= 1 # Exponente y Asignacion
print(number)
number //= 2 # Division En y Asignacion
print(number)

# Operadores de identidad
my_number = number
print(f"my_number is number: {my_number is number}")
print(f"my_number is not number: {my_number is not number}")

# Operadores de pertenencia

print(f"'d' in 'david' {'d' in 'david'}")
print(f"'b' in 'david' {'b' not in 'david'}")

"""
estructuras de control
"""

# Condicionales 

my_Name = "David"

if my_Name == "David":
    print("Welcomen David")
else:
    print("you are not David")

# Interativas

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i += 1


# Manejo de exepciones
try:
    print(10/0)
except:
    print("error no se puede dividir entre 0:")
finally:
    print("ha finalizado el manejo de errores")