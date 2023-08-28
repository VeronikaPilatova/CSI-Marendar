label intro:
scene bg exterior01

"" "Ke strážnici marendarské hlídky přicházíš s menší jistotou, než by se ti líbilo. Co když tě nepřijmou? Nebo přijmou jen z nouze, kvůli nedostatku lidí?"
"" "Co když skutečná hlídka nedostojí tvým představám?"
show bg door01
"" "Přede dveřmi na moment zaváháš, pak se ale narovnáš a zaklepeš."

scene bg guardhouse
"" "Otevře ti mladá žena v praktickém oblečení s tesákem u pasu."
$ hayfa.say("Myslím, že se ještě neznáme. Jsem Hayfa. S čím může být hlídka nápomocná?")
if gender == "M":
    $ mc.say("Hledám práci. Totiž... slyšel jsem, že městská hlídka shání nové členy? Jmenuji se %(mcName)s.")
else:
    $ mc.say("Hledám práci. Totiž... slyšela jsem, že městská hlídka shání nové členy? Jmenuji se %(mcName)s.")
# if mcName == "Luisa" or mcName.startswith("Luisa "):
#    "" "Může to být světlem, ale na moment se ti zdá, že se Hayfin výraz změní na téměř nepřátelský. Pak ale mrknš a je to pryč."
$ hayfa.say("Velitel bude nadšený, zrovna dneska si stěžoval, že se všemi těmi kupci a kejklíři, co přijedou na Einionovy slavnosti, bude problém udržet pořádek.")
$ hayfa.say("Ale řekni mi nejdřív něco o sobě. Jsi z Marendaru?")
show mcPic at menuImage
if gender == "M":
    menu:
        "Původem ano, ale dlouho jsem tu nebyl.":
            $ origin = "born here"
        "Mám tady rodinu.":
            $ origin = "family"
        "Přistěhoval jsem se teprve nedávno.":
            $ origin = "newcomer"
else:
    menu:
        "Původem ano, ale dlouho jsem tu nebyla.":
            $ origin = "born here"
        "Mám tady rodinu.":
            $ origin = "family"
        "Přistěhovala jsem se teprve nedávno.":
            $ origin = "newcomer"
hide mcPic
"" "Než stihne Hayfa položit další otázku, do místnosti vejde vysoký, velmi dobře oblečený muž s listem papíru v ruce. Tázavě se na Hayfu podívá."
$ hayfa.say("Rauvine, máme tu nového rekruta. %(callingMc)s, tohle je Rauvin, velitelova pravá ruka.")
$ rauvin.say("Rauvin de Vito, těší mne, že tě poznávám.")
$ hayfa.say("Co zajímavého umíš? Mluvit s lidmi? Všímat si věcí? Bojovat?")
show mcPic at menuImage
menu:
    "Nejvíc si asi věřím v boji.":
        $ skill = "combat"
    "Není těžké si všímat věcí, když člověk ví, kam se dívat.":
        $ skill = "observation"
    "Lidé mi většinou mají sklony mi důvěřovat.":
        $ skill = "diplomacy"
hide mcPic
"" "Hayfa a Rauvin se na sebe krátce podívají, pak obrátí pozornost zpět k tobě a krátce přikývnou"
$ rauvin.say("Co tě vlastně přimělo hledat štěstí v hlídce?")
show mcPic at menuImage
menu:
    "Chci hlavně pomoct městu...":
        $ reasons = "altruist"
        hide mcPic
        $ hayfa.say("Škoda že takových jako ty není víc. Tohle město je potřebuje jako sůl.", "happy")
        "" "V Hayfiných tmavých očích probleskne zájem a snad i uznání"
        $ hayfa.trust += 1
        hide hayfa_happy
    "Myslím, že je důležité udržovat řád.":
        $ reasons = "order"
        hide mcPic
        $ rauvin.say("Řád je potřeba vždy a všude, ale tady v Marendaru myslím obzvlášť. Po třech převratech během jednoho roku si lidé opravdu zaslouží klid.")
        $ rauvin.trust += 1
    "Mám osobní důvody.":
        $ reasons = "personal"
        hide mcPic
        $ hayfa.say("Dobře, nebudu naléhat. Hlavní je, aby se ti dalo důvěřovat.")
"" "Najednou se rozrazí dveře a vstoupí očividně rozrušený muž, podle oděvu nejspíš bohatší obchodník nebo řemeslník."
$ victim.say("Okradli mě! Musíte to okamžitě vyšetřit! Okamžitě! Jestli můj výrobek nebude zpátky do dvou dnů…", "angry")
$ rauvin.say("Uklidněte se, pane (jméno). Co přesně se vám ztratilo?")
$ victim.say("Můj mistrovský kus! Na Einionovy slavnosti! Včera večer jsem se o něm zmínil před mistrem (hlava cechu), nejspíš se bojí o svou židli.", "angry")
"" "Hayfa mírně podezřívavě zvedne obočí."
$ hayfa.say("Při jaké příležitosti jste to zmínil?")
$ victim.say("Slavil jsem včera dokončení díla U (hospodský) a (hlava cechu) tam zrovna popíjel. Slovo dalo slovo…")
$ hayfa.say("A kolik dalších lidí vědělo i předtím, co vyrábíte? Učedníci, manželka, dodavatelé materiálu…?")
$ victim.say("Ti všichni, samozřejmě. Tak vyšetříte to?", "angry")
if gender == "M":
    $ hayfa.say("Máte štěstí. Toto je %(mcName)s. Přicestoval zdaleka, aby marendarské hlídce pomohl chránit bezpečí ve městě, a má přesně ty zkušenosti, jaké si váš případ zaslouží.")
else:
    $ hayfa.say("Máte štěstí. Toto je %(mcName)s. Přicestovala zdaleka, aby marendarské hlídce pomohla chránit bezpečí ve městě, a má přesně ty zkušenosti, jaké si váš případ zaslouží.")
"" "Rauvin po Hayfě střelí pohledem."
if gender == "M":
    $ rauvin.say("Bude se tomu věnovat osobně a zbavíme ho všech ostatních povinností, aby vyšetřování nic nepřekáželo. Jestli je vaše dílo ještě ve městě, najdeme ho.")
else:
    $ rauvin.say("Bude se tomu věnovat osobně a zbavíme ji všech ostatních povinností, aby vyšetřování nic nepřekáželo. Jestli je vaše dílo ještě ve městě, najdeme ho.")
"" "Hayfa se usměje a ukáže na jedny z dveří."
$ hayfa.say("Dejte se rovnou do toho. Támhleta místnost je volná, tam můžete, mistře (jméno), našemu vyšetřovateli říct vše důležité.")

scene bg interviewroom
"" "Vejdete to jednoduché místnosti se stolem a dvěma židlemi. (Jméno) se bez vyzvání posadí a významně se na tebe podívá."
label firstInterviewStart:
show mcPic at menuImage
menu:
    "Popište mi prosím všechno od začátku.":
        hide mcPic
        jump firstInterview1
    "Kdy jste přišel na to, že váš výrobek chybí?":
        hide mcPic
        jump firstInterview2
    "Můžete mi popsat ztracenou věc?" if "shoes description" not in clues:
        hide mcPic
        $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
        $ clues.append("shoes description")
        jump firstInterviewStart

label firstInterview1:
$ victim.say("Včera jsem střevíce dokončil, bylo to už dost k večeru. Tak jsem to šel oslavit (do hospody). Dobře jsme se bavili s (přítel), dokonce jsem na oslavu zaplatil rundu celé hospodě.")
$ victim.say("Ale pak se do toho vložil (hlava cechu). Že prý na vedení cechu nemám… jak on to… přístup. Otřásá se pod ním židle, tak by mě rád odstrašil.")
$ victim.say("Tak jsem si dal ještě něco na vztek… a pak mě (přítel) doprovodil domů a šel jsem rovnou spát.")
$ friendNote.isActive = True

label firstInterview2:
$ victim.say("Dnes ráno jsem šel zkontrolovat dílnu a kluky. Byl tam hrozný svinčík a moje nové střevíce byly pryč.", "angry")
$ victim.say("Kluky jsem seřval ať to tam rychle uklidí, ale ty střevíce musíte najít. Jinak nebudu mít co ukázat na slavnostech, navíc teď, když se budu ucházet o vedení cechu…")

$ flag = True
label firstInterviewReaction:
show mcPic at menuImage
menu:
    "Měl jste všechno nechat tak, jak to bylo." if flag is True:
        hide mcPic
        $ flag = False
        $ victim.say("To jsem tam měl nechat ten chlívek? To stejně nebude po zloději, takhle to tam vypadá vždycky, když jdu ven a nedohlídnu na to, aby tam kluci uklidili.", "angry")
        $ victim.trust -= 1
        jump firstInterviewReaction
    "Kdo jsou ti kluci?" if "boys" not in victimAsked:
        hide mcPic
        $ flag = False
        $ victim.say("Můj syn a učedníci. Jsou to všechno líná nemehla, ale když nad nimi člověk stojí s bičem, tak nějakou práci odvedou.")
        $ victimAsked.append("boys")
        $ sonNote.isActive = True
        $ apprentice1Note.isActive = True
        $ apprentice2Note.isActive = True
        jump firstInterviewReaction
    "Mám ještě další otázky.":
        hide mcPic
        $ victim.say("Jestli je to nutné…")
        jump firstInterviewQuestions
    "Děkuji, to je všechno.":
        hide mcPic

label whereToStart:
$ flag = ""
$ victim.say("Tak kde začnete?")
show mcPic at menuImage
menu:
    "Mohl bych vidět vaši dílnu?" if gender == "M":
        hide mcPic
        $ status.append("straight to workshop")
        jump workshopController
    "Mohla bych vidět vaši dílnu?" if gender == "F":
        hide mcPic
        $ status.append("straight to workshop")
        jump workshopController
    "Začnu (v hospodě)":
        hide mcPic
    "Půjdu si promluvit s (hlava cechu)":
        hide mcPic
        $ victim.trust += 1
        call guildmasterController
    "Půjdu si promluvit s (konkurent)" if competitorNote.isActive == True:
        hide mcPic
    "Rád bych si promluvil s (přítel)" if friendNote.isActive == True:
        hide mcPic
        call friendController
return

###

label firstInterviewQuestions:
    show mcPic at menuImage
    menu:
        "Můžete mi popsat ztracenou věc?" if "shoes description" not in clues:
            hide mcPic
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
            $ clues.append("shoes description")
        "Kdo další byl (v hospodě), kdo se mohl o vaše dílo zajímat?" if "people in pub" not in victimAsked:
            hide mcPic
            $ victim.say("Byla tam spousta lidí, ale většinu z nich zajímala jenom ta runda zdarma. Možná tam mohl být nějaký potulný tovaryš? Kvůli lidem jsem tam nešel.")
            $ victimAsked.append("people in pub")
        "Je někdo další, s kým máte spory?" if "enemies" not in victimAsked:
            hide mcPic
            $ victim.say("Kromě (hlavy cechu)? Z cechu ještě (konkurent), ten by se taky rád dostal do jeho čela. Nechápu, jak na to přišel, jeho práce nestojí za moc, ale nějakou podporu prý má.")
            $ victimAsked.append("enemies")
            $ competitorNote.isActive = True
        "Kdo všechno žije ve vaší domácnosti?" if "family" not in victimAsked:
            hide mcPic
            $ victimAsked.append("family")
            $ victim.say("No kdo asi. Moje rodina a mí učedníci. Naštěstí jen dva, už tak ta nemehla dělají až moc nepořádku.")
            $ mc.say("A rodina, to je kdo? Manželka a děti?")
            $ victim.say("Ano, manželka, syn a dcera. Ale ta vám moc nepomůže, ta o botách nic neví, kromě toho, kolik párů bych jí měl ušít.")
            $ wifeNote.isActive = True
            $ sonNote.isActive = True
            $ daughterNote.isActive = True
            $ apprentice1Note.isActive = True
            $ apprentice2Note.isActive = True
        "Je možné, že jste střevíce ráno přehlédl?" if "possible mistake?" not in victimAsked:
            hide mcPic
            $ victim.say("Jak bych mohl přehlédnout něco, co jsem nechal ležet uprostřed stolu v dílně? A kdyby je kluci uklidili, tak budou na čestném místě na polici, tam taky nejsou.", "angry")
            $ victim.trust -= 2
            $ victimAsked.append("possible mistake?")
        "Děkuji, to je všechno.":
            hide mcPic
            jump whereToStart
    jump firstInterviewQuestions
