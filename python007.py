from decimal import Decimal
mensaje = " PYTHON FLASK"
#slicing --> rebanadas
print(mensaje[7:11])#s
print(mensaje[7:])#k
print(mensaje[:6])
print(mensaje[:])
print(mensaje[-5:])

texto = " La UTM  es una universida que +forma profesionales y buenos seres humanos"
#Mayuscuka
print(texto.upper())
#Minuscula
print(texto.lower())
#Elimina espacios en blanco desde la izquierda
print(texto.strip())
print(texto.replace("UTM","ULEAM"))
bloque1=texto.split("+")
print(bloque1[0]+bloque1[1])

usuario='Yasmani'
telefono='0958601551'
print(f'{usuario} tiene un contacto de whatsApp que responde a:{telefono}')
print('{} tiene un contacto de whatsApp que responde a:{}'.format(usuario,telefono))

total = float (Decimal('130.00'))
print(f'total: ${total}')#establecer dos decimales
print(3.75+total)
