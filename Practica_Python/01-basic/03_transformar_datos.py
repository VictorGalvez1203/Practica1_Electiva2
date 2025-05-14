#03-casting of types
#Transformar un tipo a otro

print("Conversion de tipos")
print(type(int("100")))

print(int("300")+ 2)

print("Esto se esta concatenando")
print("300" + str(2))

print(type(float("3.1416")))

print("Poner un decimal en entero")
print(int(3.1416))

print("Transformar numero a booleanos")
print(bool(2))
print(bool(0))
print(bool(-5))
#Cualquier numero sera true sin importar si es negativo o negaivo, menos el cero, ese es el unico que sera false 

print("Transformar cadena de texto a booleanos")
print(bool(""))
print(bool(" "))
print(bool("false"))
#Lo mismo pasa aqui, la unica que entregara false es la cadena de texto vacia.

print("Metodo para redondear numeros decimales o float")
print(round(11.5))
#Ese metodo de 'round' redondea al par mas cercano, o sea que si tengo 2.5 sera 2 y si tengo 11.5 sera 12