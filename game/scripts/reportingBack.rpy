label reportingBack:
    call cluesOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Vlastně zatím nic, co by mi přišlo dostatečně důležité.")
        $ rauvin.trust -= 2
        $ hayfa.trust -= 2
        $ status.append("no clue")
        if gender == "M":
            $ rauvin.say("V tom případě bys měl s pátráním co nejdřív začít, Einionovy slavnosti začínají už za čtyři dny.")
        else:
            $ rauvin.say("V tom případě bys měla s pátráním co nejdřív začít, Einionovy slavnosti začínají už za čtyři dny.")
        return

    show mcPic at menuImage
    menu:
        "(Mistrova) dílna byla zřejmě celou noc odemčená." if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
            hide mcPic
            $ rauvin.say("Takže přístup mohl mít aspoň teoreticky kdokoli… budeš muset zjistit, kdo všechno měl důvod tu věc ukrást.")
        "Žádné dveře do (mistrovy) dílny nejsou vypáčené, zloděje musel někdo pustit dovnitř." if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
            hide mcPic
            $ rauvin.say("To by mohlo zjednodušit pátrání. Stačí zjistit, kdo tam měl přístup, a okruh podezřelých se tím zúží.")
        "Jedna ze zásuvek v (mistrově) stole v dílně byl násilím vylomený, ale prý z něj nic nechybí." if "break-in" in clues and "missing stuff1" in workshopChecked and "break-in2" not in cluesReported:
            hide mcPic
            $ rauvin.say("A myslíš, že to souvisí s tvým případem? Boty by se myslím do zásuvky nevešly, nemohlo se to stát někdy dřív?")
            if gender == "M":
                $ mc.say("(Okradený mistr) o tom nevěděl, dokud jsem na to neupozornil. Víc zatím nevím.")
            else:
                $ mc.say("(Okradený mistr) o tom nevěděl, dokud jsem na to neupozornila. Víc zatím nevím.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "Jedna ze zásuvek v (mistrově) dílně byla násilím vylomená." if "break-in" in clues and "missing stuff1" not in workshopChecked and "break-in1" not in cluesReported:
            hide mcPic
            $ rauvin.say("Boty by se myslím do zásuvky nevešly, znamená to, že zloděj hledal ještě něco jiného? Ztratilo se z té zásuky něco?")
            if gender == "M":
                $ mc.say("Nevím, neptal jsem se.")
            else:
                $ mc.say("Nevím, neptala jsem se.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
        "V krbu v (mistrově) dílně jsem našel stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "M":
            hide mcPic
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistý, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "V krbu v (mistrově) dílně jsem našla stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "F":
            hide mcPic
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistá, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "(Okradený mistr) se rozhádal s polovinou cechu a většinou obchodníků, od kterých bere materiál." if "enemies" in guildmasterAsked and "enemies everywhere" not in cluesReported:
            hide mcPic
            $ rauvin.say("To by mohlo být až příliš mnoho podezřelých. Ale měl někdo z nich příležitost se k té věci dostat?")
            if "workshop unlocked" in clues:
                $ mc.say("Dílna byla zřejmě celou noc odemčená, takže bohužel v podstatě kdokoli.")
            elif "doors" in workshopChecked:
                $ mc.say("Na dveřích do dílny jsem neviděl/a žádné stopy násilí, takže zřejmě jen někdo, koho tam pustil někdo zevnitř. Nebo komu by se podařilo získat klíč.")
        "(Okradený mistr) vyhodil tři učedníky a jeden z nich se prý dostal do špatné společnosti." if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
            hide mcPic
            $ rauvin.say("Pak by rozhodně mohl být dobrý nápad si s nimi promluvit. Víš, kde je najít?")
            $ mc.say("Jeden z nich se přestěhoval do Sehnau, ale ty zbylé dva najdu.")
        "(Okradený mistr) má špatné vztahy i ve své vlastní dílně a tři učedníky už vyhodil." if "enemies" in guildmasterAsked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
            hide mcPic
            $ rauvin.say("Pak by mohl být dobrý nápad si se všemi učedníky promluvit. Víš, kde najít ty, co u něj už nejsou?")
            if gender == "M":
                $ mc.say("Jeden z nich se přestěhoval do Sehnau, druzí dva budou někde ve městě. Nejsem si jistý, kde přesně.")
            else:
                $ mc.say("Jeden z nich se přestěhoval do Sehnau, druzí dva budou někde ve městě. Nejsem si jistá, kde přesně.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
        "Raději bych si to nechal pro sebe." if gender == "M":
            hide mcPic
            $ rauvin.trust -= 2
            $ status.append("not sharing")
            "" "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
        "Raději bych si to nechala pro sebe." if gender == "F":
            hide mcPic
            $ status.append("not sharing")
            $ rauvin.trust -= 2
            "" "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
    $ cluesReported.extend(cluesAvailable)
    return

label cluesOptionsRemainingCheck:
    $ optionsRemaining = 0
    $ cluesAvailable = []
    if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("workshop unlocked")
    if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("no forced entry")
    if "break-in" in clues and "missing stuff1" in workshopChecked and "break-in2" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in2")
    if "break-in" in clues and "missing stuff1" not in workshopChecked and "break-in1" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in1")
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("burned evidence")
    if "enemies" in guildmasterAsked and "enemies everywhere" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies everywhere")
    if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("fired apprentices")
    if "enemies" in guildmasterAsked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies at home")
    return
