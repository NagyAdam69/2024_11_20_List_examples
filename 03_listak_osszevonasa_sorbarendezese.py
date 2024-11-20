"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""
lista1 = [3, 1, 4]
lista2 = [9, 7, 2]

nagylista = lista1 + lista2
nagylista.sort()
print(nagylista)
# írasd ki az első és az utolsó elemet!

print(nagylista[0])
print(nagylista[-1])