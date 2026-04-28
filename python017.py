nombres = ['Oscar', 'Nayeli', 'Benjamin', 'Josafat']
print(nombres)

print(nombres[2]) #Benjamin
print('Benjamin' in nombres) #True
for n in nombres:
    print(f' * {n}')

for n in range(1,5):
    print(f'{n}')

for n in range(1,20,2):
    print(f'{n}')

lista_numeros_pares = list(range(2,21,2))
print(lista_numeros_pares)