
"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion_ejemplo(numero_1, numero_2) -> int:
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
         print(f"esta es la primera cadena {numero_1}, y esta la segunda cadena {numero_2}")
        elif numero % 3 == 0:
         print(numero_1)
        elif numero % 5 == 0:
           print(numero_2)
        else:
           print(numero)
           contador += 1
    return contador

print(funcion_ejemplo("numero_1", "numero_2"))