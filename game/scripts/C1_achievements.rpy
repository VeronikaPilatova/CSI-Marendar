init python:

    achievement_name = {
        "flowers": Achievement(name=_("Květiny a jablečný závin"), message=_("Mistr Heinrich a jeho žena si k sobě znovu našli cestu."), image="images/achievements/trophy flowers.png", priority=None),
        "jointMasterpiece": Achievement(name=_("Společné dílo"), message=_("Spolupráce mistrů Heinricha a Njala překvapila celé město."), image="images/achievements/trophy jointMasterpiece.png", priority=None),
        "dinner": Achievement(name=_("Nacpaný k prasknutí"), message=_("Co je lepší než dobrá večeře? Tři dobré večeře v jeden den."), image="images/achievements/trophy dinner.png", priority=None),
        "poet": Achievement(name=_("Básník"), message=_("Jsi strážný mnoha talentů."), image="images/achievements/trophy quill.png", priority=None),
        "blackmail": Achievement(name=_("Vyděrač"), message=_("Pohybuješ se ve stínech bez povšimnutí."), image="images/achievements/trophy blackmail.png", priority=None),
        "burglar": Achievement(name=_("Křivolaké cesty práva"), message=_("Podařilo se ti vloupat do Heinrichovy dílny a získat tam cenné stopy."), image="images/achievements/trophy key.png", priority=None),
        "arrestedEveryone": Achievement(name=_("Na každého něco"), message=_("Marendarská věznice je velká a ty ji plně využíváš."), image="images/achievements/trophy cell.png", priority=None),
        "heinrichGuildmaster": Achievement(name=_("Heinrich cechmistrem"), message=_("Radši mluvit zpříma, než se všemi vyjít."), image="images/achievements/trophy guildmaster heinrich.png", priority=None),
        "rumelinGuildmaster": Achievement(name=_("Rumelin cechmistrem"), message=_("Někdy je nejlepší nedělat zbytečné změny."), image="images/achievements/trophy guildmaster rumelin.png", priority=None),
        "kasparGuildmaster": Achievement(name=_("Kaspar cechmistrem"), message=_("Když se dva perou, třetí je zvolen."), image="images/achievements/trophy guildmaster kaspar.png", priority=None),
        "firefighter": Achievement(name=_("Ochránce Marendaru"), message=_("Jeden požár stačil."), image="images/achievements/trophy bucket.png", priority=None),
        "katrin": Achievement(name=_("Ohnivá obhajoba"), message=_("Podařilo se ti najít zastání pro Katrin."), image="images/achievements/trophy katrin.png", priority=None),

        "fired": Achievement(name=_("Vyhozen z hlídky"), message=_("Ne každý příběh končí šťastně."), image="images/achievements/trophy trownOut.png", priority="hidden"),
        "blackmailFailed": Achievement(name=_("Neúspěšný vyděrač"), message=_("Zločin se ne vždy vyplácí."), image="images/achievements/trophy stocks.png", priority="hidden"),
        "universalCulprit": Achievement(name=_("Univerzální viník"), message=_("Zeran byl zatčen ze tří různých důvodů."), image="images/achievements/trophy handcuffs.png", priority="hidden"),
        "fistfight": Achievement(name=_("Rváč"), message=_("Někdy pouhá slova nestačí a musí přijít ke slovu pěsti."), image="images/achievements/trophy fistfight.png", priority="hidden"),
        "heinrichTools": Achievement(name=_("Heinrichovi navzdory"), message=_("Na jeho nástroje prý nesmí nikdo jiný sahat. No to určitě."), image="images/achievements/trophy tools.png", priority="hidden"),
        "bookworm": Achievement(name=_("Knihomol"), message=_("Velikost marendarské knihovny se nemůže měřit s tvým čtenářským nadšením."), image="images/achievements/trophy books.png", priority="hidden"),
    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

# Checks for granting some achievements
label dinnerAchievementCheck:
    if "dinner with Njal" in dailyStatus and "dinner with colleagues" in dailyStatus and "dinner with Salma" in dailyStatus:
        if not achievement.has(achievement_name['dinner'].name):
            $ Achievement.add(achievement_name['dinner'])
    return

label universalCulpritAchievementCheck:
    if len(persistent.zeranArrestReasons) == 3:
        if not achievement.has(achievement_name['universalCulprit'].name):
            $ Achievement.add(achievement_name['universalCulprit'])
    return

label arrestedEveryoneAchievementCheck:
    # Zeran, Aachim, Rudi, Ferdi, Kaspar, Njal, Gerd, Erle, Eckhard, Rumelin
    if len(persistent.arrestedPeople) == 10:
        if not achievement.has(achievement_name['arrestedEveryone'].name):
            $ Achievement.add(achievement_name['arrestedEveryone'])
    return
