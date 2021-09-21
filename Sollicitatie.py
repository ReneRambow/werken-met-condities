print("""
-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-

------------------------------------------
* Sollicitatieformulier Circus Directeur *
------------------------------------------""")

naam = input("Wat is uw naam? ")
gewicht = int(input("Wat is uw lichaamsgewicht in Kilogram? |Rond af op hele kilo's| "))
if gewicht >= 90:
    gewicht = True
else:
    gewicht = False
print(gewicht)
lengte = int(input("Wat is uw lichaamslengte in centimeters? "))
if lengte >= 150:
    lengte = True
else:
    lengte = False
print(lengte)

dierenDressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dierenDressuur? "))
if dierenDressuur >= 4:
    dierenDressuur = True
else:
    dierenDressuur = False
print(dierenDressuur)

jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
if jongleren >= 5:
    jongleren = True
else:
    jongleren = False
print(jongleren)

acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
if acrobatiek >= 3:
    acrobatiek = True
else:
    acrobatiek = False
print(acrobatiek)

diploma = str(input("Heeft u een MBO-4 diploma? ja/nee "))
if diploma == "ja":
    diploma = True
else:
    diploma = False
print(diploma)

vrachtwagenRijbewijs = str(input("Heeft u een geldig vrachtwagenRijbewijs? ja/nee "))
if vrachtwagenRijbewijs == "ja":
    vrachtwagenRijbewijs = True
else:
    vrachtwagenRijbewijs = False
print(vrachtwagenRijbewijs)

hogehoed = str(input("Bent u in bezit van een hoge hoed? ja/nee "))
if hogehoed == "ja":
    hogehoed = True
else:
    hogehoed = False
print(hogehoed)

certificaat = str(input("Bent u in bezit van het certificaat *Overleven et gevaarlijk personeel* ? ja/nee "))
if certificaat == "ja":
    certificaat = True
else:
    certificaat = False
print(certificaat)

geslacht = str(input("Welke geslacht heeft u? Man/Vrouw "))
if geslacht == "Man":
    print(geslacht)
    manSnor = str(input("Heeft u een snor? ja/nee "))
    if manSnor == "ja":
        Snorlengte = int(input("Hoe breed is uw snor? "))
        if Snorlengte >= 10:
            Snorlengte = True
        else:
            Snorlengte = False
        print(Snorlengte)
    else:
        print("U heeft geen snor")
elif geslacht == "Vrouw":
    print(geslacht)
    krulhaar = str(input("Heeft u krulhaar? ja/nee "))
    if krulhaar == "ja":
        kleurkrulhaar = str(input("Is uw haarkleur rood? ja/nee "))
        if kleurkrulhaar == "ja":
            lengtekrulhaar = int(input("Hoe lang is uw haar? "))
            if lengtekrulhaar >= 20:
                lengtekrulhaar = True
            else:
                lengtekrulhaar = False
            print(lengtekrulhaar)
        else:
            print("Uw haarkleur is niet rood")
    else:
        print("U heeft geen krulhaar")

werkervaring = (dierenDressuur , jongleren , acrobatiek)
overig = (gewicht , lengte , diploma , vrachtwagenRijbewijs , hogehoed , certificaat, geslacht)

overig = any(overig)
werkervaring = all(werkervaring)

x = overig
y = werkervaring

if y == True:
    werkErvaringFinalString = "Voldoende"
elif y == False:
    werkErvaringFinalString = "Onvoldoende"

if x == True:
    overigFinalString = "Genoeg"
elif x == False:
    overigFinalString = "Niet Genoeg"

print("Beste",naam, "U heeft", werkErvaringFinalString, "werkervaring en", overigFinalString, "Talenten")

print("-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-=+@!@+=-")