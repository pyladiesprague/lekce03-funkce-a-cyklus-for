# ---------------------------------------------
#  Řešení – bonusová cvičení: procházení a kombinace
# ---------------------------------------------


# B1) Trojúhelník z hvězdiček. Uživatel zadá výšku a ty vypiš
#     trojúhelník, kde první řádek má jednu hvězdičku, druhý dvě atd.
vyska = int(input("Jak vysoký trojúhelník? "))
for radek in range(1, vyska + 1):
    print("*" * radek)               # "*" * 3 je "***"


# B2) Rámeček N x N – okraj z X, vnitřek prázdný.
#     X se kreslí na prvním a posledním řádku a v prvním a posledním
#     sloupci; jinde je mezera.
n = int(input("Jak velký rámeček? "))
for radek in range(n):
    for sloupec in range(n):
        if radek == 0 or radek == n - 1 or sloupec == 0 or sloupec == n - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()


# B3) Ciferný součet. Uživatel zadá číslo. Sečti jeho jednotlivé číslice
#     a součet vypiš (třeba z 253 vyjde 2 + 5 + 3 = 10).
cislo = input("Zadej číslo: ")           # necháme jako text, ať projdeme číslice
soucet = 0
for znak in cislo:
    soucet = soucet + int(znak)          # každou číslici převedeme na číslo
print("Ciferný součet:", soucet)


# B4) Teploty za týden. Sedm teplot – průměr, nejtepleji, nejchladněji
#     a počet dní pod nulou. První teplotu si uložíme jako výchozí
#     a zbylých šest s ní porovnáváme.
prvni = int(input("Zadej teplotu: "))
soucet = prvni
nejtepleji = prvni
nejchladneji = prvni
pod_nulou = 0
if prvni < 0:
    pod_nulou = pod_nulou + 1
for den in range(6):                     # zbývá dalších šest dní
    teplota = int(input("Zadej teplotu: "))
    soucet = soucet + teplota
    if teplota > nejtepleji:
        nejtepleji = teplota
    if teplota < nejchladneji:
        nejchladneji = teplota
    if teplota < 0:
        pod_nulou = pod_nulou + 1
print("Průměr:", soucet / 7)
print("Nejtepleji:", nejtepleji)
print("Nejchladněji:", nejchladneji)
print("Dní pod nulou:", pod_nulou)


# B5) Palindrom. Slovo si v cyklu poskládáme pozpátku a porovnáme
#     s původním. Trik: každé písmeno dáme PŘED to, co už máme.
slovo = input("Napiš slovo: ")
obracene = ""
for znak in slovo:
    obracene = znak + obracene           # "k" + "aja" = "kaja" ... a tak dál
if slovo == obracene:
    print("Je to palindrom.")
else:
    print("Není to palindrom.")
