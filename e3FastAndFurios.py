"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
FastAndFurios
Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
Cal demanar velocitat inicial (m/s), l'acceleració (m/s²) i el temps.
Si la velocitat instantània és inferior o igual a 0,
has d'indicar que està parat i no pots calcular la velocitat mitjana.
"""
velocidadInicial = float(input())
Aceleracion = float(input())
tiempo = float(input())
velocidadInstantanea = velocidadInicial+Aceleracion*tiempo
velocidadMedia = (velocidadInicial + velocidadInstantanea)/2
if velocidadInstantanea <= 0:
    print("Esta pausado y no puedes calcular la velocidad")
print("Velocidad Instantea:",velocidadInstantanea,"Velocidad Media:",velocidadMedia)
