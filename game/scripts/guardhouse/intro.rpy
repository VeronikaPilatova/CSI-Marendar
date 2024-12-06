label intro:
stop music fadeout 1.0

scene bg exterior01
"Ke strážnici marendarské hlídky přicházíš se zvláštní směsicí odhodlání a nejistoty. Co když tě nepřijmou? Nebo přijmou jen z nouze, kvůli nedostatku lidí?"
"Co je teď pro hlídku vůbec důležité, po dvou převratech během jednoho roku, před kterými skrz ni její elfí velitel vládl městu pevnou rukou? Dá se opravdu věřit tomu, že nové vedení ji přetváří do podoby, na kterou město může být hrdé?"
show bg door01
"Přede dveřmi na moment zaváháš, pak se ale narovnáš a zaklepeš."

"Otevře ti mladá žena v jednoduchém nebarveném oblečení. Z jejího vzhledu nelze vyčíst, zda je členkou hlídky, nebo obyčejnou chudší měšťankou - pouze odhaduješ, že když někdo s tesákem u pasu otevírá dveře strážnice, nejspíš do hlídky patří."
"Žena si tě rychle přeměří pohledem. Promluví věcně a trochu úsečně, ale ne nepřátelsky."
$ hayfa.say("Myslím, že se ještě neznáme. Jsem Hayfa. S čím může být hlídka nápomocná?")
$ mc.say("Hledám práci. Totiž... slyšel[a] jsem, že městská hlídka shání nové členy? Jmenuji se [mcName].")
if mcName == "Luisa" or mcName.startswith("Luisa "):
    "Může to být světlem, ale na moment se ti zdá, že se Hayfin výraz změní na téměř nepřátelský. Pak ale mrkneš a je to pryč."
$ hayfa.say("Je to tak, schopné nové členy potřebujeme. Teď obzvlášť, když za pár dní budou Einionovy slavnosti, na které přijede spousta kupců a kejklířů. Velitel bude nadšený. Pojď dál.")
"Hayfa tě nechá projít kolem sebe dovnitř a zavře za tebou dveře."
scene bg guardhouse
$ hayfa.say("Ale řekni mi nejdřív něco o sobě. Jsi z Marendaru?")
show mcPic at menuImage
menu:
    "Původem ano, ale dlouho jsem tu nebyl[a].":
        $ origin = "born here"
    "Mám tady rodinu.":
        $ origin = "family"
    "Přistěhoval[a] jsem se teprve nedávno.":
        $ origin = "newcomer"

hide mcPic
"Než stihne Hayfa položit další otázku, do místnosti vejde vysoký, velmi dobře oblečený muž s listem papíru v ruce. Tázavě se na Hayfu podívá."
$ hayfa.say("Rauvine, máme tu nového rekruta. [callingMc], tohle je Rauvin, velitelova pravá ruka.")
$ rauvin.say("Svobodný pán Rauvin de Vito, těší mne, že tě poznávám.")
"Hayfa se otočí zpět k tobě."
$ hayfa.say("Co zajímavého umíš? Mluvit s lidmi? Všímat si věcí? Bojovat?")
$ mc.say("Mám úhledný rukopis a výbornou paměť. Doufal[a] jsem, že ze mě jednou bude písař, ale neměl[a] jsem peníze na dokončení učení.")
$ mc.say("Kromě toho...")
show mcPic at menuImage
menu:
    "Nejvíc si asi věřím v boji.":
        $ skill = "combat"
    "Není těžké si všímat věcí, když člověk ví, kam se dívat.":
        $ skill = "observation"
    "Lidé mi většinou mají sklony důvěřovat.":
        $ skill = "diplomacy"
hide mcPic
"Hayfa a Rauvin se na sebe krátce podívají, pak obrátí pozornost zpět k tobě a krátce přikývnou."
$ hayfa.say("Dobrá. Kde bydlíš a čím ses zatím živil[a]?")
$ mc.say("Bydlím na půdě u vdovy Gertrudy a živím se porůznu, čím se zrovna naskytne.")
show mcPic at menuImage
menu:
    "Chtěl[a] bych práci, kde můžu udělat něco dobrého.":
        hide mcPic
        $ personality.append("motivation: positive change")
        $ rauvin.say("Toho se jistě dá dosáhnout i jinak. Co tě přimělo hledat štěstí právě v hlídce?")
    "Myslím, že mám na víc.":
        hide mcPic
        $ personality.append("motivation: ambition")
        $ rauvin.say("Jistě se můžeš prokázat i jinak. Co tě přimělo hledat štěstí právě v hlídce?")
    "Líbilo by se mi něco jistějšího.":
        hide mcPic
        $ personality.append("motivation: money")
        $ rauvin.say("Jistě si lze vydělávat i jinak. Co tě přimělo hledat štěstí právě v hlídce?")
show mcPic at menuImage
menu:
    "Chci pomoct městu.":
        $ reasons = "altruist"
        hide mcPic
        $ hayfa.say("Takových bychom potřebovali co nejvíc. Tohle město už toho zažilo až moc.", "happy")
        "V Hayfiných tmavých očích probleskne zájem a snad i stopa naděje."
        $ hayfa.trust += 1
        hide hayfa_happy
    "Myslím, že je důležité udržovat řád.":
        $ reasons = "order"
        hide mcPic
        $ rauvin.say("Řád je potřeba vždy a všude, ale tady v Marendaru myslím obzvlášť. Po dvou převratech během jednoho roku si lidé opravdu zaslouží klid.")
        $ rauvin.trust += 1
    "Mám osobní důvody.":
        $ reasons = "personal"
        hide mcPic
        $ hayfa.say("Dobře, nebudu naléhat. Ale nezapomeň, že ti tady potřebujeme důvěřovat.")
    "Jestli jsou i lepší možnosti, tak já o nich nevím, zatímco tady prý máte podstav. Tak jsem tady.":
        $ reasons = "none special"
        hide mcPic
        $ rauvin.say("Tomu rozumím, ale pracovat v hlídce bez nadšení pro tu práci jako takovou by nemuselo dopadnout dobře.")
"Najednou se rozrazí dveře a vstoupí očividně rozrušený muž, podle oděvu nejspíš bohatší obchodník nebo řemeslník."
$ victim.say("Okradli mě! Musíte to okamžitě vyšetřit! Okamžitě! Jestli můj výrobek nebude zpátky do tří dnů...", "angry")
$ rauvin.say("Uklidněte se, mistře Heinrichu. Co přesně se vám ztratilo?")
$ victim.say("Můj mistrovský kus! Na Einionovy slavnosti! Včera večer jsem se o něm zmínil před mistrem Rumelinem, nejspíš se bojí o svou židli v čele cechu.", "angry")
"Hayfa mírně podezřívavě zvedne obočí."
$ hayfa.say("Při jaké příležitosti jste to zmínil?")
$ victim.say("Slavil jsem včera dokončení díla U Salmy a Rumelin tam zrovna popíjel. Slovo dalo slovo…")
$ hayfa.say("A kolik dalších lidí vědělo i předtím, co vyrábíte? Učedníci, manželka, dodavatelé materiálu…?")
$ victim.say("Ti všichni, samozřejmě. Tak vyšetříte to?", "angry")
$ hayfa.say("Máte štěstí. Toto je [mcName]. Přicestoval[a] zdaleka, aby marendarské hlídce pomohl[a] chránit bezpečí ve městě, a má přesně ty zkušenosti, jaké si váš případ zaslouží.", "happy")
"Rauvin po Hayfě střelí pohledem."
$ rauvin.say("Bude se tomu věnovat osobně a zbavíme [pronoun4] všech ostatních povinností, aby vyšetřování nic nepřekáželo. Jestli je vaše dílo ještě ve městě, najdeme ho.")
"Hayfa se usměje a ukáže na jedny z dveří."
$ hayfa.say("Dejte se rovnou do toho. Támhleta místnost je volná, tam můžete, mistře Heinrichu, našemu vyšetřovateli říct vše důležité.")

scene bg interviewroom
"Vejdete to jednoduché místnosti se stolem a dvěma židlemi. Mistr Heinrich se bez vyzvání posadí a významně se na tebe podívá."
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
        $ victim.asked.append("shoes description")
        jump firstInterviewStart

label firstInterview1:
$ victim.say("Včera jsem střevíce dokončil, bylo to už dost k večeru. Tak jsem to šel oslavit k Salmě. Dobře jsme se bavili s Eckhardem, dokonce jsem na oslavu zaplatil rundu celé hospodě.")
$ victim.say("Ale pak se do toho vložil Rumelin. Že prý na vedení cechu nemám… jak on to… přístup. Otřásá se pod ním židle, tak by mě rád odstrašil.")
$ victim.say("Tak jsem si dal ještě něco na vztek… a pak mě Eckhard doprovodil domů a šel jsem rovnou spát.")
$ time.addMinutes(8)
$ eckhardNote.isActive = True
if "Eckhard" not in clues:
    $ clues.append("Eckhard")

label firstInterview2:
$ victim.say("Dnes ráno jsem šel zkontrolovat dílnu a kluky. Byl tam hrozný svinčík a moje nové střevíce byly pryč.", "angry")
$ victim.say("Kluky jsem seřval, ať to tam rychle uklidí, ale ty střevíce musíte najít. Jinak nebudu mít co ukázat na slavnostech, navíc teď, když se budu ucházet o vedení cechu…")

$ flag = True
label firstInterviewReaction:
show mcPic at menuImage
menu:
    "Měl jste všechno nechat tak, jak to bylo." if "disturbed crime scene" not in victim.asked:
        hide mcPic
        $ victim.asked.append("disturbed crime scene")
        $ victim.say("To jsem tam měl nechat ten chlívek? To stejně nebude po zloději, takhle to tam vypadá vždycky, když jdu ven a nedohlídnu na to, aby tam kluci uklidili.", "angry")
        $ victim.trust -= 1
        jump firstInterviewReaction
    "Kdo jsou ti kluci?" if "boys" not in victim.asked:
        hide mcPic
        $ flag = False
        $ victim.say("Můj syn a učedníci. Jsou to všechno líná nemehla, jeden horší než druhý.")
        $ mc.say("I váš syn?")
        $ victim.say("Ten je ze všech nejhorší. Ti dva odvedou nějakou rozumnou práci, aspoň když nad nima člověk stojí s bičem, ale Aachim… Vážně nevím, komu tu dílnu jednou předám.")
        $ victim.asked.append("boys")
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
$ time.addMinutes(len(victim.asked)* 4)
$ victim.say("Tak kde začnete?")
show mcPic at menuImage
menu:
    "Mohl[a] bych vidět vaši dílnu?":
        hide mcPic
        $ status.append("straight to workshop")
        jump workshopController
    "Začnu U Salmy":
        hide mcPic
        jump pubController
    "Půjdu si promluvit s mistrem Rumelinem":
        hide mcPic
        $ victim.trust += 1
        jump rumelinController
    "Půjdu si promluvit s mistrem Kasparem" if kasparNote.isActive == True:
        hide mcPic
        jump kasparController
    "Rád[a] bych si promluvil[a] s Eckhardem" if eckhardNote.isActive == True:
        hide mcPic
        jump eckhardController
return

###

label firstInterviewQuestions:
    show mcPic at menuImage
    menu:
        "Můžete mi popsat ztracenou věc?" if "shoes description" not in clues:
            hide mcPic
            $ victim.asked.append("shoes description")
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
            $ clues.append("shoes description")
        "Kdo další byl U Salmy, kdo se mohl o vaše dílo zajímat?" if "people in pub" not in victim.asked:
            hide mcPic
            $ victim.say("Byla tam spousta lidí, ale většinu z nich zajímala jenom ta runda zdarma. Možná tam mohl být nějaký potulný tovaryš? Kvůli lidem jsem tam nešel.")
            $ victim.asked.append("people in pub")
        "Je někdo další, s kým máte spory?" if "enemies" not in victim.asked:
            hide mcPic
            $ victim.say("Kromě Rumelina? Z cechu ještě Kaspar, ten by se taky rád dostal do jeho čela. Nechápu, jak na to přišel, jeho práce nestojí za moc, ale nějakou podporu prý má.")
            $ victim.asked.append("enemies")
            $ kasparNote.isActive = True
        "Kdo všechno žije ve vaší domácnosti?" if "family" not in victim.asked:
            hide mcPic
            $ victim.asked.append("family")
            $ victim.say("No kdo asi. Moje rodina a mí učedníci. Naštěstí už jen dva, už tak ta nemehla dělají až moc nepořádku.")
            $ mc.say("A rodina, to je kdo? Manželka a děti?")
            $ victim.say("Ano, manželka, syn a dcera. Ale ta vám moc nepomůže, ta o botách nic neví, kromě toho, kolik párů bych jí měl ušít.")
            call unlockFamily
        "Je možné, že jste střevíce ráno přehlédl?" if "possible mistake?" not in victim.asked:
            hide mcPic
            $ victim.say("Jak bych mohl přehlédnout něco, co jsem nechal ležet uprostřed stolu v dílně? A kdyby je kluci uklidili, tak budou na čestném místě na polici, tam taky nejsou.", "angry")
            $ victim.trust -= 2
            $ victim.asked.append("possible mistake?")
        "Děkuji, to je všechno.":
            hide mcPic
            jump whereToStart
    jump firstInterviewQuestions

label unlockFamily:
    $ lisbethNote.isActive = True
    $ sonNote.isActive = True
    $ adaNote.isActive = True
    $ apprentice1Note.isActive = True
    $ apprentice2Note.isActive = True
    return
