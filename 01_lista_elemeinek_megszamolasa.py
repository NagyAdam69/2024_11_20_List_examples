"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

lista = [5, 8 , 12, 15, 22]

# len függvénnyel
# print(f"{len(lista)} darab elem van a listában")

darab = 0

for elem in lista:
    darab += 1
print(f"{darab} darab elem van a listában.")