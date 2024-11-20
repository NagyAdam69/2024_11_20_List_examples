"""
Hozz létre egy listát számokkal, ahol előfordulhatnak duplikációk: [1, 2, 2, 3, 3, 4, 5, 5].
Távolítsd el a duplikált számokat, és írd ki az eredményt!
"""

# set-es megoldás

lista = [1, 1, 2, 2, 3, 4, 5, 5, 6]

for i in lista:
    if i in lista:
        lista.remove(i)
print(lista)