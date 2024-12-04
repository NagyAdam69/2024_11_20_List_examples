"""Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát! 

1. Mennyi a sorozatban található számok szorzata? 
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét! 
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét! 
4. Igaz-e, hogy minden szám negatív? 
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? 
6. Hány 18-cal osztható szám található a sorozatban? 
7. Mennyi a sorozatban található egyik legkisebb szám indexe? 
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét! 
9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?
11. Válogassuk ki két listába a páros és a páratlan számokat!
"""
# alap
import random
szamok = [random.randint(-60, 100) for i in range(50)]
print(szamok)

def elso():
    szorzat = 1

    for szam in szamok:
        szorzat *= szam

    print(f"1. feladat: {szorzat}")
elso()

def masodik():
    utolso_index = None
    for i in range(len(szamok)):
        if szamok[i] % 5 == 0 or szamok[i] % 7 == 0:
            utolso_index = i
    print(f"2. feladat: {utolso_index}")
masodik()

def harmadik():
    elso_index = None
    for i in range(len(szamok)):
        if szamok[i] % 3 == 0 and szamok[i] % 7 == 0:
            elso_index = i
            break
    print(f"3. feladat: {elso_index}")
harmadik()

def negyedik():
    minden_negativ = all(szam < 0 for szam in szamok)

    if minden_negativ:
        print("4. feladat: Összes negatív.")
    else:
        print("4. feladat: Nem mindegyik negatív.")

def otodik():
    van_egy_es_tiz_kozott = all(not 0 < szam < 10 for szam in szamok)

    if van_egy_es_tiz_kozott:
        print("5. feladat: Nincs olyan szám, ami egy és tíz közé esik.")
    else:
        print("5. feladat: Van olyan szám, ami egy és tíz közé esik.")
otodik()

def hatodik():
    osthato_18 = sum(1 for szam in szamok if szam % 18 == 0)
    print(f"6. feladat: {oszthato_18}")

def hetedik():
    legkisebb = min(szamok)
    print(f"7. feladat: {legkisebb}")

def nyolcadik():
    for szam in szamok:
        if szam % 17 == 0 or szam % 18 == 0:
            print("8. feladat: ", end=' ')
            print(szam**2, end=" ")

def kilencedik():
    van_ilyen_szam = False
    for szam in range(len(szamok)):
        if szamok[szam] != 50 or szamok[szam] != 0:
            if szamok[szam] < 0 and szamok[szam - 1] > 0 and szamok[szam + 1] > 0:
                print("Van ilyen szám.")
            else:
                print("Nincs ilyen szám.")
    print(szamok)


