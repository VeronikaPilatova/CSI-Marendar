label sabriController:
    $ origAsked = sabri.asked.copy()
    if sabri.alreadyMet == False:
        call sabriFirst
    else:
        call sabriAgain
    call sabriOptions
    if sabri.alreadyMet == False:
        $ sabri.alreadyMet = True
        $ sabriNote.isActive = True

    # adjust time spent
    $ lastSpokenWith = "sabri"
    $ time.addMinutes((len(sabri.asked) - len(origAsked)) * 3)
    return

label sabriFirst:
    scene bg sabri outside
    $ sabri.say("Vítej. Jsem Sabri a tahle ubytovna je moje dílo. Jestli potřebuješ útočiště před křivdou nebo tlakem okolí, dokážu pomoct.")
    scene bg sabri inside
    return

label sabriAgain:
    scene bg sabri outside
    $ sabri.say("Vítej. Co tě tíží tentokrát?")
    scene bg sabri inside
    return

label sabriOptions:
    call sabriOptionsRemainingCheck
    call zeranOptionsRemainingCheck
    if sabriOptionsRemaining == 0 and zeranOptionsRemaining == 0:
        return

    show mcPic at menuImage
    menu:
        "Co je tohle za místo?" if "place" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("place")
            $ sabri.say("Marendar? Město, které málem zadusilo samo sebe a teď teprve hledá, jak pokračovat dál.")
            $ sabri.say("Dočasná čtvrť? Budoucí chudinská čtvrť. Část města pro ty, kdo si nemohou dovolit víc. Nádeníci, někteří tovaryši, nemocní. Pár domů se tu ještě opraví a část obyvatel se přesune jinam. Většina zdejších bude živořit podobným způsobem jako teď do konce života.")
            $ sabri.say("A tenhle dům? Sem přichází ti, kdo svoje postavení chtějí změnit. Kdo cítí, že si zaslouží víc.")
        "To zní jako nebezpečná sebranka." if "place" in sabri.asked and "dangerous people" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("dangerous people")
            $ sabri.say("Nebezpečná zaběhnutým pořádkům nebo něčímu pocitu nadřazenosti možná ano. Nebezpečná zdraví nebo majetku ne. Nepouštím sem lidi, kteří touží po pomstě, jen ty, kteří si chtějí vybudovat nový život.")
        "Co to je za lidi?" if "place" in sabri.asked and "people" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("people")
            $ sabri.say("Ti, kteří se nějak narodili a jinak chtějí žít. Hlavně lidé a elfové, ale už tu byl i jeden trpaslík. Mají vůli, mají schopnosti, nemají prostředky.")
            $ mc.say("A ty prostředky máš?")
            $ sabri.say("Nějaké ano. Svoje životy ale mění sami, s mojí podporou.")
        "Co tady ti lidé dělají?" if "place" in sabri.asked and "what people do here" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("what people do here")
            $ sabri.say("Hledají si svou cestu. Posilují svou sebejistotu a utvrzují se v tom, co opravdu chtějí. Část jich pak odejde do jiného města, část si najde uplatnění tady. Část jich cestu nedokončí, protože selže jejich vůle.")
        "Proč jim takto pomáháš?" if "place" in sabri.asked and "why help" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("why help")
            $ sabri.say("Jsem kněz Purushotamy. Můj bůh stojí za všemi, kdo se cítí zrazení, opuštění nebo nedocenění a mají odhodlání to změnit. Podporuje všechny, kdo chtějí žít v jiném řádu než v tom, do kterého se narodili. Sloužím bohu a lidem a tím i celému městu, protože ti lidé pak dokážou mnohem víc.")
            $ mc.say("A co z toho máš ty? Jak ty měníš svůj život?")
            $ sabri.say("Já už svůj život dávno změnil. Získal jsem naplnění. Co bych měl žádat víc?")
        "Znáš Hayfu?" if "hayfa" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("hayfa")
            $ sabri.say("Jistě. Takových jako ona by město potřebovalo co nejvíc.")
        "Proč zrovna jako ona?" if "hayfa" in sabri.asked and "what makes hayfa special" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("what makes hayfa special")
            if gender == "M":
                $ sabri.say("Protože bude chránit město do roztrhání těla a protože je neobyčejně schopná. Ale to bys přece měl vědět lépe než já. Já nesloužím v hlídce, ty ano.")
            else:
                $ sabri.say("Protože bude chránit město do roztrhání těla a protože je neobyčejně schopná. Ale to bys přece měla vědět lépe než já. Já nesloužím v hlídce, ty ano.")
        "Jak jste se poznali?" if "hayfa" in sabri.asked and "meeting hayfa" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("meeting hayfa")
            call sabriAboutHayfaPast
        "Kde se to všechno naučila?" if "hayfa" in sabri.asked and "hayfa skills" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("hayfa skills")
            call sabriAboutHayfaPast
        "Jak to v dočasné čtvrti chodí?" if "temporary quarter" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("temporary quarter")
            $ sabri.say("Jako v každé chudé čtvrti. Lidé se protloukají, jak jen mohou.")
            $ sabri.say("Elfové a lidé se stále ještě úplně neusmířili a moc se nestýkají. A jsou tu i takoví, kdo nejsou přijímaní ani mezi komunitou vlastní rasy v dočasné čtvrti. Ti stojí opravdu na kraji společnosti.")
            $ mc.say("A ti pak končí u tebe, předpokládám?")
            $ sabri.say("Často se o to pokouší. Ne všichni jsou vhodní.")
        "Bydlí tady Zeran?" if zeranNote.isActive == True and "zeran" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran")
            $ sabri.say("Ano.")
        "Můžu se Zeranem mluvit?" if "zeran" in sabri.asked and zeranOptionsRemaining > 0:
            hide mcPic
            $ sabri.say("Pokud bude chtít. Počkej tady.")
            "Sabri se otočí a vejde hlouběji do domu. Tlumeně zaslechneš klepání na dveře a krátký nezřetelný rozhovor. Potom se před tebou objeví mladý elf s nepřátelským pohledem."
            jump zeranController
        "Tušíte, co má Zeran v plánu?" if "zeran" in sabri.asked and "zeran plans" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran plans")
            $ sabri.say("Pokud vím, získat nějaké peníze a odejít jinam. Nebo odejít i bez peněz, jestli to bude trvat moc dlouho. Tohle město ho zklamalo.")
        "Dalo by se Zeranovi nějak pomoci?" if "zeran" in sabri.asked and "zeran help" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran help")
            $ sabri.say("Peníze asi neodmítne, ale myslím, že hlavně potřebuje pocit, že ho někdo bere vážně.")
        "Opravdu měl Zeran vztah s Heinrichovou dcerou?" if "zeran" in sabri.asked and "zeran and ada" not in sabri.asked and "Zeran offense" in clues:
            hide mcPic
            $ sabri.asked.append("zeran and ada")
            $ sabri.say("Neměl.")
            $ mc.say("Proč si to myslíte?")
            $ sabri.say("Jsem kněz a nějakou dobu už u mně žije.")
            $ sabri.say("Správná otázka podle mě zní, jak ho z toho někdo mohl podezřívat. Kdyby spolu něco měli, nejspíš by jí nepsal básničky a určitě by ji nezapíral i poté, co ho vyhnali.")
            $ clues.append("Zeran innocent")
        "Je možné, že Zeran ukradl výrobek mistra Heinricha určený pro Einionovy slavnosti?" if "zeran" in sabri.asked and "zeran thief" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran thief")
            $ sabri.say("To si nemyslím. Kdyby se chtěl mstít, nezůstal by jen u jedněch bot a okamžitě by po činu utekl z města.")
        "Byl včera v noci Zeran opravdu nedaleko západní brány? Tvrdí, že tam pracoval." if "alibi" in zeran.asked and "zeran alibi" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran alibi")
            $ sabri.say("Vím, že si domluvil práci, většinu noci byl pryč a ráno se vrátil s penězi. Také jsem potom nepotkal nikoho, kdo by si stěžoval, že ta práce nebyla odvedená. Věřím, že toho by si všimli.")
            $ sabri.say("Ale jestli byl u západní brány, nebo u východní, na to jsem se neptal.")
        "Už vás dál nebudu zdržovat. Děkuji vám za pomoc.":
            hide mcPic
            return

    if len(sabri.asked) - len(origAsked) == 3 and "mc faith" not in sabri.asked:
        $ sabri.say("Teď se zeptám pro změnu já. Jaký bůh je ti nejbližší?")
        $ sabri.asked.append("mc faith")
        $ mc.say("To se vlastně budu muset zamyslet... (TBD)")

    jump sabriOptions

label sabriAboutHayfaPast:
    if "meeting hayfa" in sabri.asked and "hayfa skills" in sabri.asked:
        $ sabri.say("Řekl jsem přece, že o její minulosti nechci mluvit. Zeptej se přímo jí, ona sama se rozhodne, co ti chce sdělit.")
        $ sabri.trust -= 1
    else:
        $ sabri.say("Její minulost patří jen jí a já o ní nebudu nic říkat.")
    return

###

label sabriOptionsRemainingCheck:
    $ sabriOptionsRemaining = 0
    if "place" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "dangerous people" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "people" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "what people do here" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "why help" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "what makes hayfa special" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "meeting hayfa" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "hayfa skills" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "temporary quarter" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if zeranNote.isActive == True and "zeran" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran plans" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran help" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran and ada" not in sabri.asked and "Zeran offense" in clues:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran thief" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "alibi" in zeran.asked and "zeran alibi" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    return
