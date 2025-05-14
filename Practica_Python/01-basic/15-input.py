#05 - Entrda de usuarios (input()) - Versiones simplificada
#La funcion input() permite obtener datos del usuario a traves de la consola

print("Hola, Como te llamas?")
nombre = input()

print(f"Hola {nombre}, espero que te lo estes pasando bien")

#Otra forma mas directa
nombre = input("Hola, Como te llamas? ")
print(f"Hola {nombre}, espero que te lo estes pasando bien")

#El input siempre devolvera una cadena de texto, por lo mismo hay que transformar el dato dado por el input, antes de realizar operaciones con ellos
edad = input("Hola, Cual es tu edad? ")
print(f"En 5 años tendras: {int(edad) + 5}")

# La función input() también puede devolver múltiples valores
# Para hacerlo, el usuario debe separar los valores con una coma
country, city = input("Cual es tu pais y en que ciudad?\n").split()
print(f"Vives en {country}, {city}")
# Esto solo sirve por palabras, o sea que si dejas espacios entre palabras y solo tienes dos variables, pues dara error, o sea no se puede poner Republica Dominicana
# y Santo Domingo, ya que solo tiene dos variables y se guardan los datos por palabras, por lo mismo se tendria que agregar dos variables mas para que no hayan problemas.

