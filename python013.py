#Creacion de un diccionario
luchador = {
    "nombre":"john Cena",
    "edad" : 43,
    "peso":114,
    "altura":1.85,
    "campeon_actual": True,
    "campeon_anteriores":{"WHE Championship"},
    "retirado":False,
}
#Segunda opcion para crear un diccionario
luchador2 = dict(nombre ='Rey Misterio', edad ='36', peso = '1.70 ',altura = '1.70',campeon_actual = False,retirado = False)


#impresion de un diccionario completo
print(luchador)

#Recorrer diccionario mediante clave luchador
for clave,valor in luchador.items():
    print(f'{clave:}-->{valor}')

#Recorrerdiccionario mediante clave
for clave in luchador:
    print(f'{clave}-->{luchador[clave]}')

#Recorrer diccionario2 mediante clave valor
for clave,valor in luchador2.items():
    print(f'{clave}-->{valor}')

#Aceeso a un valor del diccionario luchador
print('Luchador de la WWE',luchador['nombre'])

#Acceso a un valor del diccionario mediante el metodo get
print('Luchador de la WWE: ',luchador.get('nombre'))

#Acceso solo a claves del diccionario luchador
print('claves del diccionario luchador',luchador.keys())

#Acceso solo a valores del diccipnario luchador
print('Valores de diccionario luchador: ',luchador.values())

#Accesos a todos los elemento del diccionario del luchador
print('Elementos del diccionario del luchador; ',luchador.items())


#Modificar un valor del diiccionario luchador
luchador['nombre'] = 'Gran Kali'
luchador['altura'] = 2.20
print(luchador) #Datos actuales del diccionario luchador

#Modifcar un valor del diccionario luchador2 mediante el metodo update
luchador2.update({'nombre':'The Rock','peso':118,'altura':1.96})
print(luchador2)

#Añadir un nuevo key y value al diccionario luchador
luchador['vivo'] = True
print(luchador) #Datos actuales del diccionario luchador

#Añadir un nuevo key y value al diccionario luchador2 mwediante el metodo update
luchador2.update({'vivo':True})
print(luchador2)#Datos actuales del diccionario luchador2

#Eliminar un key y su values del diccionario luchador
luchador.pop('campeon_actual')
print(luchador)#Datos actuales del diccionario luchador

#Eliminar un key y su value del diccionario luchador2 mediante el metodo del
del luchador2['campeon_actual']
print(luchador2)#Datos actuales del diccionrio luchador2

#Eliminar el ultimo key y su value del diccionario luchador mediante el metodo popitem
luchador.popitem()
print(luchador)#Datos actuales del diccionrio luchador

#Eliminar el ultimo key y su value del diccionario luchador2 mediante el metodo popitem
luchador2.popitem()
print(luchador2)#Datos actuales del diccionrio luchador2

#Eliminar todos los elementos del diccionario luchador mediante el metodo clear
luchador.clear()
print(luchador)#Datos actuales del diccionario luchador