"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
IsACorrectDate
Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs.
NO es pot fer servir funcions de calendari com ara datetime de Python
"""
fecha = input()
fecha = fecha.split()
dia = int(fecha[0])
mes = int(fecha[1])
any = int(fecha[2])
