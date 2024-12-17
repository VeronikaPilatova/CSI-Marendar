label lieseController:
    $ origAsked = liese.asked.copy()

    if liese.alreadyMet == False:
        call lieseFirst
    else:
        call lieseAgain
    call lieseOptions

    $ time.addMinutes((len(liese.asked) - len(origAsked)) * 3)
    if liese.alreadyMet == False:
        $ time.addMinutes(10)
        $ liese.alreadyMet = True
    $ lastSpokenWith = "Liese"
    return

label lieseFirst:
    "V domě přímo naproti Heinrichově dílně žije osamělý řemeslník, který se omluví na těžkou práci a tvrdé spaní."
    "Zkusíš to ještě o dům vedle a otevře ti vyčerpaně působící mladá žena."
    $ liese.say("Potřebujete něco? Otík teď spí, hlavně ho nechci vzbudit.")
    $ mc.say("Otík?")
    $ liese.say("Je mu pět měsíců a myslím, že mu budou růst zoubky. V noci skoro nespal.")
    $ mc.say("Nevšimla jste si v noci náhodou něčeho podezřelého naproti?")
    $ liese.say("Podezřelého? Asi ne. Stalo se něco?")
    $ mc.say("Mistru Heinrichovi se včera z dílny ztratil jeho výrobek. Neviděla jste, že by dovnitř šel někdo cizí?")
    "Mladá žena zavrtí hlavou."
    $ liese.say("Myslím, že ne… jen Heinrich nebo jeho učedníci.")
    $ mc.say("Můžete mi popsat všechno, co jste viděla?")
    $ liese.say("Heinrich odešel z domu, to bylo myslím kolem šesté. Chvíli před tím, než jsem nám s manželem dělala večeři. V dílně asi zůstali učedníci, protože se tam potom ještě dlouho svítilo. Nejspíš jim dal Heinrich dost práce.")
    $ liese.say("Potom jsem na nějakou dobu usnula, vzbudil nás s Otíkem oba Heinrich, když se vracel domů. Kolik bylo hodin nevím, ale asi mohlo být dost pozdě, a ti dva hulákali jako na lesy nějakou opileckou písničku. Zapadli do dílny a ani si nerozsvítili, ten, co Heinricha doprovázel, se potom vrátil sám.")
    $ liese.say("A ještě chvíli potom šel do dílny jeden z jeho učedníků, asi se vracel z nějaké pochůzky. Ten si tam aspoň rozsvítil.")
    return

label lieseAgain:
    "Znovu zaklepeš na dům, kde jsi naposled mluvil s mladou matkou Liese. Ta vypadá pořád stejně vyčerpaná a v náručí má malé dítě."
    $ liese.say("Aha, to jste zase vy. Potřebujete ještě něco?")
    $ mc.say("Ještě mě napadlo pár dalších otázek. Můžu vás ještě chvíli zdržet?")
    "Žena si povzdechne a lépe chytí dítě, které se po tobě zvědavě natahuje."
    return

label lieseOptions:
    call lieseOptionsRemainingCheck
    if lieseOptionsRemaining == 0:
        $ mc.say("Nebudu vás už zdržovat.")
        "Žena jen přikývne a odběhne zpět do domu."
        return

    show mcPic at menuImage
    menu:
        "Na jaké pochůzce mohl ten učedník být tak pozdě v noci?" if "errand" not in liese.asked:
            hide mcPic
            $ liese.asked.append("errand")
            $ liese.say("Omlouvám se, ale to opravdu netuším.")
        "Poznala jste, který učedník na té pochůzce byl?" if "which apprentice" not in liese.asked:
            hide mcPic
            $ liese.asked.append("which apprentice")
            $ liese.say("Ten nejmladší, Gerd. Hnědovlasý usměvavý kluk.")
            $ liese.say("Ten vlastně od Heinricha nedávno odešel k jinému mistrovi a asi bych věděla, kdyby se zase vrátil, tak možná dostal za úkol mistru Heinrichovi něco donést. Nebo se šel jen podívat za ostatními kluky?")
            $ liese.say("To by mě vlastně vůbec nepřekvapilo, vždycky měli dobré vztahy.")
            $ gerdInWorkshopDiscovered = copy.deepcopy(time)
        "Ničeho dalšího jste si nevšimla?" if "anything else" not in liese.asked:
            hide mcPic
            $ liese.asked.append("anything else")
            "Žena se zamyslí."
            $ liese.say("Jedině, že potom ráno Aachim vynášel nějaké smetí, jestli něco takového může být užitečné.")
            $ mc.say("Bylo na tom něco neobvyklého?")
            $ liese.say("Jenom tím, že to většinou dělal Gerd nebo teď Rudi. Aachima jsem jít se smetím neviděla už dlouho, ale mohli si to jen s Rudim vyměnit. Uklízí stejně všichni společně.")
        "Co za smetí to bylo?" if "anything else" in liese.asked and "garbage" not in liese.asked:
            hide mcPic
            $ liese.asked.append("garbage")
            $ liese.say("Nevím. Asi nějaké odstřižky a jiný odpad z jejich práce. Možná tam měl i nějakou lahev, nevím. Je to důležité? Měla bych nakrmit Otíka.")
        "Všimla jste si, kterým směrem s tím smetím šel?" if "anything else" in liese.asked and "garbage direction" not in liese.asked:
            hide mcPic
            $ liese.asked.append("garbage direction")
            $ liese.say("Dál ulicí, jako k rybímu trhu.")
            $ mc.say("Takže směrem k řece?")
            $ liese.say("Ano. Ale kam přesně zabočil, to samozřejmě netuším.")
        "Jaký vztah spolu mají mistr Henrich a jeho žena?" if lotte.alreadyMet == True and "victim's marriage" not in liese.asked:
            hide mcPic
            $ liese.asked.append("victim's marriage")
            $ liese.say("Myslím, že jako lidé po patnácti letech manželství.")
            $ mc.say("Nevíte o tom, že by měli nějaké problémy?")
            "Liese pomalu zavrtí hlavou."
            $ liese.say("On je často se svými přáteli a ona má na starosti celou domácnost. Ale to nejsou problémy, to je život.", "sad")
        "Je možné, že by paní Lisbeth měla milence?" if lotte.alreadyMet == True and "secret lover" not in liese.asked:
            hide mcPic
            $ liese.asked.append("secret lover")
            $ liese.say("O tom nic nevím a nemyslím si, že by Lisbeth něco takového udělala. Ona je ten typ, co bude radši tiše nešťastná, než aby zradila manžela.")
        "Nebudu vás už zdržovat.":
            hide mcPic
            "Žena jen přikývne a odběhne zpět do domu."
            return
    jump lieseOptions

###

label lieseOptionsRemainingCheck:
    $ lieseOptionsRemaining = 0
    if "errand" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if "which apprentice" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if "anything else" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if "anything else" in liese.asked and "garbage" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if lotte.alreadyMet == True and "victim's marriage" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if lotte.alreadyMet == True and "secret lover" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if "anything else" in liese.asked and "garbage" not in liese.asked:
        $ lieseOptionsRemaining += 1
    if "anything else" in liese.asked and "garbage direction" not in liese.asked:
        $ lieseOptionsRemaining += 1
    return
