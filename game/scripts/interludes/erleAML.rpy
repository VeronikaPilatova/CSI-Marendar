label erleAMLresults:
    if "investigating less deals erle ongoing" in status:
        $ status.remove("investigating less deals erle ongoing")

    $ random = renpy.random.randint(1, 6)
    scene expression ("bg/bg street0[random].png")
    "Během chůze po městě si všimneš žebračky Erle, která na tebe zamává a vydá se směrem k tobě."
    $ erle.say("Trochu jsem si protáhla nohy, ale obešla jsem všechny hospody ve městě.", "happy")
    $ mc.say("A jak to dopadlo?")
    if "investigating without explanation" in erle.asked:
        $ erle.say("Dost se divili, proč mě to zajímá, a když jsem o tom nechtěla mluvit, přišlo jim to divné.")
        $ erle.say("Byli moc milí, ptali se, jestli mi nic není, a dokonce mi několikrát nabídli trochu polévky. Ale o mistru Rumelinovi mi toho moc neřekli.", "sad")
        $ erle.say("Moc se omlouvám, dělala jsem, co jsem uměla.", "sad")
        $ erle.say("Ale nic si z toho nedělej. To je tak vždycky, když má jeden nějaký velký plán. Lepší žádné nedělat.")
        show mcPic at menuImage
        menu:
            "Nevadí, díky za snahu. Tady máš odměnu.":
                hide mcPic
                $ erle.say("Jsi moc laskav[y]! A tolik peněz, asi se budu muset s někým rozdělit. Děkuji.", "happy")
            "To jsem čekal[a] víc. Za to žádnou odměnu nedostaneš.":
                hide mcPic
                $ erle.say("Ale to je v pořádku, říkala jsem přece, že jsem dostala polévku. To na jeden den stačí.", "happy")
        $ erle.say("Teď se půjdu někam natáhnout, trochu mě z toho chození bolí nohy.", "happy")
        return
    elif "working for the watch" in erle.asked:
        $ erle.say("Trochu se divili, že hlídka posílá na pochůzky zrovna mě, čekali by spíš toho mladého elfa. Ale byli moc milí a sdílní.", "happy")
    else:
        $ erle.say("Trochu se divili, proč mě to zajímá, ale asi si řekli, že takovou bláznivou ženskou jako já může zajímat cokoli. Rozhodně byli moc milí a sdílní.", "happy")
    $ erle.say("Prý k nikomu z nich mistr Rumelin chodit nezačal. Tedy do těch lepších podniků občas s někým zajde, ale nedělá tam žádné obchody, na které by tam nebyli zvyklí, ani jich není víc.")
    $ mc.say("Děkuju, to je přesně to, co jsem potřeboval[a] vědět.")
    $ mc.say("Tady máš odměnu. Doufám, že to bude stačit.")
    $ erle.say("Ale co tě napadá! Víc, než stačit. Možná se s někým ještě rozdělím.", "happy")
    $ erle.say("A pak si půjdu koupit placku a někam se natáhnout.")
    "Žebračka ti zamává a volným krokem se opět vydá do města."
    return