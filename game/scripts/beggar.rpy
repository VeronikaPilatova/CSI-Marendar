label erleController:
    # check if visit makes sense
    call erleOptionsRemainingCheck
    if optionsRemaining == 0:
        "Nenapadá tě, co dalšího se Erle ještě ptát."
        return
    call preludeController

    # walk over
    if erle.alreadyMet == False:
        $ time.addMinutes(30)
    else:
        $ time.addMinutes(15)
    $ currentLocation = "old bridge"
    $ origAsked = erle.asked.copy()

    # visit itself
    play music audio.erle fadeout 0.5 if_changed
    scene bg bridge
    if erle.alreadyMet == False:
        call erleFirst
    else:
        call erleAgain
    call erleOptions
    call leavingErle

    # adjust time spent and status
    $ time.addMinutes((len(erle.asked) - len(origAsked)) * 3)
    if erle.alreadyMet == False:
        $ erle.alreadyMet = True
    stop music fadeout 0.5
    return

label erleFirst:
    "Starý most najdeš snadno a u něj na břehu řeky skutečně sedí osamělá trpaslice."
    if time.hours < 18:
        "Na Erle je sice vidět život na ulici, nevypadá ale ani zdaleka tak zuboženě nebo zoufale, jak bys od žebráka čekal. Jak sedí na kusu staré deky, tvář s přivřenýma očima nastavenou příjemnému podzimnímu slunci, působí vlastně téměř spokojeně."
    else:
        "Na Erle je sice vidět život na ulici, nevypadá ale ani zdaleka tak zuboženě nebo zoufale, jak bys od žebráka čekal. Jak sedí na kusu staré deky a pozoruje vycházející hvězdy, působí vlastně téměř spokojeně."
    "Když se přiblížíš, natáhne k tobě ruku, aniž by se na tebe pořádně podívala."
    show mcPic at menuImage
    menu:
        "{i}(Dát jí pár mincí){/i}":
            hide mcPic
            $ erle.trust += 1
            $ erle.say("Děkuju.", "happy")
            "Erle se na tebe usměje, podívá se na mince a pak ti jich asi polovinu vrátí."
            $ erle.say("Nech si něco i pro sebe.", "happy")
            show mcPic at menuImage
            menu:
                "No dobře...":
                    hide mcPic
                    "Trochu zmateně vrácené peníze zase schováš."
                "Já mám peněz dost.":
                    hide mcPic
                    $ erle.say("Já teď už taky. Tak si třeba zajdi na něco dobrého.", "happy")
            $ mc.say("Ty jsi Erle? Jsem z městské hlídky a chci ti položit pár otázek.")
        "Ty jsi Erle? Jsem z městské hlídky a chci ti položit pár otázek.":
            hide mcPic
    $ erle.say("Proč ne, času mám dost. Neposadíš se?", "happy")
    "Erle se trochu posune, aby ti udělala místo na dece."
    return

label erleAgain:
    "Erle znovu najdeš na jejím obvyklém místě."
    return

label erleOptions:
    call erleOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("To je všechno, na co jsem se chtěl[a] zeptat.")
        return

    show mcPic at menuImage
    menu:
        "Prý jsi dnes ráno donesla Salmě nějaké lahve?" if "bottles" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles")
            $ erle.say("To je pravda. Ty byly krásné, moc hezká práce. Taky z nich měla Salma radost.", "happy")
        "Jak ses k těm lahvím dostala?" if "bottles" in erle.asked and "bottles 2" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles 2")
            $ erle.say("Našla jsem je pohozené v blátě. Nejspíš někdo bohatý, kdo neví, že sklo má cenu.")
        "Kde přesně byly?" if "bottles 2" in erle.asked and "bottles location" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles location")
            $ erle.say("Kousek odtud po proudu řeky, zachycené těsně u břehu. Někdo je asi chtěl hodit do vody.")
            $ mc.say("Na tomhle břehu?")
            $ erle.say("Myslím… asi ano. Proč?")
            show mcPic at menuImage
            menu:
                "Ty lahve byly nejspíš kradené.":
                    hide mcPic
                "Souvisí to s mým vyšetřováním.":
                    hide mcPic
                "Zajímá mě, kam tu lidé vyhazují odpadky.":
                    hide mcPic
        "Bylo mezi těmi odpadky ještě něco dalšího?" if "bottles 2" in erle.asked and "anything else" not in erle.asked:
            hide mcPic
            $ erle.asked.append("anything else")
            $ erle.say("Nějaké odstřižky a kusy kůže a jedny poničené boty. Ty byly taky hezké, ale moc tenké na rozumné nošení, i kdyby nebyly popálené a celé promočené. Ale proč vyhodili ty lahve, to nechápu.")
            $ erle.say("No, jejich škoda. Stěžovat si nebudu.", "happy")
        "Máš ty boty ještě? Můžu je vidět?" if "anything else" in erle.asked and "shoes" not in erle.asked:
            hide mcPic
            $ erle.asked.append("shoes")
            $ erle.say("Nechala jsem je tam. K čemu by mi byly?")
        "Přesně stejné lahve se ztratily z domu mistra Heinricha." if "bottles" in erle.asked and "bottles stolen" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles stolen")
            $ erle.say("Pak má Heinrich dobrý vkus.", "happy")
            $ erle.say("A asi je bohatý a neví, že sklo má cenu.")
            "Erle pokrčí rameny."
        "Proč nežebráš na nějakém lepším místě? Třeba před nějakých chrámem?" if "chosen place" not in erle.asked:
            hide mcPic
            $ erle.asked.append("chosen place")
            $ mc.say("Mohla bys mít víc peněz.")
            $ erle.say("Stačí mi, když se mám další den za co najíst. Tady se mi líbí a nemusím tu poslouchat žádné poučky o správné cestě. Navíc pod most se můžu schovat před deštěm nebo kroupami.", "happy")
        "Kdybys potřebovala střechu nad hlavou, vím o jedné ubytovně." if sabri.alreadyMet == True and "Sabri" not in erle.asked:
            hide mcPic
            $ erle.asked.append("Sabri")
            $ erle.say("Tu, co ji vede ten divný kněz, jak se to... Sabri?")
            $ mc.say("Ano...")
            $ erle.say("Tak to nejsi první, kdo mě tam posílá.")
            $ mc.say("A Sabri tě nepřijal?")
            $ erle.say("Nelíbil se mi. Pořád do každého něco hučí o tom, že je lepší než ostatní, má na víc a měl by za tím jít.", "angry")
            show mcPic at menuImage
            menu:
                "A co je na tom špatně?":
                    hide mcPic
                "Taky se mi nelíbil, ale není to lepší, než spát na ulici?":
                    hide mcPic
                    $ erle.say("Radši budu na ulici s čistou hlavou, než pod jednou střechou s někým takovým. Nemohla jsem se zbavit pocitu, že by se mnou měl nějaké vlastní plány.")
            $ erle.say("A co je špatně na tom, být spokojená s tím, co mám?")
        "Jak můžeš být spokojená s tímhle životem?" if "Sabri" in erle.asked and "satisfied" not in erle.asked:
            hide mcPic
            $ erle.asked.append("satisfied")
            $ erle.say("Je hezký den a já měla k snídani moc dobrou teplou polívku. Nic mi nechybí a nic mi nepřebývá.", "happy")
            $ mc.say("Co střecha nad hlavou, ta ti opravdu nechybí?")
            $ erle.say("Aspoň se nemusím bát, že o ni zase přijdu. K čemu je pachtit se za věcmi, které ti potom stejně nezůstanou?")
        "Mohla bys mě naučit, jak být spokojený v bídě?" if "teach me" not in erle.asked and gender == "M":
            call erleTeachMe
        "Mohla bys mě naučit, jak být spokojená v bídě?" if "teach me" not in erle.asked and gender == "F":
            call erleTeachMe
        "Myslíš, že takhle na tebe můžou být tví předkové hrdí?" if race == "dwarf" and "ancestors" not in erle.asked:
            hide mcPic
            $ erle.asked.append("ancestors")
            $ erle.say("Podle předků jsem se snažila žít většinu života. Štěstí mi to nepřineslo a jestli na mě předkové hrdí byli, pak mi to nedali nijak najevo. Tak teď ať si svůj názor nechají pro sebe.", "angry")
            $ erle.say("Oni to mají jednoduché, ti už o nic přijít nemůžou.")
            show mcPic at menuImage
            menu:
                "To není pravda.":
                    hide mcPic
                    $ mc.say("Pokud na naše předky zapomeneme, přestaneme o nich vyprávět a vážit si jich, nic po nich nezůstane. To ti nepřijde jako ztráta?")
                    $ erle.say("Pak budeme mít konečně klid a oni taky.")
                    "Erle pokrčí rameny, ale její sevřené rty a pohled stranou působí méně lhostejně, než by asi chtěla."
                "Na tom vlastně něco bude.":
                    hide mcPic
                    "Erle mlčky přikývne a dál už se k tématu nevrací."
        "To jsou všechny moje otázky.":
            hide mcPic
            return
    jump erleOptions

label leavingErle:
    menu:
        "{i}(Zkontrolovat místo nálezu){/i}":
            "Vydáš se po proudu řeky, rozhlížíš se po břehu a doufáš, že tu boty pořád ještě budou."
            scene bg riverbank
            "Slunce stále příjemně svítí, ale tady u vody je o něco chladněji než uprostřed města a proud unáší spadané listy. Doufáš, že se ti podaří u hlídky uchytit a nebudeš muset trávit zimu někde na profukujícím seníku."
            "Nakonec Heinrichovy boty v blátě málem přehlédneš a musíš se několik kroků vrátit. Promočený, špinavý a deformovaný kus fialové kůže mistrovské dílo příliš nepřipomíná a až na bližší pohled začneš rozpoznávat kovové ozdoby a elegantní tvarování."
            "Pokusíš se je v řece co nejvíc očistit, ale nemusíš být švec, aby ti bylo jasné, že je už nelze zachránit."
            $ status.append("stolen shoes found")
        "{i}(Vrátit se na strážnici){/i}":
            pass
    return

###

label erleTeachMe:
    hide mcPic
    $ erle.asked.append("teach me")
    if time.hours > 17:
        $ erle.say("Vidíš, jak krásně svítí hvězdy? Stačí si prostě říct, že víc k dobrému životu nepotřebuješ.")
    else:
        $ erle.say("Vidíš, jak krásně svítí slunce? Stačí si prostě říct, že víc k dobrému životu nepotřebuješ.")
    show mcPic at menuImage
    menu:
        "Mít hezký dům a spoustu dobrého jídla by mi přišlo mnohem lepší.":
            hide mcPic
            $ erle.say("Dokud bys o to nepři[sel]. Pak by to bylo mnohem horší, než nemít nic od začátku.", "sad")
        "Na tom možná něco bude.":
            hide mcPic
            "Erle jen přikývne a víc se k tématu nevrací."
        "Co bys dělala, kdyby pršelo?":
            hide mcPic
            $ erle.say("Schovala se pod most, poslouchala zvuk deště a užívala si, že kolem nikdo není a já mám klid.")
    return

###

label erleOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "bottles" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles" in erle.asked and "bottles 2" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles 2" in erle.asked and "bottles location" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles 2" in erle.asked and "anything else" not in erle.asked:
        $ optionsRemaining += 1
    if "anything else" in erle.asked and "shoes" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles" in erle.asked and "bottles stolen" not in erle.asked:
        $ optionsRemaining += 1
    if "chosen place" not in erle.asked:
        $ optionsRemaining += 1
    if sabri.alreadyMet == True and "Sabri" not in erle.asked:
        $ optionsRemaining += 1
    if "Sabri" in erle.asked and "satisfied" not in erle.asked:
        $ optionsRemaining += 1
    if race == "dwarf" and "ancestors" not in erle.asked:
        $ optionsRemaining += 1
    if "teach me" not in erle.asked:
        $ optionsRemaining += 1
    return
