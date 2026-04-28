#Tipos de datos  primitivos
#int, bool, double
#Tipos de datos no primitivos
#str, list, tuple, dict, set, range

usuario_web = 'Yasmani'
paises_sudamericano = ['Ecuador', 'Brasil','Argentina','Uruguay']
profesiones_personas =('Ingeniero Civil','Economista','Doctor','Licenciado')
usuario = {
    "nombre":"Yasmani",
    "apellido":"Lopez",
    "Correo": "garcia-yasmani@hotmail.com",
    "Contraseña":"1234"
}
print(usuario['Correo'])

cursos = {'Programacion orientada a objetos','Base de Datos', 'Arquitectura de Software'}
 
for c in cursos:
    print(c)

curso = list(cursos) #pierden el orden especifico
print(curso[0])

#Uso de la funcion type() para conover el tipo de datos
print(type(usuario_web))
print(type(paises_sudamericano))
print(type(profesiones_personas))
print(type(usuario))
print(type(cursos))