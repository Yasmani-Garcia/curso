#Cadena de caracteres
mensaje = """
El señor es mi pastor,
nada me faltara
(salmos 23:1)
"""
print(mensaje)

#Slicing --> rebanda -->(NLP)
cadena = "Si tenemos que nombrar dos frameworks para desarrollo en Python uno de ellos sería Django, por supuesto, ya que es el más popular. Tampoco dudaríamos al señalar la otra alternativa:  Flask. Este framework que lleva años ganando popularidad y expandiendo su comunidad. ¿Quieres saber más sobre esta herramienta para desarrollar proyectos web en Python?"
print(len(cadena)) # Cantidad de caracteres que tiene la cadena
pos = cadena.find('.')
print(cadena[0:pos+1])
#print(cadena[0:130])

#Verificar si una palabra esta en la cadena
print("frameworks" in cadena) #booleano(true or false)

#if = si se encuentran un termino dentro de la cadena
texto = "La programacion es el arte de pensar bajo una sintaxis adecuada"
if "arte" in texto:
    print("arte esta en texto")
    posicion = texto.find("arte")
    print(posicion)
else:
    print("No se encontro")