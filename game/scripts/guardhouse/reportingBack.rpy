label reportingBack:
    call cluesOptionsRemainingCheck
    if optionsRemaining == 0 and "provisional watchman" not in status:
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
        "Dílna mistra Heinricha byla zřejmě celou noc odemčená." if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("workshop unlocked")
            $ rauvin.say("Takže přístup mohl mít aspoň teoreticky kdokoli… budeš muset zjistit, kdo všechno měl důvod tu věc ukrást.")
        "Žádné dveře do dílny mistra Heinricha nejsou vypáčené, zloděje musel někdo pustit dovnitř." if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("no forced entry")
            $ rauvin.say("To by mohlo zjednodušit pátrání. Stačí zjistit, kdo tam měl přístup, a okruh podezřelých se tím zúží.")
        "Jedna ze zásuvek u stolu v dílně mistra Heinricha byla násilím vylomená, ale prý z ní nic nechybí." if "break-in" in clues and "missing stuff1" in workshop.checked and "break-in2" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("break-in")
            $ rauvin.say("A myslíš, že to souvisí s tvým případem? Boty by se myslím do zásuvky nevešly, nemohlo se to stát někdy dřív?")
            if gender == "M":
                $ mc.say("Mistr Heinrich o tom nevěděl, dokud jsem na to neupozornil. Víc zatím nevím.")
            else:
                $ mc.say("Mistr Heinrich o tom nevěděl, dokud jsem na to neupozornila. Víc zatím nevím.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "Jedna ze zásuvek v dílně mistra Heinricha byla násilím vylomená." if "break-in" in clues and "missing stuff1" not in workshop.checked and "break-in1" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("break-in")
            $ rauvin.say("Boty by se myslím do zásuvky nevešly, znamená to, že zloděj hledal ještě něco jiného? Ztratilo se z té zásuky něco?")
            if gender == "M":
                $ mc.say("Nevím, neptal jsem se.")
            else:
                $ mc.say("Nevím, neptala jsem se.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
        "V krbu v dílně mistra Heinricha jsem našel stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "M":
            hide mcPic
            $ rauvin.asked.append("burned evidence")
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistý, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "V krbu v dílně mistra Heinricha jsem našla stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "F":
            hide mcPic
            $ rauvin.asked.append("burned evidence")
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistá, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1

        "Mistr Heinrich se rozhádal s polovinou cechu a většinou obchodníků, od kterých bere materiál." if "enemies" in rumelin.asked and "enemies everywhere" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("enemies everywhere")
            $ rauvin.say("To by mohlo být až příliš mnoho podezřelých. Ale měl někdo z nich příležitost se k té věci dostat?")
            if "workshop unlocked" in clues:
                $ mc.say("Dílna byla zřejmě celou noc odemčená, takže bohužel v podstatě kdokoli.")
            elif "doors" in workshop.checked:
                if gender == "M":
                    $ mc.say("Na dveřích do dílny jsem neviděl žádné stopy násilí, takže zřejmě jen někdo, koho tam pustil někdo zevnitř. Nebo komu by se podařilo získat klíč.")
                else:
                    $ mc.say("Na dveřích do dílny jsem neviděla žádné stopy násilí, takže zřejmě jen někdo, koho tam pustil někdo zevnitř. Nebo komu by se podařilo získat klíč.")
        "Mistr Heinrich vyhodil tři učedníky a jeden z nich se prý dostal do špatné společnosti." if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("fired apprentices")
            $ rauvin.say("Pak by rozhodně mohl být dobrý nápad si s nimi promluvit. Víš, kde je najít?")
            $ mc.say("Jeden z nich se přestěhoval do Sehnau, ale ty zbylé dva najdu.")
        "Mistr Heinrich má špatné vztahy i ve své vlastní dílně a tři učedníky už vyhodil." if "enemies" in rumelin.asked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("fired apprentices")
            $ rauvin.say("Pak by mohl být dobrý nápad si se všemi učedníky promluvit. Víš, kde najít ty, co u něj už nejsou?")
            if gender == "M":
                $ mc.say("Jeden z nich se přestěhoval do Sehnau, druzí dva budou někde ve městě. Nejsem si jistý, kde přesně.")
            else:
                $ mc.say("Jeden z nich se přestěhoval do Sehnau, druzí dva budou někde ve městě. Nejsem si jistá, kde přesně.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1

        "Mistr Heinrich má problémy s alkoholem." if kaspar.alreadyMet == True and "alcoholic" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("alcoholic")
            call alcoholicResponse
        "Mistr Kaspar se mi nelíbí. Snažil se mi vlichotit a nevím, nakolik mu můžu věřit." if kaspar.alreadyMet == True in status and "kaspar suspicious" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("kaspar suspicious")
            $ rauvin.trust += 1
            $ hayfa.trust += 2
            $ rauvin.say("Zajímavé. Bylo to jen lichocení, nebo se ti snažil něco podsunout?")
            $ mc.say("Říkal, že mistr Heinrich pije tak moc a je tak vzteklý, že ty boty klidně mohl zničit sám. A naznačoval, že cechmistr by ho právě kvůli tomu mohl chtít znemožnit.")

        "Cechmistr Rumelin včera mistru Heinrichovi vyhrožoval." if "pub fight" in salma.asked and "pub fight" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("pub fight")
            $ mc.say("Prý se osobně postará, aby se nikdy nedostal do čela cechu. To mi zní jako silný motiv.")
            $ rauvin.say("Mistra Rumelina znám spíš jako vyjednavače. Čekal bych, že mistra Heinricha třeba pomluví a poštve proti němu další mistry, ne že by se vloupal do jeho dílny. Ani že by tam někoho poslal.")
            $ rauvin.say("Ukazuje na cechmistra ještě něco dalšího?")
            if gender == "M":
                $ mc.say("Zatím nic, o čem bych věděl.")
            else:
                $ mc.say("Zatím nic, o čem bych věděla.")
            if "rumelin alibi" in salma.asked:
                $ mc.say("Navíc od Salmy odešel o hodně později, než Heinrich.")
            $ rauvin.say("Rozumím. Asi ho nemůžeme zcela vyloučit, ale zaměřil bych se hlavně na jiné podezřelé.")
        "Další podezřelý může být Karsten, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu." if "other fights" in salma.asked and "husband" not in lotte.asked and "karsten" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("karsten")
        "Další podezřelá může být manželka obchodníka, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu. Karsten sám není ve městě, ale jeho žena ano." if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" not in lotte.asked and "Lotte" not in cluesReported:
            hide mcPic
            $ rauvin.asked.appemd("lotte")
        "Další podezřelá může být manželka obchodníka, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu. Karsten sám není ve městě, ale jeho žena prý byla sama doma." if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" in lotte.asked and "Lotte" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("lotte")
        "S případem to možná nesouvisí, ale ševcovští mistři poslední dobou obchodují jinak než dřív." if "less deals" in salma.asked and "less deals" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("AML")
            $ mc.say("Mistr Njal má podle Salmy najednou problém uzavřít obchody a mistr Rumelin uzavírá méně smluv na drahý materiál. Zajímavé je, že smlouvy na prodej zůstávají stejné.")
            "Rauvin se zamračí a zamyslí."
            $ rauvin.say("To opravdu zní trochu zvláštně. Možná to nic neznamená, ale pro jistotu nechám někoho zjistit, jestli se jen nepřesunuli do jiné hospody. A jestli cechmistr pořád prodává zboží, které drahý materiál potřebuje.")
            $ status.append("add investigating less deals")

        "Raději bych si to nechal pro sebe." if "provisional watchman" not in status and gender == "M":
            hide mcPic
            $ rauvin.trust -= 2
            $ status.append("not sharing")
            "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
            jump leaveReporting
        "Raději bych si to nechala pro sebe." if "provisional watchman" not in status and gender == "F":
            hide mcPic
            $ status.append("not sharing")
            $ rauvin.trust -= 2
            "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
            jump leaveReporting
        "Vlastně radši počkám, až budu mít víc stop." if "provisional watchman" in status:
            hide mcPic
            jump leaveReporting

    if "provisional watchman" in status and "report given" not in dailyStatus:
        $ dailyStatus.append("report given")
    if "promised to share" in dailyStatus:
        $ hayfa.trust += 1
        $ dailyStatus.remove("promised to share")
    $ cluesReported.extend(cluesAvailable)

    label leaveReporting:
    if "provisional watchman" in status and "Rauvin visited" not in status:
        $ status.append("Rauvin visited")
    return

label alcoholicResponse:
    $ rauvin.say("To je zajímavé. Vím, že se napije rád, ale nikdy jsem neslyšel o žádných výtržnostech. Odkud tu stopu máš?")
    show mcPic at menuImage
    menu:
        "Říkal to mistr Kaspar. Vypadal, že mluví ze zkušenosti.":
            hide mcPic
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ rauvin.say("Dobrá, nemuselo se ke mně asi donést všechno. Nicméně jestli s tou informací máme pracovat, potřebujeme ji ověřit ještě z dalšího zdroje.")
        "Velmi se mě o tom snažil přesvědčit mistr Kaspar.":
            hide mcPic
            $ mc.say("Když nad tím tak přemýšlím, žádné důkazy nebo zážitky nezmiňoval, jen ho hodně očerňoval. Možná doufal, že mu to pomůže dostat se do čela cechu.")
            $ rauvin.say("Tomu bych klidně věřil. Ale s případem to vůbec nemusí souviset.")
        "Radši si to nechám pro sebe.":
            hide mcPic
            $ rauvin.trust -= 2
            $ hayfa.trust -= 2
            if gender == "M":
                $ rauvin.say("Protože je tvůj zdroj tak tajný, nebo tak málo důvěryhodný? V každém případě myslím, že je na čase, aby ses vrátil k případu.")
            else:
                $ rauvin.say("Protože je tvůj zdroj tak tajný, nebo tak málo důvěryhodný? V každém případě myslím, že je na čase, aby ses vrátila k případu.")
    return
###

label cluesOptionsRemainingCheck:
    $ optionsRemaining = 0
    $ cluesAvailable = []
    if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("workshop unlocked")
    if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("no forced entry")
    if "break-in" in clues and "missing stuff1" in workshop.checked and "break-in2" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in2")
    if "break-in" in clues and "missing stuff1" not in workshop.checked and "break-in1" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in1")
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("burned evidence")
    if "enemies" in rumelin.asked and "enemies everywhere" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies everywhere")
    if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("fired apprentices")
    if "enemies" in rumelin.asked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies at home")
    if kaspar.alreadyMet == True and "alcoholic" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("alcoholic")
    if kaspar.alreadyMet == True and "kaspar suspicious" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("kaspar suspicious")
    if "pub fight" in salma.asked and "pub fight" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("pub fight")
    if "other fights" in salma.asked and "husband" not in lotte.asked and "merchant" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("merchant")
    if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" not in lotte.asked and "Lotte" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Lotte")
    if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" in lotte.asked and "Lotte" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Lotte")
    if "less deals" in salma.asked and "less deals" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("less deals")
    return
