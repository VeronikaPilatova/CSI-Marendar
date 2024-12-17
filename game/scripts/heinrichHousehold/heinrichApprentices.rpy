label boysMain:
    $ sonNote.isActive = True
    $ apprentice1Note.isActive = True
    $ apprentice2Note.isActive = True
    $ lastSpokenWith = "boys"
    $ heinrichHouseholdSpokenWith.append("boys")

    $ origAsked = boysAsked.copy()
    if "boys met" not in status:
        call boysFirst
    else:
        call boysAgain
    call boysOptions

    # adjust time spent and status
    $ time.addMinutes((len(boysAsked) - len(origAsked)) * 4)
    if "boys seen" in status:
        $ status.remove("boys seen")
    $ status.append("boys met")
    if "Heinrich sent away" in boysAsked:
        $ boysAsked.remove("Heinrich sent away")
    if "no privacy" in status:
        $ status.remove("no privacy")
    if currentLocation == "victim house":
        jump victimHouseholdConversationEnded
    return

label boysFirst:
    "Kluci se po sobě podívají a nakonec promluví ten nejstarší z nich."
    $ son.say("Prý vám máme nějak pomoct s vyšetřováním? Jsem Aachim, syn mistra Heinricha.")
    $ son.say("A tohle jsou Ferdi a Rudi.")
    $ yesman.say("Dobrý den.")
    $ optimist.say("Co pro vás můžeme udělat?")
    return

label boysAgain:
    $ optimist.say("Máte něco nového? Pokrok v pátrání?")
    $ mc.say("Chtěl[a] jsem se vás ještě zeptat na pár věcí.")
    $ son.say("Ale my už jsme vám řekli všechno, co víme.")
    if "no privacy" in status:
        "Heinrich Aachima zpraží pohledem a ten nervózně uhne očima."
    $ son.say("Ale samozřejmě se pokusíme pomoct.")
    $ yesman.say("Jak jenom budeme moct.")
    return

label boysOptions:
    call boysOptionsRemainingCheck
    if boysOptionsRemaining == 0:
        $ mc.say("To je všechno, můžeš zase jít.")
        call boysReleased
        return

    show mcPic at menuImage
    menu:
        "Byl někdo po odchodu mistra Heinricha v jeho dílně?" if "workshop empty" not in boysAsked:
            hide mcPic
            $ boysAsked.append("workshop empty")
            $ son.say("Nebyl.")
            $ yesman.say("Samozřejmě, že nebyl.")
            $ optimist.say("Mistr ji po odchodu zamknul.")
            $ mc.say("Zamkl i vchod z domu?")
            if "no privacy" in status:
                "Aachim se krátce podívá na svého otce, který stojí kousek stranou se zamračeným výrazem."
            $ son.say("...nevím.")
            $ mc.say("Zamyká ho obvykle?")
            $ son.say("...obvykle ne.")
            $ optimist.say("Ale stejně tam nikdo nesmí.")
            $ yesman.say("Mistr tam má svoje nástroje a rozdělanou práci.")
        "Co jste včera večer dělali vy?" if "evening activities" not in boysAsked:
            hide mcPic
            $ boysAsked.append("evening activities")
            $ optimist.say("Uklidili jsme dílnu a pak si šli lehnout.")
            $ yesman.say("Potom jsme šli rovnou spát.")
            "Aachim přikyvuje."
            if "no privacy" in status:
                $ optimist.say("Mistr nás… vede k tomu, abychom brzo vstávali. Ranní ptáče, využívání denního světla a tak.")
            else:
                $ optimist.say("Mistr nás nutí brzo vstávat.")
            $ mc.say("V kolik hodin jste asi skončili s úklidem?")
            $ son.say("To nevím.")
            $ optimist.say("Byli jsme potom tak unavení, že jsme čas ani nezjišťovali.")
        "Pamatujete si na ty učedníky, které váš mistr propustil?" if "enemies" in rumelin.asked and "fired apprentices" not in boysAsked:
            hide mcPic
            $ boysAsked.append("fired apprentices")
            if "no privacy" in status:
                $ son.say("Samozřejmě. Myslím, že se teď mají dobře.")
                "Opodál stojící Heinrich svého syna zpraží pohledem a Aachim zmlkne, ale nevypadá, že by chtěl měnit názor."
                $ optimist.say("...jak jenom můžou. Sigi a Gerd mají nové mistry, to je aspoň něco. Zeran samozřejmě ne…")
                $ son.say("Ten dělal oči na Adu, ten si nic dobrého nezaslouží.", "angry")
            else:
                $ son.say("Samozřejmě. Ti, kteří se odsud mohli dostat.")
                $ mc.say("Jak to myslíš?")
                $ son.say("Že všichni měli vlastně štěstí.")
                $ optimist.say("Možná kromě Zerana…", "sad")
                $ son.say("Ten dělal oči na Adu, ten si štěstí nezaslouží.", "angry")
            $ clues.append("Zeran offense")
        "Víte, kde je najít?" if "fired apprentices" in boysAsked and "fired apprentices" not in clues:
            hide mcPic
            $ clues.append("fired apprentices")
            $ son.say("Gerd je v učení u mistra Njala a Sigi odešel do Sehnau.")
            $ optimist.say("A Zeran teď prý je někde v Dočasné čtvrti.")
            $ yesman.say("Chytil se tam špatné společnosti.")
            $ son.say("Vrána k vráně.", "angry")
            if "no privacy" in status:
                "Všimneš si, že mistr Heinrich bezděčně přikývne."
            $ mc.say("Jaké špatné společnosti?")
            $ yesman.say("Prostě špatné. Všichni to říkají.")
            $ optimist.say("Možná v té ubytovně, jak ji vede ten podezřelý kazatel?")
            if "no privacy" in status:
                $ optimist.say("Ale tam to samozřejmě nikdo z nás nezná.")
                $ yesman.say("My tam nechodíme.")
            $ gerdNote.isActive = True
            $ zeranNote.isActive = True
        "Kdy jste se naposled viděli se Zeranem nebo Gerdem?" if "fired apprentices" in clues and "fired apprentices contacts" not in boysAsked:
            hide mcPic
            $ boysAsked.append("fired apprentices contacts")
            $ son.say("Zerana jsem neviděl od toho dne, kdy odtud vypadl, a doufám, že to tak i zůstane.", "angry")
            $ yesman.say("Také jsem ho dlouho neviděl.")
            $ optimist.say("Před pár dny jsem ale viděl Gerda. Šel jsem pro nějaké věci k panu Rovienovi a potkal jsem ho tam. Vypadal spokojeně.")
            if "no privacy" not in status:
                $ son.say("Aby ne.", "angry")
            $ optimist.say("Prý ho mistr Njal dokonce poslouchá, když má nějaký nápad. A když to je hloupost, tak mu to vysvětlí.")
            $ yesman.say("Mistr Heinrich říkal, že se tam Gerd naučí jen ztrácet čas.")
            if "no privacy" in status:
                "Aachim obrátí oči v sloup, ale nic neřekne."
            else:
                $ son.say("On říká spoustu věcí.", "angry")
            $ yesman.say("Také říkal, že to vlastně Gerd už teď umí až moc dobře, takže se tam nenaučí vůbec nic.")
            $ optimist.say("Rudi, neviděl ty ses s Gerdem před pár dny také?")
            $ yesman.say("No, jo. Ale nic zajímavého neříkal.")
            $ yesman.say("Mluvili jsme hlavně o holkách.", "blushing")
            $ yesman.say("Prý se určitě líbí hrnčířovic Mirce, ale podle mě si vymýšlí. Vždyť je o rok mladší než ona.")
            $ son.say("Já se s ním moc nevídám. Přeci jen odešel z dílny mého otce, je to trochu nepříjemné.")
        "Gerd prý byl v noci tady v dílně, když se ty boty ztratily. Víte o tom něco?" if "fired apprentices" in clues and "which apprentice" in liese.asked and "Gerd in workshop" not in boysAsked:
            hide mcPic
            $ boysAsked.append("Gerd in workshop")
            if "no privacy" in status:
                $ optimist.trust -= 2
                $ yesman.trust -= 2
                $ son.trust -= 2
                $ ada.trust -= 2
                "Učedníci se po sobě překvapeně podívají, než však stihnou odpovědět, ozve se jejich mistr."
                $ victim.say("Jak, že byl tady v dílně? Co si dovoluje sem lézt?", "angry")
                $ optimist.say("Víte to jistě?", "surprised")
                show mcPic at menuImage
                menu:
                    "Nevím, proto se vás ptám.":
                        hide mcPic
                        $ victim.trust -= 1
                        $ optimist.say("No já ho tady rozhodně neviděl.")
                        $ yesman.say("Ani já.")
                        $ son.say("Já také ne.")
                        $ victim.say("Tak kdo s tím tedy přišel?", "angry")
                        $ son.say("Někdo se musel splést.")
                        $ yesman.say("Proč by sem chodil? U mistra Njala mu je dobře.")
                        $ optimist.say("... protože se tam může jít vyspat po dni plném dřiny, takže určitě nebude někde trajdat. To jsi chtěl říct, že jo?")
                        $ yesman.say("... ano, přesně to.")
                        $ victim.say("Tak proč tady řešíme něco, co nikdo neviděl a co ani nedává smysl, aby se stalo? Všichni máme důležitější práci než tohle.", "angry")
                    "Gerd to sám přiznal." if "stolen idea" in clues:
                        hide mcPic
                        $ boysAsked.append("Gerd in workshop - confession")
                        $ victim.say("A ještě má tu drzost to přiznat!", "angry")
                        call heinrichLearnsAboutGerdInWorkshop
                    "Viděla ho jedna ze sousedek.":
                        hide mcPic
                        $ victim.say("Která?", "angry")
                        show mcPic at menuImage
                        menu:
                            "Lotte.":
                                hide mcPic
                                $ victim.say("Tak to ses nechal nachytat. Je to drbna a navíc mě nemá ráda.", "angry")
                                $ victim.say("Radši jdi po nějaké lepší stopě.")
                                jump boysOptions
                            "Liese.":
                                hide mcPic
                                $ victim.say("To dává smysl, pořád jí řve děcko, tak může v noci koukat z okna.", "angry")
                            "To musím nechat v tajnosti.":
                                hide mcPic
                                $ victim.say("Stejně na tom nezáleží, jsou jedna jako druhá.", "angry")
                        call heinrichLearnsAboutGerdInWorkshop
            else:
                "Učedníci se po sobě překvapeně podívají."
                $ yesman.say("Co by tady dělal?", "surprised")
                $ optimist.say("Není to nějaká mýlka?", "surprised")
                $ mc.say("Viděla ho jedna ze sousedek.")
                $ optimist.say("To se musela splést. Většinu večera jsme tu… uklízeli a Gerd sem rozhodně nepřišel. To bychom si pamatovali.")
                $ yesman.say("No, mně se některé věci trochu ztrácejí...")
                $ optimist.say("Tohle bychom nezapomněli.")
                $ son.say("Myslíte... že by mohl Gerd stát za tou krádeží?", "surprised")
                show mcPic at menuImage
                menu:
                    "Připadá mi to pravděpodobné.":
                        hide mcPic
                        $ son.trust -= 1
                        $ optimist.trust -= 1
                        $ yesman.trust -= 1
                        $ optimist.say("Ale proč? Vždyť by tím nic nezískal.", "surprised")
                        $ mc.say("Určité indicie k němu vedou. Další vyšetřování stále může ukázat, že je nevinný. Nebo také ne.")
                    "Spíše tomu nevěřím.":
                        hide mcPic
                    "Teprve se snažím udělat si obrázek.":
                        hide mcPic
                    "To je podrobnost případu, kterou nemůžu říkat.":
                        hide mcPic
                "Učedníci si vymění pohledy a trochu nervózně pokývnou."
                $ optimist.say("Ale vážně nevidím důvod, proč by Gerd ty boty kradl.")
                $ yesman.say("Přesně. Vždyť by mu ani nebyly.")
                $ yesman.say("Jedině že by je chtěl dát nějaké holce...")
                $ yesman.say("Ale to by neudělal.")
                $ son.say("Možná kdyby byl pod nějakým tlakem.")
                $ optimist.say("To jedině. Ale co já vím, žije se mu teď dobře.")
        "Jak dlouho jste u mistra Heinricha?" if "how long here" not in boysAsked:
            hide mcPic
            $ boysAsked.append("how long here")
            $ optimist.say("Já asi čtyři roky.")
            $ yesman.say("Já asi o dva měsíce méně.")
            $ son.say("Já celý svůj život. Neměl jsem příliš na výběr.", "sad")
            if "no privacy" in status:
                "Mistr Heinrich syna probodne pohledem, ale jakoukoli poznámku nakonec spolkne."
        "Znamená to, že tady nechceš být?" if "how long here" in boysAsked and "no privacy" not in status:
            hide mcPic
            $ son.say("Nikdo příčetný by tady nechtěl být, i myši se tátově dílně radši vyhýbají obloukem.", "angry")
            $ optimist.say("Ty máš aspoň zajištěnou budoucnost.")
            $ son.say("Jo, to mám.", "sad")
            $ mc.say("To přece není důvod ke smutku?")
            if son.trust < 2:
                $ son.say("Samozřejmě ne. Občas mám trochu závrať z toho, jak velký to je závazek, to je všechno. Jiného dědice táta nemá.")
            else:
                $ son.say("Všichni mi říkají, jak mám být hrozně vděčný. Táta nejvíc. Budu mít celý život slušný výdělek, tak na co si stěžuju? Ale mě celá ta ševcovina prostě hrozně štve.", "angry")
                $ son.say("Ale spousta lidí by byla vděčná za kousek toho, co mám já, a stejně nic jiného neumím a ani nevím, co bych umět chtěl, takže budu celý život dělat řemeslo, které jsem si nevybral a které bych nejradši už nikdy neviděl.", "sad")
                $ son.say("A budu si připadat hloupě, že mám hezký dům a spoustu jídla, ale stejně mi to nestačí.", "sad")
                "Rudi a Ferdi na se Aachima zaraženě dívají."
                $ son.say("Ale teď zním jako nevděčník a to není správné. Samozřejmě, že tady chci být. Ať žije šití bot.")
        "Kdo obvykle vynáší smetí z dílny?" if "anything else" in liese.asked or erleNote.isActive == True:
            hide mcPic
            $ son.say("Teď už zase Rudi. Je tu nejkratší dobu.")
            $ optimist.say("Donedávna to dělal Gerd, ale ten je teď u mistra Njala.")
            if "no privacy" not in status:
                $ son.say("A má se tam mnohem líp, než my tady.")
                $ yesman.say("Stejně si myslím, že bychom se měli střídat.", "angry")
                $ optimist.say("Smůla. Dělá to vždy ten, co je v dílně nejkratší dobu. A to jsi ty.", "happy")
                $ yesman.say("Jestli mě budeš hodně štvát, tak odtud odejdu a pak uvidíš, jaké to je, být zase ten otloukánek.", "angry")
                $ son.say("Nepřeháněj, je to jenom vynášení smetí.")
                $ optimist.say("Neměli bychom se vrátit k případu? Nechceme zdržovat hlídku.")
        "Mohl by tenhle kousek stuhy být od ztracených střevíců?" if "burned evidence" in clues and "burned evidence seen" not in boysAsked:
            hide mcPic
            $ boysAsked.append("burned evidence seen")
            $ son.pressure += 2
            $ optimist.pressure += 2
            $ yesman.pressure += 2
            if "no privacy" in status and "burned evidence seen" in victim.asked:
                "Mistr Heinrich se na stuhu podívá jako první, ale když neuvidí nic nového, zaměří se místo toho na kluky. Ti si ohořelý útržek zmateně prohlédnou, ale často se u toho vrací pohledem k zamračenému Heinrichovi."
                $ optimist.say("To vypadá...", "surprised")
                $ yesman.say("...to fakt vypadá jako kus těch bot...", "surprised")
                $ optimist.say("...ale jak? To přece nedává smysl...", "surprised")
                $ son.say("Kde jste to na[sel]?", "surprised")
                $ optimist.say("Vždyť ty boty byly tady na stole, úplně v pořádku.", "surprised")
                $ mc.say("Na[sel] jsem to v krbu tady v dílně. A doufal[a] jsem, že co se tomu stalo, mi řeknete vy.")
                $ victim.say("Víte o tom něco?", "angry")
                "Všichni tři kluci s vyděšeným výrazem zavrtí hlavou."
                $ son.say("Ne... ne, opravdu.", "surprised")
                $ yesman.say("Taky ne.", "surprised")
                $ optimist.say("To bude asi... nějaký zbytek z výroby? Odstřižek, možná?", "surprised")
                $ victim.say("A proč by potom byl v krbu, když všechny odstřižky měly být už nejmíň týden uklizené?", "angry")
                $ optimist.say("...nevím. Mohl někam zapadnout?", "surprised")
                $ victim.say("Takže neuklízíte. To si s váma ještě vyřídím.", "angry")
                $ victim.say("Chcete se jich ptát ještě na něco, nebo se už můžou vrátit k pořádné práci?", "angry")
            elif "no privacy" in status and "burned evidence seen" not in victim.asked:
                "Jakmile mistr Heinrich uslyší tvou otázku, odstrčí učedníky z cesty a málem ti kousek stuhy vytrhne z ruky."
                call burnedEvidenceSeenVictim
                "Heinrich se významně podívá na kluky, kteří vás pozorují s vyděšenými výrazy."
                $ victim.say("Vy o tom něco víte?", "angry")
                $ son.say("Ne… ne, opravdu.", "surprised")
                $ yesman.say("Taky ne.", "surprised")
                $ optimist.say("To bude asi... nějaký zbytek z výroby? Odstřižek, možná?", "surprised")
                $ victim.say("A proč by potom byl v krbu, když všechny odstřižky měly být už nejmíň týden uklizené?", "angry")
                $ optimist.say("...nevím. Mohl někam zapadnout?", "surprised")
                $ victim.say("Takže neuklízíte. To si s váma ještě vyřídím.", "angry")
                $ victim.say("Chcete se jich ptát ještě na něco, nebo se už můžou vrátit k pořádné práci?", "angry")
            else:
                call burnedEvidenceSeenBoys
        "Co víte o ztracených lahvích vína?" if "anything suspicious" in lisbeth.asked and "lost bottles 1" not in boysAsked:
            hide mcPic
            $ boysAsked.append("lost bottles 1")
            $ optimist.say("Vůbec nic!")
            $ yesman.say("Přesně. Ani kousek.")
            $ son.say("Nemáme s tím nic společného.")
            $ optimist.say("Proč bychom o tom měli něco vědět?")
            $ yesman.say("Za pití jeho vína by nás mistr přizabil.")
            $ optimist.say("Jaké ztracené lahve, vlastně?")
            $ yesman.say("Snad ne ty ze zásoby pana mistra!")
            $ mc.say("Ano, lahve, které má mistr Heinrich schované pro přátele a významné návštěvy.")
            $ yesman.say("Tak o těch už vůbec nic nevíme.")
            $ son.say("Bohužel. Pořád nic.")
        "Kdo jiný potom všechno to víno vypil?" if "lost bottles 1" in boysAsked and "lost bottles 2" not in boysAsked:
            hide mcPic
            $ boysAsked.append("lost bottles 2")
            $ son.say("Táta, samozřejmě. Nejspíš i s Eckhardem.")
            if "drunkard" in ada.asked:
                $ mc.say("A oni i uklidili prázdné lahve? Ada říkala, že mistr Heinrich po sobě obvykle neuklízí.")
                $ son.say("Ada tomu nerozumí.")
                if "coming home" in lisbeth.asked:
                    $ mc.say("Navíc Mistr Heinrich přišel z hospody a šel rovnou do postele. Kdyby pili ještě doma, určitě by si toho všimla tvoje matka.")
            elif "coming home" in lisbeth.asked:
                $ mc.say("Navíc Mistr Heinrich přišel z hospody a šel rovnou do postele. Kdyby pili ještě doma, určitě by si toho všimla tvoje matka.")
            if "drunkard" in ada.asked or "coming home" in lisbeth.asked:
                $ son.say("Hm… nemohli si něco vzít s sebou ven? Aby nikoho nevzbudili?")
                $ mc.say("To mistr Heinrich obvykle dělá?")
                $ optimist.say("No obvykle ne, ale včera zrovna třeba mohl?")
                if "drunkard" in ada.asked:
                    $ yesman.say("A lahve by potom zůstaly venku.")
        "Co že jste dnes tak unavení?" if "lost bottles 1" in boysAsked and "lost bottles 3" not in boysAsked and time.days == 1:
            call boysTired
        "Co že jste [investigationStart] byli tak unavení?" if "lost bottles 1" in boysAsked and "lost bottles 3" not in boysAsked and time.days != 1:
            call boysTired
        "Takže se shodneme, že jste zásoby mistra Heinricha vypili vy?" if "lost bottles 2" in boysAsked and "lost bottles 3" in boysAsked and "confession" not in boysAsked:
            hide mcPic
            $ boysAsked.append("confession")
            $ optimist.say("...", "surprised")
            $ yesman.say("...", "surprised")
            $ son.say("... tak trochu?", "surprised")
            $ optimist.say("Trochu jsme upili, ale to přece skoro nemůže být poznat.", "surprised")
            $ mc.say("Paní Lisbeth říkala něco o polovině zásob.")
            "Kluci se po sobě vyděšeně podívají."
            $ optimist.say("Byl bych přísahal, že to nebyla víc než jedna láhev!", "surprised")
            $ yesman.say("Tolik jsme toho přece nemohli zvládnout!", "surprised")
            $ optimist.say("To se hlavně nesmí dozvědět mistr. Ten by nás zabil.", "surprised")
            $ yesman.say("A vyhodil.", "surprised")
            $ son.say("A mě dvakrát.", "surprised")
            $ optimist.say("Neřeknete mu to, že ne?", "surprised")
            show mcPic at menuImage
            menu:
                "Neřeknu, ale stejně na to brzy přijde.":
                    hide mcPic
                    $ mc.say("Co kdybyste se rovnou přiznali? To by mohla být polehčující okolnost.")
                    $ son.say("To pochybuju. Stejně by táta hrozně zuřil a my bychom byli hned po ruce.", "sad")
                    $ yesman.say("A potom by nás vyhodil.", "surprised")
                    $ son.say("A my bychom pak byli bez peněz na další učení, a i kdybychom peníze někde sebrali, nikdo by nás nepřijal. Pořád jsme učedníci, co něco vzali vlastnímu mistrovi. Nebo vlastnímu otci.", "sad")
                "Pochopitelně řeknu. Musím hlásit pokrok v pátrání.":
                    hide mcPic
                    $ optimist.say("Ale on nás pak vážně vyhodí!", "surprised")
                    $ son.say("A my zůstaneme bez peněz na další učení, a i kdybychom peníze někde sebrali, nikdo by nás nepřijal. Pořád jsme učedníci, co něco vzali vlastnímu mistrovi. Nebo vlastnímu otci.", "sad")
            $ optimist.say("Co teď ale máme dělat? Dovedete si představit, jak se asi vede někomu, kdo se neměl šanci vyučit? Jaké má šanci sehnat živobytí?", "sad")
            show mcPic at menuImage
            menu:
                "Dovedu, ale můžu s tím něco udělat?":
                    hide mcPic
                    $ optimist.say("Nemohl to víno třeba ukrást ten stejný zloděj, který ukradl mistrovy boty?")
                    $ mc.say("Chcete, abych váš průšvih hodil na někoho nevinného?")
                    $ optimist.say("No když to je zloděj...")
                    $ son.say("Mně se to nějak nezdá.", "sad")
                    $ optimist.say("Nebo si třeba s mistrem můžete zkusit promluvit?")
                    $ mc.say("Možná. Nevím, jestli to k něčemu povede.")
                    $ mc.say("Můžu zkusit být na pozoru, jestli se objeví nějaká příležitost.")
                "Někdo si nezaslouží nic jiného.":
                    hide mcPic
                    $ son.trust -= 2
                    $ optimist.trust -= 2
                    $ yesman.trust -= 2
                    $ optimist.say("Někdo možná, ale my? Vždyť jsme neudělali nic tak hrozného.", "surprised")
                    $ mc.say("Je to krádež. Zneužití důvěry někoho, kdo vás vzal pod svou střechu.")
                    $ optimist.say("Ale...", "surprised")
                    $ son.say("No, je dobré vědět, na čem jsme.", "sad")
                "Až moc dobře. Jestli můžu pomoct, aby vás to nepotkalo, tak to udělám.":
                    hide mcPic
                    $ son.trust += 1
                    $ optimist.trust += 1
                    $ yesman.trust += 1
                    $ optimist.say("Opravdu? To jste úžasn[y]!", "surprised")
                    if victim.trust < 4:
                        $ mc.say("Nemůžu slíbit, že se to podaří, mé slovo u mistra Heinricha nemá velkou váhu.")
                    else:
                        $ mc.say("Nemůžu slíbit, že se to podaří. S mistrem Heinrichem sice vycházím celkem dobře, ale tolik na mě zase nedá.")
                    $ optimist.say("I tak jsme vám vděční.", "happy")
                    $ yesman.say("Děkujeme.", "happy")
                    $ son.say("A jestli se to nepodaří, aspoň už ze mě táta nebude moct být znovu zklamaný.")
        "Když jste v dílně uklízeli, boty v ní pořád byly?" if "confession" in kaspar.asked and "shoes in workshop" not in boysAsked:
            hide mcPic
            $ boysAsked.append("shoes in workshop")
            $ optimist.say("Jo, určitě.")
            $ yesman.say("Ty bychom nepřehlédli.")
            $ mc.say("A když jste šli spát, tak taky?")
            $ son.say("Samozřejmě. Proč se ptáte?")
            $ mc.say("Snažím se přijít na to, kdy přesně zmizely.")
            $ mc.say("Jeden můj svědek tvrdí, že v dílně nebyly ještě než se mistr Heinrich vrátil od Salmy.")
            if "no privacy" in status:
                $ victim.say("Co to je za svědka? Jestli se mi někdo coural do dílny, tak mě to rozhodně zajímá.", "angry")
                label workshopWitnessMenu1:
                show mcPic at menuImage
                menu:
                    "Mistr Kaspar":
                        hide mcPic
                        label workshopWitnessMenu2:
                        if "secret lover identity" in victim.asked:
                            $ victim.say("Ten zmetek! Nejenom, že mi chodí za ženou, ale ještě si dávají dostaveníčka v mé vlastní dílně?", "furious")
                            show mcPic at menuImage
                            menu:
                                "Nebylo na tom nic milostného":
                                    hide mcPic
                                    $ victim.say("Takže tvrdíš, že ho Lisbeth do dílny pustila jen proto, že slušně poprosil? Nebo že ten kašpar zvládne projít zamčenými dveřmi?", "angry")
                                "{i}(Neříct nic){/i}":
                                    hide mcPic
                            if "burned evidence seen" in victim.asked:
                                $ victim.say("A víš vůbec jistě, že moje střevíce nezničil on?", "angry")
                            else:
                                $ victim.say("A víš vůbec jistě, že moje střevíce nevzal on?", "angry")
                            show mcPic at menuImage
                            menu:
                                "Možné to samozřejmě je.":
                                    hide mcPic
                                    $ victim.say("Možné? Jestli mi ten slizký had leze do dílny, tak k tomu měl nejlepší příležitost! A moc dobře ví, že proti mně nemá ve volbě šanci.", "furious")
                                    $ mc.say("Na zatčení musím mít jasné důkazy, které obstojí před soudem.")
                                    $ victim.say("Tak s těmi důkazy pohni, ať ho co nejdřív vidím na pranýři, zmetka jednoho.", "angry")
                                "Toho by si vaše žena určitě všimla.":
                                    hide mcPic
                                    $ victim.say("No jen jestli. A jestli mi zase nelže.", "angry")
                                    $ victim.say("Asi si s nimi s oběma budu muset promluvit ještě jednou.", "angry")
                        else:
                            $ victim.say("Ten šašek, který mi chce konkurovat ve volbě cechmistra? Jak se ten dostal do mé dílny?", "surprised")
                            show mcPic at menuImage
                            menu:
                                "Bohužel opravdu nemůžu nic říct." if "part of investigation how" in victim.asked:
                                    hide mcPic
                                    $ victim.say("Tak to bych se asi měl zeptat tvých nadřízených. Nepředpokládám, že jestli mě někdo stejným způsobem vykrade, dokážeš mi to všechno zaplatit.", "angry")
                                "Pustila ho tam vaše manželka.":
                                    hide mcPic
                                    $ victim.say("Co to plácáš za nesmysly?", "angry")
                                    $ mc.say("Můžete se jí zeptat sám.")
                                    $ victim.say("To udělám. A jestli mi lžeš do očí, budu si na tebe stěžovat.", "angry")
                                    $ status.append("kaspar and lisbeth ratted out")
                                "Pustili ho tam vaši učedníci.":
                                    hide mcPic
                                    $ victim.trust -= 1
                                    "Kluci se po sobě zmateně podívají."
                                    $ son.say("Cože?", "surprised")
                                    $ yesman.say("Co?", "surprised")
                                    $ optimist.say("Nepustili!", "surprised")
                                    $ yesman.say("Nepustili!", "surprised")
                                    $ son.say("Proč bychom to prosím vás dělali?", "surprised")
                                    $ mc.say("Aspoň to mistr Kaspar říkal.")
                                    $ victim.say("Asi se budu muset Kaspara zeptat.", "angry")
                                "Vloupal se tam.":
                                    hide mcPic
                                    $ victim.trust -= 1
                                    $ victim.say("To je pitomost. Kdyby někdo vylomil zámek, přece bych si toho všiml.")
                                    if "doors" in workshop.checked:
                                        $ victim.say("A ty taky, viděl jsem, jak jsi dveře prohlížel[a].", "angry")
                                    $ mc.say("Je možné, že se dostal do dílny, protože bylo odemčeno.")
                                    $ victim.say("To se mi hodně nezdá.", "angry")
                                "To bohužel nevím." if "part of investigation how" not in victim.asked:
                                    hide mcPic
                                    $ victim.trust -= 2
                                    $ victim.say("To ses ho ani nezeptal[a]?", "angry")
                                    $ mc.say("No...")
                                    $ victim.say("Co je tohle za neschopnost?", "angry")
                                    $ victim.say("A jak si můžeš být jist[y], že moje střevíce nevzal on?", "angry")
                                    $ mc.say("Nebojte se, pracuji se všemi variantami.")
                                    $ victim.say("No jen jestli. Zatím jsi mě moc nepřesvědčil[a].")
                                "To je součást vyšetřování a nemůžu vám to nyní říct." if not any("part of investigation" in str for str in victim.asked):
                                    hide mcPic
                                    $ victim.asked.append("part of investigation how")
                                    $ victim.trust -= 1
                                    $ victim.say("To mám jen čekat, až se sem stejným způsobem dostane nějaký další špinavec?", "angry")
                                    jump workshopWitnessMenu2
                                "Tohle vám už opravdu říct nemůžu." if "part of investigation who" in victim.asked:
                                    hide mcPic
                                    $ victim.asked.append("part of investigation how")
                                    $ victim.trust -= 1
                                    $ victim.say("To mám jen čekat, až se sem stejným způsobem dostane nějaký další špinavec?", "angry")
                                    jump workshopWitnessMenu2
                    "To je součást vyšetřování a nemůžu vám to nyní říct.":
                        hide mcPic
                        $ victim.asked.append("part of investigation who")
                        $ victim.say("Vyšetřování zločinu v mé dílně. Pokud někdo má právo to vědět, tak já.", "angry")
                        show mcPic at menuImage
                        menu:
                            "Máte asi pravdu. Ten svědek je mistr Kaspar.":
                                hide mcPic
                                jump workshopWitnessMenu2
                            "I tak vám to říct nemůžu.":
                                hide mcPic
                                $ victim.trust -= 1
                                $ victim.say("Tak to bych se asi měl zeptat tvých nadřízených. Nepředpokládám, že jestli se ten stejný člověk vrátí a vykrade to tu, dokážeš mi to všechno zaplatit.", "angry")
            $ optimist.say("Ty střevíce tady určitě byly. Dost jsem je obdivoval, doufám, že jednou budu také takhle zručný.")
            if "no privacy" in status:
                $ victim.say("Tak o tom silně pochybuju.", "angry")
        "Viděli jste včera vystoupení té tanečnice s ohněm?" if "fireshow" in status and "fireshow" not in boysAsked:
            hide mcPic
            $ boysAsked.append("fireshow")
            call boysAboutFireshow
        "Mistře Heinrichu, můžete nás nechat o samotě?" if "no privacy" in status:
            hide mcPic
            if "Heinrich sent away" in boysAsked:
                $ victim.trust -= 1
                $ victim.say("To má být nějaký hloupý vtip? Nebudu tady pobíhat jako slepice jenom proto, že ty se neumíš rozhodnout. Stojím tady a ty koukej vyšetřovat, nebo vypadnout.", "angry")
            else:
                "Mistr se zamračí, ale pak beze slova odejde z dílny."
                $ boysAsked.append("Heinrich sent away")
                $ status.remove("no privacy")
        "Radši zavolám vašeho mistra." if currentLocation == "workshop" and "no privacy" not in status:
            hide mcPic
            $ status.append("no privacy")
            "Kluci se po sobě vyděšeně podívají, ale neodváží se odporovat."
            "Mistra Heinricha ani nemusíš hledat. Stojí téměř hned za dveřmi do dílny a připojí se k vám více než ochotně."
        "To je všechno, můžete zase jít.":
            hide mcPic
            if "Heinrich sent away" in boysAsked:
                $ boysAsked.remove("Heinrich sent away")
            call boysReleased
            return
    jump boysOptions

label heinrichLearnsAboutGerdInWorkshop:
    $ victim.say("Toho spratka si podám a jeho povedeného mistra také.", "angry")
    $ victim.say("Nebo k tomu máš ještě něco?", "angry")
    $ son.say("Kdy jste se to vlastně dozvěděl[a]?")
    show mcPic at menuImage
    menu:
        "Prý odnesl střih, podle kterého byly zhotovené ty ukradené boty.":
            hide mcPic
            $ victim.say("Aha.", "furious")
            $ victim.say("A přemýšlel[a] jsi nad tím, k čemu by to bylo?", "angry")
            $ victim.say("Střihy se nekradou, střihy nejsou žádná cennost. To každý ví.", "angry")
            $ victim.say("Zjisti si něco o ševcovině a nevěř každé pohádce, co ti někdo nakuká.", "angry")
            return
        "Zjistil[a] jsem to dnes." if gerdInWorkshopDiscovered.days == time.days:
            hide mcPic
            label gerdInWorkshopDiscoveredRecently:
            if gerdInWorkshopDiscovered.days > 1 and "Gerd in workshop - neighbour" in boysAsked:
                $ victim.trust -= 2
                $ rauvin.trust -= 1
                $ hayfa.trust -= 1
                $ son.say("Ale sousedů jste se přece musel[a] ptát hned na začátku, nebo ne? Kromě nás z domu měli největší naději, že si něčeho všimnou.", "surprised")
                $ victim.say("To je pravda! To jsi to pátrání hned od začátku tak flinkal[a], nebo mi teď lžeš?", "angry")
                $ mc.say("Nejdřív jsem musel[a]...")
                $ victim.say("Víš co? Mě to nezajímá. Očividně máš v pátrání co dohánět, tak to mazej dohnat a přestaň nás všechny zdržovat.")
            elif len(boysAsked) - len(origAsked) < 3 and len(heinrichHouseholdSpokenWith) == 1:
                $ victim.say("To je dobře, že s tím jdeš hned. Mně do dílny bez pozvání nikdo lézt nebude.", "angry")
                $ son.say("Ale jak potom... ne, počkat...", "surprised")
                $ victim.say("Co?", "angry")
                $ son.say("Nic, myslel jsem, že mě něco napadlo, ale byla to hloupost.")
                $ victim.say("Kdybys radši přemýšlel u šití.", "angry")
                $ victim.say("[callingMc].capitalize(), máš ještě nějaké otázky, nebo můžeme jít zase pracovat?")
            else:
                $ victim.trust -= 1
                $ son.say("Ale tady v domě jste už pěknou dobu a takhle důležitou věci si schováváte? Vždyť se tátovi mohla objevit nějaká neodkladná záležitost, kdy by se to potom dozvěděl?", "surprised")
                $ victim.say("Přesně! Řešíš tady kdovíco a na takhle důležitou novinu málem vůbec nedošlo. Tak si představuješ dobrou práci?", "angry")
                $ victim.say("Očekávám, že když se hrabeš ve věcech mojí rodiny a mého domu, tak mi aspoň okamžitě řekneš, kdykoli se dozvíš něco důležitého.", "angry")
                $ victim.say("Tak co, máš ještě něco podstatného, nebo se můžeme konečně všichni vrátit ke svojí práci?", "angry")
        "Zjistil[a] jsem to zrovna včera večer." if gerdInWorkshopDiscovered.days == time.days - 1 and time.hours < 13:
            hide mcPic
            jump gerdInWorkshopDiscoveredRecently
        "Zjistil[a] jsem to na začátku vyšetřování, když jsem obe[sel] sousedy." if time.days > 1:
            hide mcPic
            $ son.say("A proč jste to neřekl hned? Jak si to s ním potom můžu vyřídit?", "angry")
            $ son.say("A to to ještě ani není moje dílna. Jak se musí cítit táta, nevědět, co se děje pod jeho střechou?", "angry")
            $ victim.say("Přesně! Pobíháš po městě, řešíš kdovíco a s takhle důležitou novinou si dáš na čas. Tak si představuješ dobrou práci?", "angry")
            $ victim.say("Očekávám, že když se hrabeš ve věcech mojí rodiny a mého domu, tak mi aspoň okamžitě řekneš, kdykoli se dozvíš něco důležitého.", "angry")
            $ victim.say("Tak co, máš ještě něco podstatného, nebo se můžeme konečně všichni vrátit ke svojí práci?")
    return

label burnedEvidenceSeenBoys:
    "Kluci si ohořelý útržek prohlédnou."
    $ optimist.say("To vypadá...", "surprised")
    $ yesman.say("...to fakt vypadá jako kus těch bot...", "surprised")
    $ optimist.say("...ale jak? To přece nedává smysl...", "surprised")
    $ son.say("Kde jste to na[sel]?", "surprised")
    $ optimist.say("Vždyť ty boty byly tady na stole, úplně v pořádku.", "surprised")
    if currentLocation == "workshop":
        $ mc.say("Na[sel] jsem to v krbu tady v dílně. A doufal[a] jsem, že co se tomu stalo, mi řeknete vy.")
    else:
        $ mc.say("Na[sel] jsem to v krbu v mistrově dílně. A doufal[a] jsem, že co se tomu stalo, mi řeknete vy.")
    $ optimist.say("Asi to bude nějaký odstřižek nebo zbytek z výroby, ale jak se dostal do krbu?", "surprised")
    $ son.say("Viděl to táta?", "surprised")
    if "burned evidence seen" in victim.asked:
        $ son.trust -= 2
        $ son.pressure +=1
        $ optimist.pressure += 1
        $ yesman.pressure += 1
        $ mc.say("Viděl a vůbec z toho nebyl nadšený.")
        $ yesman.say("Jestli se těm botám fakt něco stalo, tak nás mistr zabije!", "surprised")
        $ son.say("To je konec!", "surprised")
        $ optimist.say("Co říkal?")
        $ son.say("Nemůžete mu říct, že to byl omyl?", "sad")
        $ optimist.say("Nebo že to vůbec nesouvisí s jeho botami? Vážně to bude jenom nějaký odstřižek.")
    else:
        $ mc.say("Zatím ne, ale asi bych měl[a].")
        $ son.say("Nemohl[a] byste s tím počkat? Aspoň než zjistíte, co přesně se stalo?")
        $ yesman.say("Jestli se těm botám fakt něco stalo, tak nás mistr zabije!", "surprised")
        $ optimist.say("To přece s tou krádeží nemůže nijak souviset. Vážně to bude jenom nějaký odstřižek.")
    $ yesman.say("Takových je tady vždycky spousta a vyklízíme je odevšad.")
    show mcPic at menuImage
    menu:
        "Pokusím se ho uklidnit." if "burned evidence seen" in victim.asked:
            call boysPromisedSecrecy
            $ status.append("calm Heinrich")
        "Nechám si to zatím pro sebe." if "burned evidence seen" not in victim.asked:
            call boysPromisedSecrecy
            $ status.append("boys promised secrecy")
        "To bohužel nemůžu.":
            hide mcPic
            $ son.say("Táta nás zabije!", "surprised")
            $ optimist.say("Snad ne, ono to vážně nemusí nic znamenat...")
            $ son.say("surprised")
        "Víte něco o tom odstřižku něco?":
            hide mcPic
            "Všichni tři kluci zavrtí hlavou."
            $ son.say("Ne, ale tátu znám až moc dobře.", "angry")
            $ yesman.say("Nic o tom nevíme.")
    return

label boysPromisedSecrecy:
    hide mcPic
    $ son.trust += 1
    $ optimist.trust += 1
    $ yesman.trust += 1
    $ son.say("Nebudete toho litovat. Ono se vám bude i líp vyšetřovat, když nebude táta běsnit a házet věcmi.", "happy")
    $ optimist.say("Tak strašné by to snad...")
    $ son.say("Máte to u nás!")
    $ yesman.say("Rozhodně!")
    return

label boysTired:
    hide mcPic
    $ boysAsked.append("lost bottles 3")
    $ son.say("Dlouho jsme pracovali.")
    $ yesman.say("A uklízeli.")
    $ mc.say("To vypadáte každé ráno takhle?")
    $ yesman.say("No to ne...")
    $ optimist.say("Asi jsme včera pracovali obzvlášť příkladně.")
    $ mc.say("A nepili jste náhodou? Už jsem viděl[a] dost lidí s kocovinou, abych poznal[a], jak to vypadá.")
    $ yesman.say("No, trochu.")
    $ optimist.say("Ale až potom, co jsme uklidili.")
    $ son.say("No, možná jsme něco málo přehlédli.")
    $ optimist.say("Pili jsme angreštovou pálenku. Je to nový recept, tak jsem ji dostal se slevou.")
    $ son.say("Je to hodně silná pálenka. Asi jsme jí trochu přebrali.")
    $ yesman.say("Rozhodně!")
    $ optimist.say("Ale nic jiného jsme nepili!")
    return

label boysReleased:
    if "no privacy" in status:
        "Učedníci se tázavě podívají na svého mistra a ten je pohybem ruky vyžene."
        $ victim.say("Potřebujete tady ještě něco?")
    else:
        $ son.say("Máme ještě práci.")
        $ yesman.say("Snad jsme pomohli.")
        $ optimist.say("Kdybyste potřeboval[a] ještě něco...")
        $ son.say("Snad nebudete...")
        "Kluci zmizí mírně nejistě, ale o to rychleji."
        if currentLocation == "workshop":
            "V dílně je okamžitě nahradí mistr Heinrich, který tě očividně nechce nechat ve své dílně ani chvilku bez dozoru."
            $ victim.say("Potřebujete tady ještě něco?")
    return

label boysAboutFireshow:
    $ yesman.say("Té hezké hnědovlasé?", "blushing")
    $ optimist.say("Tobě se líbila?", "happy")
    if "no privacy" in status:
        "Mistr Heinrich se na kluky zamračí a s přísným pohledem čeká na odpověď."
    $ son.say("Neviděli.")
    $ yesman.say("...", "blushing")
    $ son.say("No dobře, viděli.")
    $ optimist.say("Kousek. Náhodou jsme šli kolem.")
    $ son.say("Opravdu bude souzená za žhářství?", "surprised")
    $ yesman.say("Ale dostane se z toho, že ano?", "surprised")
    label fireshowBoys1:
    show mcPic at menuImage
    menu:
        "To záleží na tom, jestli bude někdo svědčit v její prospěch.":
            hide mcPic
            $ yesman.say("... a bude?", "surprised")
            $ mc.say("Snažím se sehnat pár lidí. Chcete se přidat?")
            $ son.say("K tomu svědčení?", "surprised")
            $ optimist.say("To by bylo něco!", "susprised")
        "To záleží na tom, jestli to udělala." if "katrin guilty" not in boysAsked:
            hide mcPic
            $ boysAsked.append("katrin guilty")
            $ yesman.say("Samozřejmě, že neudělala.", "angry")
            $ optimist.say("No, ten vůz zapálila ona...")
            $ son.say("Jen protože se na ni vrhli.")
            $ yesman.say("Přesně. Jinak by dál tančila, my bychom ji tleskali, pak by šla domů a všechno by bylo v pořádku.")
            $ optimist.say("Takže ji soud propustí?")
            jump fireshowBoys1
        "To záleží na vás.":
            hide mcPic
            $ yesman.say("Jak? Máme ji vysvobodit z vězení?", "surprised")
            $ son.say("[mcName] je z hlídky, vážně myslíš, že navrhuje zrovna tohle?")
            $ optimist.say("Rozhodně by to nikdo nečekal!", "happy")
            $ yesman.say("... v tom případě nevím, co můžeme udělat.", "sad")
            $ mc.say("Můžete svědčit v její prospěch.")
        "Asi ne.":
            hide mcPic
            $ yesman.say("To přece… musí být něco, co se dá udělat!", "angry")
            show mcPic at menuImage
            menu:
                "Můžete svědčit v její prospěch.":
                    hide mcPic
                "Myslím, že se nic dělat nedá.":
                    hide mcPic
                    $ yesman.say("...", "sad")
                    $ optimist.say("Zapomeň na ni, na slavnostech bude spousta jiných kejklířek.")
                    $ yesman.say("Takže je v pořádku, když tuhle zabijou?", "angry")
                    $ optimist.say("Tak jsem to… promiň?", "surprised")
                    $ son.say("Asi bychom měli změnit téma. Potřebujete od nás ještě něco, nebo můžeme jít pracovat?")
                    return            
    $ son.say("Poslouchal by nás tam vůbec někdo?", "surprised")
    if "Heinrich supports boys' testimony" in status:
        $ mc.say("Už jsem mluvil[a] s mistrem Heinrichem, prý jestli budete mít, co říct, tak vám pozornost zajistí.")
    else:
        $ mc.say("To zařídím.")
    $ son.say("...", "surprised")
    $ optimist.say("...", "surprised")
    $ yesman.say("... vážně máme mluvit před celým soudem?", "surprised")
    $ son.say("To zní trochu děsivě.", "surprised")
    $ convincingWitness = 0
    show mcPic at menuImage
    menu:
        "To není nic hrozného. Jsou to jenom lidi z města, které znáte.":
            hide mcPic
            $ convincingWitness -= 1
            $ son.say("No já nevím, tím to je možná ještě horší. Jestli si udělám ostudu, budu je pak každý den potkávat.", "sad")
            $ optimist.say("Ale každý den je budeš potkávat, i jestli je uchvátíš.", "happy")
            $ mc.say("Důležité je, že víte, že to jsou lidé jako vy a nemusíte z nich mít strach.")
            $ yesman.say("Já třeba z pana Oswalda trochu strach mám. Vždyť vedl dvě povstání.", "surprised")
        "Soustřeďte se na to, že to je pro dobrou věc, a půjde to snadno.":
            hide mcPic
            $ convincingWitness -= 1
            $ yesman.say("To je pravda! Ona žádný zločin nespáchala.", "happy")
            $ optimist.say("No, městské zákony jsou v tomhle...")
            $ yesman.say("A jestli někdo bude tvrdit opak, tak mu to pořádně vysvětlím!", "angry")
            $ optimist.say("... chci říct, jistě že nespáchala. Zákony proti tanci určitě nejsou.", "surprised")
            $ mc.say("Jen se nenechte unést.")
            $ son.say("Možná by nebylo chytré se tam se všemi pohádat.")
            $ yesman.say("Když oni ji budou chtít odsoudit a my nechceme, aby ji odsoudili?", "surprised")
            $ mc.say("Soudci se právě teprve během soudu budou rozhodovat.")
            $ yesman.say("Ti možná, ale ta sektářka z hlídky v tom má asi hodně jasno.", "angry")
            $ yesman.say("Jak ji tam vlekla... to jí nedaruju.", "angry")
        "Dobře si to nacvičte.":
            hide mcPic
            $ convincingWitness += 1
            $ mc.say("Nejdřív to všechno řekněte sobě navzájem, potom třeba mně nebo Adě a nakonec mistru Heinrichovi.")
            $ mc.say("Tím si na to zvyknete a potom už budete vypovídat klidně i před vévodou.")
            $ son.say("A co když po pár větách přijde nějaká otázka, která mě vyvede z míry?", "surprised")
            $ yesman.say("Přesně. Mě vyvede z míry už jenom to, když se mě mistr při práci zeptá, co to zase dělám.", "sad")
            $ son.say("Tak hrozný ten soud snad nebude...")
            $ mc.say("Na otázky se můžete připravit úplně stejně. Prostě si představte, že jste nějaký šťoural, ptejte se sebe navzájem a pak společně vymyslete dobrou odpověď.")
            $ optimist.say("Šťourání tady Aachimovi jde.", "happy")
            $ son.say("Já ti nevím. To šlo hlavně Gerdovi.")
            $ optimist.say("Tak zajdeme za Gerdem. Ať nepřijde o všechnu zábavu jen proto, že se nechal vyhodit.", "happy")
            if "pastTrialsIntro" in pastTrialsTopics:
                $ mc.say("To udělejte. A nejsou v knihovně nebo na radnici záznamy z minulých soudů? To vám pomůže si představit, jak to celé může probíhat.")
                $ yesman.say("Myslím, že jsou. Celé stohy.")
            else:
                $ mc.say("To udělejte. A v knihovně si můžete najít záznamy z minulých soudů. To vám pomůže si představit, jak to celé může probíhat.")
            $ son.say("A pustí nás táta, abychom si četli v knihovně?", "surprised")
            $ mc.say("Nepotřebujete toho přečíst moc, stačí několik případů pro představu.")
            $ optimist.say("To bude hned.")
    $ son.say("Co tam ale vůbec máme říkat?")
    $ optimist.say("Já myslím, že tam se vždycky někdo ze soudců vyptává a ty jen odpovídáš?")
    show mcPic at menuImage
    menu:
        "Je to tak. Stačí počkat na otázky.":
            hide mcPic
            $ mc.say("Oni si sami řeknou, co je zrovna zajímá.")
        "Lepší je, když je k ptaní vůbec nepustíte.":
            hide mcPic
            $ convincingWitness -= 1
            $ mc.say("Prostě začněte vyprávět od začátku do konce.")
            $ son.say("A nebudou se chtít někdy doptat na podrobnosti?", "surprised")
            $ mc.say("Tak řekněte, že k tomu se dostanete, a pak se vraťte, kde jste byli.")
            $ mc.say("To je nejlepší způsob, jak se v tom neztratit.")
            $ son.say("A co když se zeptají na něco, na co už došlo, nebo něco napoprvé nepochopí a budou si to potřebovat ujasnit?", "surprised")
            $ mc.say("Úplně ze všech otázek se samozřejmě nevyvlečete a některé určitě přijdou i na konci, ale aspoň jich takhle nebude tolik.")
        "Myslím, že budete moct začít sami a oni se potom doptají.":
            hide mcPic
            $ convincingWitness += 1
            $ mc.say("Asi vás nenechají mluvit nepřerušeně. Určitě je bude zajímat nějaká podrobnost, kterou na první vyprávění vynecháte.")
            $ mc.say("Ale zároveň by nebyli rádi, kdyby z vás museli úplně všechno tahat.")
            $ yesman.say("To musím něco nejdřív sám vyprávět a potom se ještě budou ptát a hledat v tom mezery? To zní strašně.", "surprised")
            $ mc.say("Ber to tak, že si o tom prostě popovídáte. Jako kdybys to vyprávěl Gerdovi.")
            $ optimist.say("Tomu by asi vyprávěl hlavně jiné věci...", "happy")
            $ yesman.say("Nech toho!", "surprised")
            $ mc.say("A hlavně se nebojte dodat něco, na co se třeba nezeptají, když to bude důležité.")
    $ yesman.say("A jak poznáme, co soudce zajímá?")
    show mcPic at menuImage
    menu:
        "Hlavně nich nevynechte.":
            hide mcPic
            $ mc.say("Ta dívka nic nespáchala, a jestli soudci uslyší celou pravdu, musí to poznat.")
            $ yesman.say("... jste si jist[y]?", "surprised")
            $ optimist.say("V radě máme docela slušné lidi, na ty se dá spolehnout.")
            $ yesman.say("V tom případě jim musíme podrobně vylíčit i to, jak ji Hayfa zatýkala. Ať všichni poznají, co je zač.", "angry")
            show mcPic at menuImage
            menu:
                "To je dobrý nápad. Soud uvidí, že žaloba je zaujatá.":
                    hide mcPic
                    $ convincingWitness -= 1
                    $ son.say("A nebudeme potom vypadat zaujatě my?", "surprised")
                    $ yesman.say("Ale my máme pravdu!", "angry")
                "Raději ne. Toho se soud netýká a působilo by to jako zbytečné pomlouvání.":
                    hide mcPic
                    $ yesman.say("Zbytečné? Takhle bych nezatýkal ani hrdlořeza!", "angry")
                    $ mc.say("Tak potom po soudu zkusíme dát stížnost k veliteli.")
                    $ yesman.say("... no dobře, zkusím se držet.", "sad")
                    $ son.say("Nech tuhle část na nás.")
        "Říkejte jen to nejdůležitější, abyste se neztratili v podrobnostech.":
            hide mcPic
            $ optimist.say("... a to je co? Tančila, potom vytáhla oheň, strhla se mela a začal hořet vůz?")
            $ yesman.say("A je nevinná!", "angry")
            $ son.say("... to nezní příliš přesvědčivě.", "sad")
            $ optimist.say("A co je tedy to nejdůležitější?")
            show mcPic at menuImage
            menu:
                "Že na ni lidé zaútočili a hořet začalo jen kvůli tomu.":
                    hide mcPic
                    $ convincingWitness += 1
                    $ optimist.say("To bylo hodně děsivé, to by utekl každý.")
                    $ yesman.say("A ten hrubián na ni sahal a kdo ví, co jí chtěl udělat!", "angry")
                    $ son.say("Kdyby ji nechali utéct, nic by se nestalo, ale někdo jí zkusil nadběhnout.")
                    $ yesman.say("Určitě nějaký další hrubián.", "angry")
                    $ son.say("A hlavně ten první jí pořád byl v patách. Musela utíkat rychle.")
                    $ optimist.say("A nemohla ty vějíře radši zahodit?")
                    $ son.say("Mohla a běželo by se jí pak snáz. Ale to by nemohla dát pozor, že tím něco nezapálí! I při útěku dobře věděla, co dělá!")
                "Že tančit opravdu umí, a nic tedy nehrozilo.":
                    hide mcPic
                    $ yesman.say("No to ona umí", "blushing")
                    $ mc.say("A umíte k tomu dát příklad, aby si to soudci dokázali představit?")
                    $ optimist.say("Třeba jak hýbala každou rukou jinak a ještě se u toho všelijak vlnila.")
                    $ yesman.say("A mrkala na publikum. Jednou i na mě!", "blushing")
                    $ son.say("Nebo jak se vždycky rychle otočila, ale stejně skončila přesně na stejném místě.")
                    $ yesman.say("A vždycky se jí u toho rozevlály vlasy.", "blushing")
                    $ son.say("Tyhle dodatky možná radši soudu neříkej. Chceme působit vážně a nezaujatě.")
                    $ yesman.say("Ale vypadat takhle dobře, to musí dát hroznou práci!", "surprised")
                    $ yesman.say("To není, jako když ty ses sice naučil tu Zairisovu novou figuru, ale vypadal jsi u toho, že si zlomíš obě nohy.")
                    $ son.say("No dovol...", "angry")
                    $ optimist.say("Na to, že se musel při cvičení schovávat, aby ho neviděla Ada a nesmála se mu, to ještě dopadlo docela dobře.")
                    $ son.say("... myslel jsem, že tady řešíme důležité věci.")
                    $ yesman.say("To je pravda! Co dál?")
                "Že ten oheň vytáhla na bezpečném místě.":
                    hide mcPic
                    $ convincingWitness += 1
                    $ optimist.say("... uprostřed města!", "surprised")
                    $ son.say("Ne. Ve čtvrti, kde jsou zděné stěny.")
                    $ mc.say("A daleko od všeho hořlavého, jestli se nepletu?")
                    $ yesman.say("Ten vůz byl rozhodně pěkných pár kroků.")
                    $ son.say("Některé části domů jsou dřevěné, ale ty byly daleko a tak snadno to dřevo také nechytne.")
                    $ optimist.say("Doškové střechy už ve městě nikdo nemá. Některé požár nezasáhl, ale všichni se jich co nejrychleji zbavili.")
                    $ yesman.say("Takže jediné ohrožení způsobil ten hrubián, co ji vyhnal na vůz.", "angry")
                "Že ji do té doby všichni obdivovali a povzbuzovali.":
                    hide mcPic
                    $ convincingWitness -= 1
                    $ son.say("Aby ne, tančila dobře, ale jak to souvisí s ohněm?")
                    $ optimist.say("Tak, že pořád chtěli další a další čísla.")
                    $ yesman.say("Ještě zajímavější a neobvyklejší.")
                    $ mc.say("A zároveň vypadali, že jí důvěřují a chtějí od ní vidět všechno, co umí.")
                    $ optimist.say("Přesně! Přesvědčili ji, že může, že to je v pořádku.", "happy")
                    $ yesman.say("Také bylo. Já bych její vystoupení s ohněm velmi rád viděl. Všiml sis, jak se jí odrážel ve vlasech? A to ani ještě nestihla tančit!", "blushing")
                    $ son.say("Já bych to možná radši viděl někde mimo město...", "sad")
                    $ optimist.say("Ale tam bychom ji nenašli a zbytek obecenstva také ne, tak musela ve městě!")
                "Že tam měla hudebníka, který ji k tomu určitě navedl.":
                    hide mcPic
                    $ convincingWitness -= 1
                    $ yesman.say("To je pravda! Co ten je vůbec zač?", "angry")
                    $ optimist.say("Nějaký jiný komediant? Upřímně, na něj jsem se moc nedíval.")
                    $ mc.say("Když k tomu hraje, nejspíš vybírá skladbu.")
                    $ yesman.say("A tím i druh tance. Takže ten oheň vůbec nebyl její nápad!")
                    $ son.say("No že teď přijde něco nového, to vyhlásila ona...")
                    $ yesman.say("Ale určitě na znamení od něj!", "angry")
        "Hlavně zdůrazněte to, co té dívce pomůže.":
            hide mcPic
            $ yesman.say("Takže neříkej nic o zákonech, Ferdi!", "angry")
            $ optimist.say("... není nějaký zákon o tom, že se nemá na ulici útočit na jiné lidi?")
            $ yesman.say("No vidíš! Ten tam vytáhni!", "happy")
            $ son.say("Já bych to nedělal, stihl do ní jen strčit a to většinou nikdo neřeší.")
            $ optimist.say("A to, že potom začal hořet ten vůz, taky radši nemám říkat?", "surprised")
            show mcPic at menuImage
            menu:
                "Radši ne, on to zmíní někdo jiný.":
                    hide mcPic
                    $ convincingWitness -= 1
                    $ son.say("A nebudeme potom vypadat nedůvěryhodně?", "surprised")
                    $ yesman.say("Máme té tanečnici pomoct, ne? Jak bychom jí pomohli, kdybychom schválně vytahovali věci proti ní?", "angry")
                    $ optimist.say("To dává smysl. Mistrovi taky nebudu říkat, když se nám něco nepovede.")
                    $ son.say("Ale stejně to většinou pozná.", "sad")
                    $ optimist.say("Oni ale neuvidí naši botu... co když se na to zeptají?")
                    $ mc.say("Lhát nemůžete, ale zkuste to zamluvit nebo aspoň odvést pozornost někam jinam.")
                "To říct musíte, když se to stalo. Jenom na to nepřitahujte tolik pozornosti.":
                    hide mcPic
                    $ convincingWitness += 1
                    $ mc.say("Kdybyste to zkusili zamlčet úplně, nebyli byste důvěryhodní.")
                    $ mc.say("Naopak dobře popište, co k tomu vedlo. Co ti lidé vypadali, že by jí mohli chtít udělat.")
                    $ optimist.say("To si snad nechci představovat.", "sad")
                    $ yesman.say("Jeden ji chytil tak hrubě, že se málem nedokázala vykroutit.", "angry")
                    $ son.say("ěch lidí, co po ní vyběhlo, rozhodně nebylo málo.")
                    $ optimist.say("Vypadalo to, že ji budou chtít přímo na místě zlynčovat a ani nepočkají na někoho z hlídky.", "angry")
                    $ son.say("A to je teprve něco, co by se tu nemělo dít. Ještě, že utekla.", "angry")
    $ yesman.say("Ještě něco, co by pomohlo?")
    $ son.say("Ať už té tanečnici, nebo nám v přesvědčování soudu?")
    $ mc.say("Možná ještě jedna rada na závěr.")
    show mcPic at menuImage
    menu:
        "Snažte se působit co nejvíc sebejistě.":
            hide mcPic
            $ mc.say("Mluvte co nejvíc nahlas a celou dobu se dívejte soudcům do očí.")
        "Jestli budete nervózní, dejte si před soudem loka kořalky. To pomáhá.":
            hide mcPic
            $ convincingWitness -= 1
            $ mc.say("Uvolní vás to a budete si víc věřit a díky tomu budete mnohem přesvědčivější.")
        "Dejte si pozor, abyste nemluvili přes sebe a neskákali si do řeči.":
            hide mcPic
            $ convincingWitness += 1
            $ mc.say("Doplňovat se můžete, ale nejdřív vždy v klidu počkejte, než ten před vámi domluví.")
    $ optimist.say("Tak jo, to zvládneme!", "happy")
    $ yesman.say("Děkujeme za pomoc. To se budou u soudu divit.", "happy")
    $ son.say("Můžeme nějak pomoct my vám?")
    if "Heinrich supports boys' testimony" in status and convincingWitness > 0:
        $ katrin.cluesAgainst += 1
    return

###

label boysOptionsRemainingCheck:
    $ boysOptionsRemaining = 0
    if "workshop empty" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "evening activities" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "enemies" in rumelin.asked and "fired apprentices" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "fired apprentices" in boysAsked and "fired apprentices" not in clues:
        $ boysOptionsRemaining += 1
    if "fired apprentices" in clues and "fired apprentices contacts" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "burned evidence" in clues and "burned evidence seen" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "anything suspicious" in lisbeth.asked and "lost bottles 1" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "lost bottles 1" in boysAsked and "lost bottles 2" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "lost bottles 1" in boysAsked and "lost bottles 3" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "lost bottles 2" in boysAsked and "lost bottles 3" in boysAsked and "confession" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "confession" in kaspar.asked and "shoes in workshop" not in boysAsked:
        $ boysOptionsRemaining += 1
    if "fireshow" in status and "fireshow" not in boysAsked:
        $ boysOptionsRemaining += 1
    return
