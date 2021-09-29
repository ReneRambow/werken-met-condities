print(""" 
██╗░░░██╗░█████╗░██╗░░░██╗██████╗░  ░██╗░░░░░░░██╗░█████╗░██╗░░░██╗  ████████╗░█████╗░
╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗  ░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝  ╚══██╔══╝██╔══██╗
░╚████╔╝░██║░░██║██║░░░██║██████╔╝  ░╚██╗████╗██╔╝███████║░╚████╔╝░  ░░░██║░░░██║░░██║
░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗  ░░████╔═████║░██╔══██║░░╚██╔╝░░  ░░░██║░░░██║░░██║
░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║  ░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░

░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░
██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░
╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░
░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░
██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝ """)

if input("Je wordt wakker. Wat ga je eerst doen?\nA: je gaat je aankleden\nB: je gaat je tanden poetsen\n").lower() == 'a':
    print("\nJe gaat je eerst aankleden")
else:
    print('\nJe gaat eerst je tanden poetsen')

if input("\nJe hebt honger. Wat ga je doen?\nA: Je laat je moeder het eten maken\nB: je maakt zelf iets te eten\n").lower() == 'a' :
    print("\nJe moeder maakt voor jou het eten")
else:
    print("\nJe maakt zelf jouw eten")

if input("\nJe gaat je schoenen aantrekken. Je weet alleen niet van welk merk. Je moet een keuze maken. Welke keuze maak je?\nA: Nike schoenen\nB: Adidas schoenen\n").lower() == 'a' :
    print("\nJe trekt Nike schoenen aan")
else:
    print("\nJe trekt Adidas schoenen aan")

if input('\nJe loopt de deur uit en wilt naar school gaan. Hoe ga je dat doen?\nA: met de fiets\nB: je gaat lopen\n').lower() == 'a':
    print("\nJe pakt de fiets")
    if input('\nJe stapt op je fiets en begint naar shool te fietsen. Onderweg zie je een huis in de brand staan. Je ziet dat er nog geen hulpdiensten ter plaatse zijn. Wat ga je doen?\nA: je belt de brandweer\nB: je fietst gewoon door\n').lower() == 'a' :
        print("\nJe belt de brandweer")
        if input('\nDe hulpdiensten arriveren en vragen jou of je hebt gezien waardoor de brand is ontstaan. Je zegt dat je dat niet gezien hebt en vraagt of je nog ter plaatse moet blijven. De hulpdiensten zeggen dat je het plaats delict mag verlaten. Wat ga je doen?\nA: je pakt je telefoon en begint te filmen\nB: je stapt op je fiest en verlaat het gebied\n').lower() == 'a' :
            print("\nJe pakt je telefoon en begint te filmen")
            if input('\n1 van de politie agenten komt naar je toe en vraagt of je kunt stoppen met filmen. Wat ga je doen?\nA: Je belooft te stoppen maar gaat stiekem door met filmen.\nB: Je luistert naar de agent en verlaat het gebied.\n').lower() == 'a' :
                print("\nJe belooft te stoppen maar besluit stiekem door te filmen")
                print("\nJe filmt 5 minuten lang en besluit daarna door te gaan richting school. Je komt op school aan en de docenten zijn boos. Je legt alles uit en laat het filmpje zien. De docenten geloven er niks van en je moet nablijven.")
                print("\nJe hebt gefaald")
            else:
                print("\nJe luistert naar de agent en verlaat het gebied")
                print("\nJe fietst door naar school en komt net op tijd. De docent noemt alle namen op en zet je op aanwezig.")
                print("\nJe hebt gewonnen")
        else:
            print("\nJe stapt op je fiets en verlaat het gebied")
            print("\nJe krijgt een lekke band en komt daardoor te laat op school aan. Je moet nablijven.")
            print("\nJe hebt gefaald")
    else:
        print("\nJe fietst gewoon door")
        print("\nJe nadert een stoplicht en fietst door rood. Een auto raakt je en je beland in het ziekenhuis.")
        print("\nJe hebt gefaald")
else:
    print("\nJe gaat lopen")
    if input('\nJe loopt langzaam richting school. Je nadert een zebrapad en ziet 100m verder een ongeluk gebeuren. Wat doe je?\nA: je belt 112\nB: je negeert het en loopt gewoon door\n').lower() == 'a' :
        print("\nJe belt 112")
        if input('\nJe wacht tot de hulpdiensten arriveren en loopt weer verder. Je bent vergeten iets te eten mee te nemen. Je gaat naar de bakker en wilt een broodje halen. Bij de bakker staat een lange rij. Wat doe je?\nA: Je wacht netjes tot je aan de beurt bent\nB: Je gaat weer weg en loopt door naar school\n').lower() == 'a' :
            print("\nJe wacht netjes")
            print("\nJe pakt je broodje en loopt door naar school. Je komt het lokaal binnen maar je mag geen tene in het lokaal hebben. De docent zegt dat je moet nablijven.")
            print("\nJe hebt gefaald")

        else:
            print("\nJe gaat weer weg en gaat door naar school")
            print("\nJe komt in het lokaal aan en gaat op je plek zitten. Je bent aanwezig gemeld.")
            print("\nJe hebt gewonnen")

    else:
        print("\nJe negeert het en loopt gewoon door")
        if input('\nJe krijgt honger en wilt wat te eten halen. Je gaat naar de dichtstbijzijnde winkel en haalt een broodje. Je gaat richting de kassa maar er staat en hele lange rij. Wat doe je?\nA: Je wacht netjes\nB: Je dringt voor\n').lower() == 'a' :
            print("\nJe wacht netjes")
            print("\nJe betaald je broodje en gaat door richting school. Echter ben je te laat op shool. Je moet nablijven.")
            print("\nJe hebt gefaald")
        else:
            print("\nJe dringt voor")
            print("\nJe wordt aangesproken door een medewerker en die vraagt jou de winkel te verlaten. Je loopt verder richting school maar je bent te laat. De gevolgen zijn dat je moet nablijven.")
            print("\nJe hebt gefaald")