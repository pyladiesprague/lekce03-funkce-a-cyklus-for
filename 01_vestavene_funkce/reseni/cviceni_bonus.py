# ---------------------------------------------
#  Řešení – bonusová cvičení: užitečné funkce
# ---------------------------------------------


# B1) Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.
cena = int(input("Kolik jste utratili? "))
lidi = int(input("Kolik vás bylo? "))
print(round(cena / lidi, 2))        # pro 1000 a 3 vypíše 333.33


# B2) Vypiš součet všech čísel od 50 do 100 včetně.
#     Rozmysli si, jaký range zapsat, aby platila obě krajní čísla.
print(sum(range(50, 101)))          # 3825   DO se nepočítá, proto 101


# B3) Máš tři naměřené teploty (klidně i záporné). Vypiš dvě věci:
#     - jak velké bylo rozpětí (nejteplejší mínus nejchladnější den),
#     - jak daleko od nuly byla ta nejextrémnější teplota.
teplota1 = -8
teplota2 = 5
teplota3 = 12
print(max(teplota1, teplota2, teplota3) - min(teplota1, teplota2, teplota3))  # 20
print(max(abs(teplota1), abs(teplota2), abs(teplota3)))                        # 12
