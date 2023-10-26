"""
P08 užduotis 4

Panaudoti meniu pagal paskaitos meniu pavyzdį ir parašyti kalkuliatorių, kuris turėtų meniu punktus sudėtis,
atimtis, daugyba, dalyba, išeiti ir galėtų atlikti šiuos veiksmus su 2 skaičiais.

Galimi patobulinimai - meniu punktas "spausdinti skaičių seką nuo iki", taip pat visų kalkuliatoriaus atliktų veiksmų
registravimas ir išsaugojimas tekstiniais stringais į listą, pasirinkus išeiti iš programos, visi atlikti veiksmai
atspausdinami.
"""

# Užduotis - skaičiuotuvas
istorija = []
while True:
    print()
    print("SKAIČIUOTUVO KONSOLĖ\n"
          "Galimo operacijos:\n"
          " 1 - sudėtis\n"
          " 2 - atimtis\n"
          " 3 - daugyba\n"
          " 4 - dalyba\n"
          " Išeiti - q")
    print("-" * 30)
    operacija = input("Pasirinkite kokią operaciją norite atlikti:")
    # Operacijos patikrinimas
    if operacija == "q":
        print("Ate Ate...")
        break
    elif not operacija.isdigit():
        print("Netinkama įvestis. Turi būti skaičius")
        continue
    elif int(operacija) > 4 or int(operacija) == 0:
        print("Tokio pasirinkimo nėra!")
        continue
    varA = input("Įveskite pirmo kintamojo A vertę:")
    varB = input("Įveskite antro kintamojo B vertę:")
    # Patikrinimas

    # Operaciju vykdymas
    varA = int(varA)
    varB = int(varB)
    if operacija == "1":
        ats = varA + varB
        print(f"A+B={ats}")
        istorija.append(f"A+B={ats}")
    elif operacija == "2":
        ats = varA - varB
        print(f"A-B={ats}")
        istorija.append(f"A-B={ats}")
    elif operacija == "3":
        ats = varA * varB
        print(f"A*B={ats}")
        istorija.append(f"A*B={ats}")
    elif operacija == "4":
        ats = varA / varB
        print(f"A/B={ats}")
        istorija.append(f"A/B={ats}")
