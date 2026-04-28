#CONJUNTOS --->SETS
frutas = {}
frutas2 = {'PIña','Durazno','Melocoton'}
frutas3 = set(({'Mora','Durazno','Fresa'}))
cadena = 'Hola coders'
c = set(cadena)
print(c)
print(frutas2)

numeros = {1,1,2,2,3,4,5,6,6,7,8,8,9,10}
print(numeros)

#For para recorrer valores de un conjunto
for n in numeros:
    print(n)

if(11 in numeros):
    print(f'existe en:{numeros}')
else:
    print(f'No existe en {numeros}')

frutas2.add("Sandia")
print(frutas2)

frutas2.update(frutas3)
print(frutas2)

frutas4 = ['Limon', 'Manzana','Banana','Uva']
frutas2.update(frutas4)
print(frutas2)

bandera = True
while bandera:
    frutas2.pop() #elimina una fruta al aLeatoria
    opc = (input('Desean salir de la app [s/n]:'))
    if opc == 's':
        bandera = False
    else:
         print(frutas2)