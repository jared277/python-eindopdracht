Boodschappen = ["melk", "brood", "soep", "sap", "chocolade"]

Boodschappen.append("orange")

Boodschappen.append("water")

Boodschappen.remove ("brood")

print (len (Boodschappen))

for producten in Boodschappen:
    print (producten)
    
if "soep" in Boodschappen:
    print("soep zit in de lijst")