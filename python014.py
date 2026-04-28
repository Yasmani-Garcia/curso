import datetime
'''
#Estructura de control if
hora = int(input('Ingrese hora: '))
print(type(hora))#str
if hora >=0 and hora <=5:
    print('De madrugada')
elif hora >=6 and hora <=12:
    print("Buenos dias")
elif hora >12 and hora <=18:
    print('Buenas tarde')
else:
    print('Buenas noches')

#Estructura if/else
año_nacimiento= int(input ('Ingrese año de nacimiento: '))
año_actual = datetime.datetime.now().strftime('%Y')# año actual
edad = int(año_actual) - año_nacimiento
if edad >= 18:
    print(f'usted tiene {edad} años por lo tanto es mayor de edad')
else:
   print(f'usted tiene {edad} años por lo tanto es menor de edad')

'''
'''
usuario = input('User: ')
clave = input('Password: ')
if usuario == 'admin'and clave == 'admin123':
       print(f'Bienvenido {usuario}')
else:
       print(f'Usuario o clave incorrecta. Acceso denegado')

'''
usuario = input('User: ')
clave = input('Password: ')
bienvenido = 'Bienvenid@ {usuario}' if usuario == 'admin' and clave == 'admin123.'else 'Acceso denegado'
print(bienvenido)

#Validar que un usuario sea mayor de edas y que tenga una estatura mayor a 1.70 mts
edad = int(input('Edad: '))
estatura = float(input('Estatura en mts: '))
if edad >= 18:
       if estatura > 1.70:
              print('Admitido')
else:
       print('No Admitido')