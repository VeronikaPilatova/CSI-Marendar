label dancerController:
    $ origAsked = katrin.asked.copy()
    call dancerCellsIntro
    call dancerOptions
    $ katrin.alreadyMet = True
    $ time.addMinutes((len(katrin.asked) - len(origAsked)) * 3)
    return

label dancerCellsIntro:
    scene bg cell
    "Dívka sedí na kavalci u stěny naproti mřížím a rukama si objímá kolena a ramena. Sukni má těsně přitaženou k tělu a ruce má holé až na několik blyštivých náramků. V přítmí cel to není snadné poznat s jistotou, ale zdá se, že se jemně chvěje."
    "Když k ní přijdeš, vzhlédne, ale nic neříká a jen tě pozoruje."
    return

label dancerOptions:
    call dancerOptionsRemainingCheck
    if optionsRemaining == 0:
        "Otočíš se a necháš dívku svému osudu."
        return

    show mcPic at menuImage
    menu:
        "Kdo jsi?" if "introductions" not in katrin.asked:
            hide mcPic
            $ katrin.asked.append("introductions")
            $ katrin.say("Na to už jste se mě ptali. Jmenuju se Katrin, pocházím z X u Y a snažím se dostat do Eichenau nebo prostě někam, kde se dá bezpečně žít.")
            $ katrin.say("A žádnou Luisu opravdu neznám. Kdo to vůbec je? Ta... ta tmavovlasá hlídkařka, co mě sem přivedla, ji zmínila několikrát.", "surprised")
            show mcPic at menuImage
            menu:
                "Tady kladu otázky já.":
                    hide mcPic
                    $ katrin.say("Jistě, promiňte. Já jen... to vystoupení bylo vážně bezpečné, ale na to se mě zatím ještě neptal nikdo.", "sad")
                "Jediná Luisa, o které vím, je Rauvinova sestra.":
                    hide mcPic
                    if "Luisa arsonist" in globalClues:
                        $ mc.say("Hayfa ji myslím podezřívá ze spolupráce na založení požáru Marendaru.")
                    $ katrin.say("Neznám ani žádného Rauvina... proč bych s někým z nich měla mít co do činění? A ještě na přípravě zločinu?", "surprised")
                    $ mc.say("To se bude potřeba zeptat Hayfy.")
                    $ katrin.say("Děkuji, ale to možná nebude potřeba...")
                "Nemám tušení.":
                    hide mcPic
                    $ katrin.say("Škoda. Tedy ono je to asi lepší. Musí to být nějaký hrozný zločinec a o těch je možná lepší ani nevědět.")
        "Cestuješ sama?" if "introductions" in katrin.asked and "alone" not in katrin.asked and "brother" not in katrin.asked:
            hide mcPic
            $ katrin.asked.append("alone")
            $ katrin.say("Ještě... ještě s mladším bratrem.")
            $ katrin.say("Hrál mi k tanci podle toho, jak jsem řekla, nic víc. Rozhodně nevybíral, jaké číslo bude následovat.", "angry")
        "K vystoupení ti hrál nějaký kluk, to je kdo?" if "brother" not in katrin.asked and "alone" not in katrin.asked:
            hide mcPic
            $ katrin.asked.append("brother")
            $ katrin.say("Můj mladší bratr. Jmenuje se Kilian.")
            $ katrin.say("Prostě brnkal podle toho, co jsem řekla. Rozhodně nevybíral, jaké číslo bude následovat.", "angry")
        "Víš, co ti hrozí za trest?" if "punishment" not in katrin.asked:
            hide mcPic
            $ katrin.asked.append("punishment")
            $ katrin.say("No... ne úplně. Ta hlídkařka stihla během cesty vyjmenovat skoro všechny tresty, co znám, a ještě nějaké další.", "sad")
            $ katrin.say("Ale nevím, co z toho je jen za nošení ohně uvnitř města a co za žhářství.", "sad")
        "Je ti zima?" if "cold" not in katrin.asked:
            hide mcPic
            $ katrin.asked.append("cold")
            "Dívka krátce pokrčí rameny."
            $ katrin.say("Tyhle šaty jsou myšlené na tanec, ne na sezení ve sklepě.")
            menu:
                "{i}(Sehnat jí něco přes sebe){/i}":
                    $ katrin.trust += 1
                    $ hayfa.trust -= 1
                    "Krátce prohlédneš okolní cely. Pokrývky vězni zjevně nikdy nedostávali, ale v zapadlém koutě najdeš několik plášťů, které snad dřív někdo nosil na slavnostní příležitosti."
                    "Jeden doneseš dívce a prostrčíš ho skrz mříže. Ona se do něj vděčně zabalí a zůstane stát naproti tobě."
                    $ katrin.asked.append("received cloak")
                "{i}(Položit jinou otázku.){/i}":
                    pass
        "{i}(Odejít){/i}":
            hide mcPic
            "Otočíš se a necháš dívku svému osudu."
            return
    jump dancerOptions

###

label dancerOptionsRemainingCheck:
    $ optionsRemaining = 0

    if "introductions" not in katrin.asked:
        $ optionsRemaining += 1
    if "introductions" in katrin.asked and "alone" not in katrin.asked and "brother" not in katrin.asked:
        $ optionsRemaining += 1
    if "brother" not in katrin.asked and "alone" not in katrin.asked:
        $ optionsRemaining += 1
    if "punishment" not in katrin.asked:
        $ optionsRemaining += 1
    if "cold" not in katrin.asked:
        $ optionsRemaining += 1
    return
