"""
Funciones definidas por el usuario
"""

# Simples

def hellou():
    print("hola, david")

hellou()

#Con Un Retorno 

def retorn():
    return "hola, david"

variable = retorn()
print(variable)

# Con un Argumento

def argumento(name):
    print(f"hola, {name}")

argumento("david")

# Con Argumentos

def argumento(name, years, ciu):
    print(f"hola, {name} tienes {years} años y vives en {ciu}")

argumento("david", "22", "Cabudare")


# Con un Argumento Predeterminado

def defaul_argumento(name="David,", years=22, ciu="Cabudare"):
    print(f"hola, {name}, tienes {years}, y vives en {ciu}")

defaul_argumento()

# Con Argumento y Retorno

def retorno_argumento(years, name):
    return f"{years}, {name}"

print(retorno_argumento(22, "david"))

# Retorno con varios valores

def multiple_retorno():
    return 22, "david"

years, name = multiple_retorno()
print(years)
print(name)

# Con un numero variable de argumentos

def variable_argumentos(*names):
    for name in names:
        print(f"hola, {name}")

variable_argumentos("David", "Alejandro", "epicdeivid")

"""
Funciones dentro de funciones
"""

def otra_funcion():
    def funcion_interna():
        print("hola soy una funcion interna :=)")
    funcion_interna()

otra_funcion()

"""
Funciones del lenguaje (built-in)
"""

print(len("MoureDev"))
print(type(36))
print("david".upper())

"""
Variables locales y globales
"""

variable_gobal = "david"

def ejemplo():
    variable_local = "hola"
    print(f"{variable_local} como estas {variable_gobal}")

ejemplo()