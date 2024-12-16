label endOfDay:
    $ random = renpy.random.randint(1, 6)
    scene expression ("bg/bg street0[random] night.png")
    "Vyjdeš na ulici a uvědomíš si, že lidí podstatně ubylo. Spatříš jediného osamělého chodce spěchajícího z poslední pochůzky a zdáli zaslechneš opilecké halekání. Dost možná už je příliš pozdě na to, aby bylo vhodné klepat na dveře domů a klást otázky."
    "I tobě se mezi úvahy o případu stále častěji vkrádá myšlenka na měkkou deku a suché klidné místo, kde si ji můžeš rozložit. Možná je čas jít spát a v pátrání pokračovat zítra."

    if time.days == 1:
        call fireshow
        if "duplicate key" in status:
            scene bg heinrich outside night
            "Cestou spát se ještě jednou podíváš směrem k Heinrichově dílně a stiskneš v ruce svou kopii klíče."
            "Převzetí u zámečníka bylo ještě snazší, než jsi čekal[a]. Stačilo jen ukázat pověření člena hlídky a úslužný usměvavý hobit už neměl žádné další otázky. Ten humbuk s hořícím vozem ale přišel v nejhorší možnou chvíli."
            "Na ulici se pořád pohybují lidé, ve většině domů se svítí a nezdá se, že by se to mělo dost rychle změnit. Rozhodně se nemůžeš spolehnout na to, že by tě v Heinrichově domě nikdo neviděl."
            "Rozhodneš se, že jestli máš opravdu jít v noci do dílny, bude to muset počkat."
    if time.days == 2 and "duplicate key" in status:
        "Nebo můžeš konečně využít svou kopii klíče a vplížit se tajně do Heinrichovy dílny. Pokud se toho odvážíš."
        "Nechceš si ani představovat, jaký trest by tě asi čekal, kdyby tě tam chytili, ale na druhou stranu... slavnosti se nemilosrdně blíží a ty nutně potřebuješ nějaký důkaz, který povede k rychlému odsouzení pachatele."
        menu:
            "{i}(Jít spát){/i}":
                pass
            "{i}(Dostat se do Heinrichovy dílny){/i}":
                call workshopNightController

    scene bg hayloft night
    "Nahoru na seník se sotva vyškrábeš, jak jsi unaven[y]. Zabalíš se do deky a okamžitě usneš."

    if "seen during break in" in status:
        jump workshopNightArrestAfter

    # technical
    if time.days == 1:
        if son.imageParameter == "hungover":
            $ son.imageParameter = ""
        if optimist.imageParameter == "hungover":
            $ optimist.imageParameter = ""
        if yesman.imageParameter == "hungover":
            $ yesman.imageParameter = ""
        if eckhard.imageParameter == "hungover":
            $ yesman.imageParameter = ""
    elif time.days == 2:
        $ rauvin.status.append("out of office")
        $ hayfa.status.append("out of office")

    if "promised to share" in dailyStatus:
        $ hayfa.trust -= 1
    $ dailyStatus.clear()

    $ time.addDays(1)
    $ time.hours = 7
    $ time.minutes = 0
    # update relative time variables
    if time.days == 2:
        $ dayOfCrime = "předevčírem"
        $ investigationStart = "včera"
        $ festivalStart = "za tři dny"
    elif time.days == 3:
        $ dayOfCrime = "v den krádeže"
        $ investigationStart = "předevčírem"
        $ festivalStart = "pozítří"
    elif time.days == 4:
        $ dayOfCrime = "v den krádeže"
        $ investigationStart = "den po krádeži"
        $ festivalStart = "zítra"
    elif time.days == 5:
        $ dayOfCrime = "v den krádeže"
        $ investigationStart = "den po krádeži"
        $ festivalStart = "dnes"

    # start of day
    show bg hayloft dawn
    with Fade(0.5, 1.0, 0.5)
    "Probudí tě nemilosrdné ranní slunce. Chce se ti obrátit na druhý bok, zahrabat do sena a spát dál, ale brzy se máš hlásit na strážnici."

    if time.days == 2:
        call firstStandUp
        call kilianEncounter
    elif time.days == 3:
        call secondStandup
    elif time.days == 4:
        call thirdStandup
    $ timeOfDay = "standup"
    call guardhouseAgain

    return
