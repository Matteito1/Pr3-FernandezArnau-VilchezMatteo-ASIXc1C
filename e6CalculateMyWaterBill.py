"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
CalculateMyWaterBill
El preu que pagues per l’aigua que consumeixes. El consum es divideix en 5 trams de preus progressius.
El consum es calcula segons els m3 consumits. Qui més estalvi d’aigua fa, menys trams consumeix i,
per tant, més estalvia. Aquest sistema ajuda a fomentar un consum responsable.
Preu = (5.0 * 0.5849) + 6.40
"""
letra = input("Introduce la letra (en Mayusculas) del habitatge:")
numero = float(input("Introduce el numero de m³ gastados:"))
A = 2.46
B = 6.40
C = 7.25
D = 11.21
E = 12.10
F = 17.28
G = 28.01
H = 40.50
I = 61.31
tramo1 = 0.5849
tramo2 = 1.1699
tramo3 = 1.7548
tramo4 = 2.3397
tramo5 = 2.9246
if numero:
    if numero > 5 or numero > 4 or numero > 3 or numero > 2 or numero > 1 or numero > 0 or numero >6:
        precio = (numero * tramo1) + A
        print(numero)
elif numero > 7 or numero > 8 or numero > 9:
    precio = (numero * tramo2) + A
    print(numero)
elif numero > 10 or numero > 11 or numero > 11 or numero > 12 or numero > 13 or numero > 14 or numero > 15:
    precio = (numero * tramo3) + A
    print(numero)
elif numero > 16 or numero > 17 or numero > 18:
    precio = (numero * tramo4) + A
    print(numero)
elif numero > 19:
    precio = (numero * tramo5) + A
    print(numero)
