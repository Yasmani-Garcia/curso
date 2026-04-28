'''
import datetime
def edad_usuario(año_nacimiento):
    edad = datetime.date.today().year - año_nacimiento
    return edad

def login(u,p,an):
    
    #Simulacion de consulta de SQL desde una base de datos
    #usuario = f'SELECT * FROM usuario WHERE username={u}  AND contraseña = {p}'
    #datos = usuario.fetchall()
    # print('Datos:  ',datos)
    if u == 'admin' and p == 'admin123.':
        e = edad_usuario(an)
        #print(f'Bienvenido{u}, su edad es {e}años.')
        mensaje = f'Bienvenido{u}, su edad es {e}años.'
        return mensaje 
    else:
        #print('Usuario no encontrado o contraseña incorrecta.')
        mensaje = 'Usuario no encontrado o contraseña incorrecta.'
        return mensaje
contador = 1
while contador <=3:  

    usuario_input = input('Ingrese su nombre de usuario:  ')
    contraseña_input = input('Ingrese su contraseña:  ')
    fecha_nacimiento_input = int(input('Ingrese su año de nacimiento(YYYY): '))
          
    datos = login(usuario_input,contraseña_input,fecha_nacimiento_input)
    
    print(datos)
    contador +=1
'''
carrito = [] #lista vacia
def añadir_al_carrito(producto):
    
    carrito.append(producto)
    return carrito

while True:
    producto_input = input('Ingrese el nombre del producto: ')
    print('Deseas desea agregar productos  (s/n)')
    respuesta = input().lower()
    if respuesta == 'n':
        break
print('Producto en el carrito')
for p in carrito:
    print(f'{p}')