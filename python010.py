#TUPLAS
#Construir una tuplas vacia
jugadores = ()
#Construir una lista con valores
jugadores2 = ('Ronaldo','Messi','Griezman',('Garnacho','Cisneros','Palmer'))
#Construir una lista mediante su constructor
jugadores3 = tuple(('Diaz','Caicedo','Scholes'))

#funcion len() para imprimir cantidad de elemento de la tupla
print(len(jugadores)) #[]-->0
print(len(jugadores2)) #3
print(len(jugadores3))#3

#Para conocer el tipo de la tupla
print(type(jugadores))#clase list

#Como colocar el dato de una tupla
print(jugadores2[3][1])

#Seleccion por rango
print(jugadores2[0:3])

#Cambio de valores en tupla
jugadores2 = list((jugadores2))
jugadores2[0] = 'Salah'
print(jugadores2)

#Cambio por rango
jugadores3 = list((jugadores3))
jugadores3[:] =('Yamal', 'Pedri','Paez')
print(jugadores3)

#Agregar un elemento al finla de la tupla
jugadores3.append('Embappe')
print(jugadores3)

#Agregacion mediante indice
jugadores3.insert(1,'Hincapie')
print(jugadores3)

jugadores4 = ['Dembele','Modric','Nico Willians','Caicedo']
lista_completa = jugadores3 + jugadores4
lista_completa = tuple((lista_completa)) # transformar a una tupla
print(lista_completa, type(lista_completa))

#Eliminar un elemento de la tupla
lista_completa = list((lista_completa))
lista_completa.remove('Nico Willians')#Eliminado a niko
print(lista_completa)
lista_completa.pop(5)#Eliminando a Dembele
lista_completa = tuple((lista_completa))
print(lista_completa, type(lista_completa))

#Vaciar la lista
#lista_completa.clear()

#Eliminar la lista  
#del lista_completa