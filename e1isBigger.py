"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
IsBigger
Programa que demana dos números si el primer és més gran o igual
que el segon els intercanvia
"""

numero1 = int(input())
numero2 = int(input())
if numero1>=numero2:
    numero1,numero2=numero2,numero1
    print(numero1,numero2)
else:
    print(numero1,numero2)
