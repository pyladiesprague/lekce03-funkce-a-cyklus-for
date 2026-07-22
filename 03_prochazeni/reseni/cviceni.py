# ---------------------------------------------
#  Řešení – procházení a kombinace
# ---------------------------------------------


# 1) Statistika čísel. Uživatel zadá počet, pak čísla. V jednom průchodu
#    spočítej součet, průměr, největší a nejmenší – bez sum, max a min.
#    Trik: první číslo si uložíme jako výchozí největší i nejmenší
#    a zbytek s ním porovnáváme.
pocet = int(input("Kolik čísel zadáš? "))
prvni = int(input("Zadej číslo: "))
soucet = prvni
nejvetsi = prvni
nejmensi = prvni
for i in range(pocet - 1):              # první už máme, zbývá o jedno míň
    cislo = int(input("Zadej číslo: "))
    soucet = soucet + cislo
    if cislo > nejvetsi:
        nejvetsi = cislo
    if cislo < nejmensi:
        nejmensi = cislo
print("Součet:", soucet)
print("Průměr:", soucet / pocet)
print("Největší:", nejvetsi)
print("Nejmenší:", nejmensi)


# 2) Analýza věty. Projdi větu znak po znaku, počítej samohlásky a mezery.
veta = input("Napiš větu: ")
samohlasky = 0
mezery = 0
for znak in veta:
    if znak in "aeiou":
        samohlasky = samohlasky + 1
    if znak == " ":
        mezery = mezery + 1
print("Počet znaků:", len(veta))
print("Samohlásek:", samohlasky)
print("Mezer:", mezery)
print("Slov:", mezery + 1)              # slov je o jedno víc než mezer


# 3) Bum-Bác pro čísla od 1 do 30.
#    Dělitelnost třemi i pěti = dělitelnost patnácti, a musí se testovat
#    jako první – jinak by číslo spadlo hned do "Bum" nebo "Bác"
#    a na "BumBác" by nikdy nedošlo (to už známe z minulé lekce).
for cislo in range(1, 31):
    if cislo % 15 == 0:
        print("BumBác")
    elif cislo % 3 == 0:
        print("Bum")
    elif cislo % 5 == 0:
        print("Bác")
    else:
        print(cislo)


# 4) Násobilková tabulka 4x4 pomocí vnořených cyklů.
#    radek = vnější (řádky), sloupec = vnitřní (sloupce v jednom řádku).
for radek in range(1, 5):
    for sloupec in range(1, 5):
        print(radek * sloupec, end=" ")
    print()                             # po každém řádku skoč na nový řádek


# 5) Hody dvěma kostkami. Vnější cyklus = první kostka, vnitřní = druhá.
#    Pro každou hodnotu první kostky projdeme všechny hodnoty druhé.
for kostka1 in range(1, 7):
    for kostka2 in range(1, 7):
        print(kostka1, "+", kostka2, "=", kostka1 + kostka2)
