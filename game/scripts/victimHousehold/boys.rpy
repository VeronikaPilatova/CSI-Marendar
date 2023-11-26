label boysMain:
    $ sonNote.isActive = True
    $ apprentice1Note.isActive = True
    $ apprentice2Note.isActive = True
    $ lastSpokenWith = "boys"

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
            $ optimist.say("Asi před týdnem jsem ale viděl Gerda. Šel jsem pro nějaké věci k panu Rovinovi a potkal jsem ho tam. Vypadal spokojeně.")
            if "no privacy" not in status:
                $ son.say("Aby ne.", "angry")
            $ optimist.say("Prý ho mistr Njal dokonce poslouchá, když má nějaký nápad. A když to je hloupost, tak mu to vysvětlí.")
            $ yesman.say("Mistr Heinrich říkal, že se tam Gerd naučí jen ztrácet čas.")
            if "no privacy" in status:
                "Aachim obrátí oči v sloup, ale nic neřekne."
            else:
                $ son.say("On říká spoustu věcí.", "angry")
            $ yesman.say("Také říkal, že to vlastně Gerd už teď umí až moc dobře, takže se tam nenaučí vůbec nic.")
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
                        $ victim.say("Ten šašek, který mi chce konkurovat ve volbě cechmistra? Jak se ten dostal do mé dílny?", "surprised")
                        label workshopWitnessMenu2:
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
                                $ victim.say("Ten šašek, který mi chce konkurovat ve volbě cechmistra? Jak se ten dostal do mé dílny?", "surprised")
                                jump workshopWitnessMenu2
                            "I tak vám to říct nemůžu.":
                                hide mcPic
                                $ victim.trust -= 1
                                $ victim.say("Tak to bych se asi měl zeptat tvých nadřízených. Nepředpokládám, že jestli se ten stejný člověk vrátí a vykrade to tu, dokážeš mi to všechno zaplatit.", "angry")
            $ optimist.say("Ty střevíce tady určitě byly. Dost jsem je obdivoval, doufám, že jednou budu také takhle zručný.")
            if "no privacy" in status:
                $ victim.say("Tak o tom silně pochybuju.", "angry")
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
            call boysReleased
            return
    jump boysOptions

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
    return
