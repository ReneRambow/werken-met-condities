if input("Is de kaas geel?") == "ja":
    if input("zitten er gaten in de kaas?") == "ja":
        if input("Is de kaas belachelijk duur?") == "ja":
            print("Emmentaler")
        else:
            print("Leerdammer")
    else:
        if input("Is de kaas hard als steen?") == "ja":
            print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")
else:
    if input("Heeft de kaas een korst?") == "ja":
        if input("Heeft de kaas blauwe schimmels?") == "ja":
            print("Blue de Rochbaron")
        else:
            print("camembert")
    else:
        if input("Heeft de kaas blauwe schimmels?") == "ja":
            print("fourme d'ambert")
        else:
            print("mozzarella")