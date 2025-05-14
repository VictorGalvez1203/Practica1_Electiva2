#o4 - Variables
#Las variables sirven para guardar datos en memoeria
#Python es un lenguaje de tipado dinamico y de tipado fuerte

#Asignar una variables
#Solo hace falta poner el nombre que le daremos a la variables y el dato
my_name = "Victor"
print(my_name)

#Las variables pueden tener el mismo nombre y no habra problema
age = 20
print(age)

age = 22
print(age)

#Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
#que no tienes que declararlo explicitamente
name = "victor"
print(type(name))

name = 22
print(type(name))

#Tipado fuerte: python no realiza conversion de tipo automatico
#print(10+"2")

#Pero si podemos formatear una cadena literal
#f-string (literal de cadena de formato)
print(f"Hola soy {my_name} y tengo actualemnte {age} años de edad.")


#Conversiones de nombres de variables
mi_nombre_de_variables = "ok" #snake_case
nombre = "ok"

#Escribir el nombre de la variables en mayuscula o UPPER_CASE, para indicar que es una constante, o sea es una variables normal, solo es para poder diferencial. 
MI_CONSTANTE = 3.14 #UPPER_CASE -> constantes


#Todas las palabras recervadas de python

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally', 
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield']