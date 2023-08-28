label fireshow:
    scene bg street05 night
    "Cestou k domu, kde prozatím přespáváš, zaslechneš rytmickou píseň hranou na nějaký strunný nástroj. Není to velká zacházka a hudebník zřejmě není daleko od domu mistra Heinricha. Vydáš se tím směrem s myšlenkou, že se tak třeba dozvíš víc o některém z ševců."
    "Tóny loutny či snad lyry vystřídá potlesk a poté mladý ženský hlas."
    "Teď ale přichází čas na číslo, které vám skutečně rozproudí krev v žilách. Je to umění z dalekého jihu, tanec ladný i živý, trochu svůdný a trochu nebezpečný. Odhoďte zábrany, zapomeňte na obavy a nechte se pohltit."
    "Hudba se znovu rozezní, tentokrát je mnohem pomalejší a tesknější. Potom konečně zahneš za roh. Ulice je temná a zprvu rozeznáš jen siluety asi desítky diváků a osamocené tanečnice."
    scene bg fireshow
    "Vzápětí scénu prosvětlí několik malých loučí v dívčiných rukou, spojených do podoby dvou vějířů. Mihotavé světlo dopadne na její vlasy, na kluka s lyrou pár kroků od ní, na čepici ležící na zemi a několik mincí v ní."
    "A na obličeje diváků, v nichž se úsměvy rychle mění v překvapení a poté v hněv."
    scene bg after fireshow
    $ anon1.say("Co to má znamenat?")
    $ anon3.say("Okamžitě to zhasni!")
    $ anon2.say("Chceš to tu snad podpálit?")
    $ kilian.say("To je jen...")
    $ anon1.say("Žádné výmluvy!")
    "Jeden z mužů k dívce vykročí a hrubě ji chytí za paži."
    $ anon1.say("Dej to sem!")
    $ katrin.say("Nechte mě!", "surprised")
    "Tanečnice se pokusí muže odstrčit druhou rukou. Jeden z vějířů se tak dostane k jeho obličeji. Muž vykřikne a pustí ji. Ona se rozběhne pryč."
    $ anon2.say("Za ní!")
    $ anon3.say("Chyťte žhářku!")
    scene bg cart
    menu:
        "{i}(Pronásledovat dívku spolu s měšťany){/i}":
            "Rozběhneš se za prchající tanečnicí. Několik dalších pronásledovatelů je před tebou a není jisté, zda je předstihneš. Snad alespoň nedoběhneš příliš pozdě."
        "{i}(Pokusit se měšťany uklidnit){/i}":
            "Vykřikneš několik slov, žádný z měšťanů ti ale nevěnuje pozornost. Skoro se zdá, jako by pro ně mihotání ohně ve dvou vějířích zastínilo všechno ostatní. "
        "{i}(Zůstat na místě){/i}":
            pass
    "Z jednoho z domů kdosi vyběhne a zastoupí dívce cestu. Ona v poslední chvíli vyskočí na blízký vůz a přeběhne přes něj. Během skoku upustí oba vějíře, jeden na dlažbu ulice, druhý na korbu vozu."
    scene bg burning cart
    "Až teď se ukáže, že vůz je plný slámy. Vyšlehne vysoký plamen."
    "Na ulici se vyrojí další lidé, kteří okamžitě začnou hasit a dávat pozor, aby se oheň nerozšířil."
    "Proti dívce se rozběhne další postava. Tentokrát tanečnice neunikne. Útočník ji několikrát bolestivě udeří a strhne ji k zemi."
    $ hayfa.say("Šíření ohně se tady neodpuští, {i}žhářko{/i}. Poslala tě Luisa, nebo tě to prostě těší?", "angry")
    "Hayfa dívce zkroutí ruce za zády a rychle je spoutá. Na místo začnou dobíhat další pronásledovatelé."
    $ anon1.say("Pusťte mě na ni!")
    $ anon2.say("Z toho nevyvázne!")
    $ hayfa.say("Ta špína patří hlídce. Ale nevyvázne.", "angry")
    "Hayfa se postaví a trhne dívčinými pouty vzhůru. Tanečnice vykřikne bolestí a rychle se také zvedne na nohy."
    $ hayfa.say("Postavíme ji před soud a pak ji potrestáme všem na očích.", "angry")
    $ hayfa.say("Já se o ni postarám. Vy jděte hasit.")
    "Měšťané si vymění krátké pohledy a pak se skutečně obrátí a přidají se k lidem, kteří nosí vodu, polévají vůz i okolní domy a zadupávají odletující jiskry."
    "Hayfa i se zajatkyní rázně zamíří směrem na strážnici."
    menu:
        "{i}(Doběhnout Hayfu){/i}":
            scene bg after fireshow
            "Hayfa jde velmi rychle a tanečnici s sebou málem vleče a lidé spěchající hasit jí uhýbají s cesty, zatímco ty se mezi nimi musíš proplétat. Přesto ji za krátkou chvíli dostihneš. Hlídkařka se na tebe krátce podívá, ale jinak si tě nevšímá ani nezpomalí."
            $ origAsked = hayfa.asked.copy()

            call hayfaFireshowOptionsRemainingCheck
            if optionsRemaining == 0:
                "Krátce se rozloučíš a necháš hlídkařku projít kolem sebe."
                return

            label hayfaFireshowOptions:
            show mcPic at menuImage
            menu:
                "To bylo chytré, takhle ji zachránit před lynčem! Máš v úmyslu ji teď pustit?" if "fireshow clever" not in hayfa.asked and "fireshow needs punishment" not in hayfa.asked:
                    hide mcPic
                    $ hayfa.asked.append("fireshow clever")
                    if len(hayfa.asked) - len(origAsked) > 2:
                        $ hayfa.trust -= 1
                    "Hayfa se zarazí a upřeně se na tebe zahledí. Tanečnice se nezastaví včas, Hayfa jí trhne zpět k sobě a dívka sykne bolestí."
                    $ hayfa.say("Ty bys ji pustil?", "angry")
                    show mcPic at menuImage
                    menu:
                        "Samozřejmě, že ano!":
                            hide mcPic
                            $ hayfa.trust -= 3
                            $ mc.say("Vždyť bylo vidět, že těmi mávátky nic zapálit nemůže. Není důvod ji trestat.")
                            if gender == "M":
                                $ hayfa.say("Tys nezažil požár Marendaru. Já ano.", "angry")
                            else:
                                $ hayfa.say("Tys nezažila požár Marendaru. Já ano.", "angry")
                            $ hayfa.say("Oheň na ulici je zakázaný z dobrého důvodu.", "angry")
                            "Hayfa smýkne dívkou a opět vyrazí na cestu."
                        "Samozřejmě, že ne!":
                            hide mcPic
                            $ mc.say("Jen mě těší, že ji neubili na ulici, ale rozhodne o ní spravedlivý soud.")
                            "Hayfa tě ještě okamžik sleduje a potom bez dalšího slova smýkne dívkou a opět vyrazí na cestu."
                "Vážně jí hrozí nějaký trest?" if "fireshow needs punishment" not in hayfa.asked:
                    hide mcPic
                    $ hayfa.asked.append("fireshow needs punishment")
                    if len(hayfa.asked) - len(origAsked) > 2:
                        $ hayfa.trust -= 1
                    $ hayfa.say("Samozřejmě. Jako všem žhářům.", "angry")
                    show mcPic at menuImage
                    menu:
                        "Ale ona nic zapálit nechtěla!":
                            hide mcPic
                            $ hayfa.trust -= 2
                            $ hayfa.say("To ať vysvětlí těm lidem, co teď hasí.", "angry")
                            $ mc.say("Neměli by co hasit, kdyby ji nedonutili utíkat.")
                            $ hayfa.say("Možná. Oheň na ulici přinesla ona.", "angry")
                            $ katrin.say("Okolo nebylo nic hořlavého!", "surprised")
                            $ hayfa.say("To si schovej k soudu.", "angry")
                        "To je dobře. Jeden požár byl až moc.":
                            hide mcPic
                            "Hayfa neodpoví a dál vleče tanečnici směrem ke strážnici."
                "Potřebuješ s ní pomoct?" if "fireshow need help" not in hayfa.asked:
                    hide mcPic
                    $ hayfa.asked.append("fireshow need help")
                    if len(hayfa.asked) - len(origAsked) > 2:
                        $ hayfa.trust -= 1
                    $ hayfa.say("Ne.")
                "{i}(Jít spát){/i}":
                    hide mcPic
                    "Krátce se rozloučíš a necháš hlídkařku projít kolem sebe."
                    return
            jump hayfaFireshowOptions
        "{i}(Pomoct hasit){/i}":
            $ mc.reputation += 3
            $ victim.trust += 1
            $ lisbeth.trust += 1
            $ son.trust += 1
            $ hayfa.trust += 1
            $ status.append("firefighter")
            "Než se stihneš pořádně rozhlédnout, někdo ti vrazí vědro s vodou a pošle tě k nejbližší studně."
            "Brzy zjistíš, že hašení probíhá důkladněji a ve větším počtu lidí, než by nejspíš bylo třeba. Vůz je od domů dostatečně daleko, a když nějaká jiskra náhodou přeskočí, vyhasne sama dřív, než ji někdo stihne zadusit."
            scene bg cart
            "Místní však nenechávají nic náhodě a hasí s nejvyšší pozorností a úsilím. I poté, co největší zášlehy plamenů pohasnou a na místě zůstanou jen dohořívající zbytky, nedopřeje si nikdo odpočinku."
            if ada.status == "grounded":
                "Ačkoli dům mistra Heinricha je ve vedlejší ulici, a není tedy přímo ohrožený, zahlédneš několik známých tváří - Aachim, Rudi a Ferdi pomáhají utloukat odletující jiskry, Lotte nosí džbány s pivem hasícím mužům a sám Heinrich střídavě nosí těžká vědra s vodou a volá na ostatní, kde budou nejužitečnější."
            else:
                "Ačkoli dům mistra Heinricha je ve vedlejší ulici, a není tedy přímo ohrožený, zahlédneš několik známých tváří - Aachim, Rudi a Ferdi pomáhají utloukat odletující jiskry, Ada a Lotte nosí džbány s pivem hasícím mužům a sám Heinrich střídavě nosí těžká vědra s vodou a volá na ostatní, kde budou nejužitečnější."
            "Při hašení nedochází k velkým zmatkům a zdá se, že to je z velké části i jeho zásluha."
            if gender == "M":
                "Z místa se rozejdete až poté, co přestane doutnat poslední uhlík. Jsi unavený a rozbolavělý, ale zároveň máš pocit, jako by mezi vámi během té doby vznikla jistá sounáležitost - jako bys získal právo obyvatele Marendaru nazývat svými sousedy."
            else:
                "Z místa se rozejdete až poté, co přestane doutnat poslední uhlík. Jsi unavená a rozbolavělá, ale zároveň máš pocit, jako by mezi vámi během té doby vznikla jistá sounáležitost - jako bys získala právo obyvatele Marendaru nazývat svými sousedy."
        "{i}(Jít spát){/i}":
            pass
    $ status.append("fireshow")
    $ cells.append(katrin)
    return

label hayfaFireshowOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "fireshow clever" not in hayfa.asked and "fireshow needs punishment" not in hayfa.asked:
        $ optionsRemaining += 1
    if "fireshow needs punishment" not in hayfa.asked:
        $ optionsRemaining += 1
    if "fireshow need help" not in hayfa.asked:
        $ optionsRemaining += 1
    return
