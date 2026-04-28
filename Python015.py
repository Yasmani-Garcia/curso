import datetime
import locale
dia= datetime.date.today()

#Pasar a español
locale.setlocale(locale.LC_TIME,'spanish')

nombre_dia = dia.strftime('%A').capitalize()
print(nombre_dia)

match nombre_dia:
    case 'Lunes':
        print('Lunes --> Descuento en frutas y verduras')
    case 'Martes':
        print('Martes --> Descuento en lacteos')
    case 'Miercoles':
        print('Miercoles --> Descuento en carnes')
    case 'Jueves':
        print('Jueves --> Descuento en productos de limpiezas')
    case 'Viernes':
        print('Viernes --> Descuento en producto de panaderia')
    case 'Sabado':
        print('Sabado --> Descuento en Bebidas')
    case 'Domingo':
        print('Domingo --> Descuento en productos congelados')
    case _:
        print("Dia no valido para descuento especiales")



