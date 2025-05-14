import os

def clear_console():
    os.system('cls' if os.name== 'nt' else 'clear')

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

name= "Victor Galvez"
city = "Santo Domingo"
print(f"Hola Mi nombre es {name}.\nActualmente estoy viviendo en la ciudad: {city}.")

input("\nPresiona Enter para continuar...")
clear_console()

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"El primier dato es {a} y su tipo de datos es {type(a)}")
print(f"El Segundo dato es {b} y su tipo de datos es {type(b)}")
print(f"El Tercero dato es {c} y su tipo de datos es {type(c)}")
print(f"El Cuarto dato es {d} y su tipo de datos es {type(d)}")
print(f"El quinto dato es {e} y su tipo de datos es {type(e)}")

input("\nPresiona Enter para continuar...")
clear_console()

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

str = 12345
print(f"La cadena es {str}, ahora sera un entero {int(str)}, pero ahora sera un decimal {float(str)}")

float = 3.99
print(f"Este es el decimal: {float}, y asi cuando esta en entero: {int(float)}, lo que pasa es que se eliminan los numeros despues del punto.")

input("\nPresiona Enter para continuar...")
clear_console()

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

name = "Victor"
age = 22
height = 1.68

print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros")

input("\nPresiona Enter para continuar...")
clear_console()

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)

input("\nPresiona Enter para continuar...")
clear_console()