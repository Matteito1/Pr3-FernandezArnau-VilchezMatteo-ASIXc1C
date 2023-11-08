"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
CustomerLoyaltyCard
Programa que demana l'import d'una factura, amb iva inclòs.
Calcula l'import amb descompte, en cas de tenir la targeta de client,
tenint en compte els següents criteris:
Si l'import de la factura, és igual o superior a 100 €,
se li aplica un descompte del 21%,
en cas contrari no se li aplica cap descompte. El descompte es calcula al preu final,
I no a la “base imponible”. I després si li aplica l’IVA
Precio total = Base imponible * Tipo de IVA
"""
Precio = float(input("Introduzca el valor:"))
tarjeta= input("Tiene usted tarjeta (si/no):")
if tarjeta =="no":
    print("No tiene tarjeta asi que su precio será sin descuento y será:",Precio,"€")
elif tarjeta == "si":
   if Precio >= 100:
    PrecioMod = Precio+21
    PrecioDescont = PrecioMod*0.79
    PrecioIva = PrecioDescont*1.21
    Descuento = round(PrecioDescont,2)
    Iva = round(PrecioIva,2)
    print("Tu precio total es:",Iva,"€","Tu descuento del 21%:",Descuento,"Tu precio con IVA:",Iva)
else:
    print("Lo siento no tendrá ningún descuento y su precio es de", Precio,"€")
