product1 = "brood"
prijsProduct1 = 20
aantal1 = 10
aantalVerkocht1 = 3
inkoopPrijs1 = 15
winstBrood1 = 15

product2 = "soep"
prijsProduct2 = 10 
aantal2 = 15
aantalVerkocht2 = 7
inkoopPrijs2 = 5
winstsoep2 = 35

product3 = "wc's"
prijsProduct3 = 200
aantal3 = 20
aantalVerkocht3 = 10
inkoopPrijs3 = 75
winstwc3 = 1250

totaleInkomen = (
     prijsProduct1 * aantalVerkocht1
    + prijsProduct2 * aantalVerkocht2
    + prijsProduct3 * aantalVerkocht3
)

totaalwinst = winstBrood1 + winstsoep2 + winstwc3
totaalVerkocht = aantalVerkocht1 + aantalVerkocht2 + aantalVerkocht3
totaalomzet = totaleInkomen - totaalwinst
print(f"wij verkopen {product1}, {product2} en {product3}")
print(f"prijs per brood is {prijsProduct1} euro ,prijs van soep is {prijsProduct2} euro , en prijs van de wc's is {prijsProduct3} euro")
print(f"we hebben {aantalVerkocht1} brood verkocht, {aantalVerkocht2} soepen verkocht,en  {aantalVerkocht3} wc's verkocht")
print(f"totaal verkochte producten is {totaalVerkocht}")


      

print(f" wij hebben intotaal {totaleInkomen} Euro verdient")
print(f" wij hebben {totaalwinst} euro gepspendeerd aan inkoopprijzen")
print(f"dus dan hebben wij hebben intotaal {totaalomzet} euro winst gemaakt")
