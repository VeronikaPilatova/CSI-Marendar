label arrest:
    python:
        cells.append(arrested[-1])
        newlyArrested = arrested[-1]
        arrestReason = arrested[-1].arrestReason[-1]
        if newlyArrested not in persistent.arrestedPeople:
            persistent.arrestedPeople.append(newlyArrested)

    scene bg guardhouse
    call arrestedEveryoneAchievementCheck
    if newlyArrested == rumelin:
        "TBD: Odvedeš Rumelina do cely."
    elif newlyArrested == eckhard:
        "TBD: Odvedeš Eckharda do cely."
    elif newlyArrested == zeran:
        "TBD: Odvedeš Zerana do cely."
        if arrestReason == "vagrancy":
            call zeranVagrancyArrestReaction

    scene bg cells entrance
    $ currentLocation = "cells"
    if "cells visited" not in status:
        call cellsFirst
        $ status.append("cells visited")

    jump guardhouseAgain

label endArrest:
    if "arrest in progress" in status:
        $ status.remove("arrest in progress")
        scene bg guardhouse
        call guardhouseIntro
    return

###

label zeranVagrancyArrestReaction:
    scene bg cells entrance
    "Když začneš stoupat po schodech od chodby s celami zpět na denní světlo, zjistíš, že dveře zpět do hlavní místnosti jsou zavřené a před nimi, přímo na vrcholku schodiště, stojí Hayfa."
    $ hayfa.say("Vážně jsi právě zahodil[a] svou budoucnost jen proto, aby sis něco dokázal[a]?")
    $ mc.say("... prosím?")
    if gender == "M":
        $ hayfa.say("Zatknul jsi Zerana. Za potulku. Uvnitř domu, ve kterém bydlí. Za takové zneužití moci by se nestyděl ani Velin.", "angry")
    else:
        $ hayfa.say("Zatkla jsi Zerana. Za potulku. Uvnitř domu, ve kterém bydlí. Za takové zneužití moci by se nestyděl ani Velin.", "angry")
    $ mc.say("Neměl žádnou úctu k hlídce! Jak potom můžeme střežit pořádek?")
    $ hayfa.say("My bez zneužívání moci. Ty už nijak.", "angry")
    $ hayfa.say("Teď mi vrať glejt a vypadni z tohohle města.", "angry")
    $ mc.say("Do toho, jestli ve městě zůstanu, přece nemáš, co mluvit.")
    $ hayfa.say("Mám povinnost město chránit před všemi, co mu chtějí ublížit. A o tobě už vím, co jsi zač.")
    "Odevzdáš glejt a hlídkařka ti ustoupí z cesty. Potom tě sleduje pohledem po celou tu nepříjemně dlouhou dobu, dokud nepřejdeš přes strážnici k hlavnímu vchodu a nezazní za tebou bouchnutí pantů."
    scene bg door01
    "Stojíš na ulici a přemýšlíš, kam ještě můžeš jít."
    jump thrownOut
    return

label rumelinArrestReaction:
    if "out of office" not in rauvin.status:
        if "arrest Rumelin" not in rauvin.asked and "rumelin threatened" not in status:
            $ rauvin.say("Mistře Rumeline. Co se stalo, snad proti vám nikdo nespáchal zločin?", "surprised")
            $ rumelin.say("Bohužel ano. [mcName] se rozhodl[a] mě zatknout.", "angry")
            $ rauvin.say("To je... v kompetenci jednotlivých strážných, ano.")
            $ rumelin.say("Takže to tak necháte?", "surprised")
            $ rauvin.say("Věřím, že se to brzy vysvětlí, a okamžitě vám pak dám zprávu. Bohužel vás do té doby budu muset požádat, abyste zůstal. Postupy jsou pevné a pro všechny stejné.")
            $ rumelin.say("Doufám, že mi aspoň uvolníte nějakou místnost se stolem a přinesete mi věci z pracovny. Nemám čas tady jen tak sedět, než si mezi sebou vyříkáte, kdo tu udělal větší hloupost.", "angry")
            $ rauvin.say("To bohužel nebude možné. Jak jsem řekl, postupy jsou pevné a stejné pro všechny.")
            $ rumelin.say("Tím vážnost hlídky rozhodně nezvýšíte. Ale jestli mě chcete zavřít jako kdejakého pobudu, tak prosím, ukažte cestu, ať tahle trapná záležitost co nejdříve skončí.", "angry")
            scene bg cell
            "Dovedeš cechmistra do sklepení, otevřeš jednu z cel a pokyneš, aby vstoupil."
            "On ji pohrdavě přehlédne, vejde dovnitř a beze slova tě sleduje, zatímco zamykáš a odcházíš pryč."
            scene bg guardhouse
            "Nahoře už tě čeká Rauvin a pokyne ti, ať s ním vejdeš do malé boční místnosti - stejné, v jaké jsi prve mluvil[a] s mistrem Heinrichem."

        if "arrest Rumelin" not in rauvin.asked and "rumelin threatened" in status:
            $ rauvin.say("Mistře Rumeline. Co se stalo, snad proti vám nikdo nespáchal zločin?", "surprised")
            if gender == "M":
                $ rumelin.say("Bohužel ano. Provedl jsem určité složitější obchody, které váš podřízen[y] bohužel nepochopil[a], prohlásil[a] je za zločin a chtěl[a] o nich vykládat každému na potkání.")
            else:
                $ rumelin.say("Bohužel ano. Provedl jsem určité složitější obchody, které vaše podřízen[y] bohužel nepochopil[a], prohlásil[a] je za zločin a chtěl[a] o nich vykládat každému na potkání.")
            $ rumelin.say("Ačkoli jsem přesvědčený, že na těch obchodech není nic špatného, někdo by je mohl špatně pochopit, zvlášť v podání někoho, kdo je přehnaně nadšený do hledání zločinů, ale vůbec nerozumí obchodu ani ševcovině.")
            if gender == "M":
                $ rumelin.say("Tak jsem ve slabé chvíli nabídl, že si koupím jeho mlčení. On[a] přijal[a] a teď mě přesně za tyto obchody zatýká.", "angry")
            else:
                $ rumelin.say("Tak jsem ve slabé chvíli nabídl, že si koupím její mlčení. On[a] přijal[a] a teď mě přesně za tyto obchody zatýká.", "angry")
            $ mc.say("Ty obchody měly za cíl znemožnit mistru Njalovi, aby zhotovil mistrovský výrobek na slavnosti.")
            $ rumelin.say("Ty obchody měly chránit cech a mistr Njal výrobek na slavnosti má.", "angry")
            $ mc.say("Ne ten, pro který se nakonec rozhodl.")
            $ rauvin.say("Prosím dost, oba. [mcName] se mnou o zatčení předem nemluvil[a]. Nevím, jestli jsou v pořádku ty zmíněné obchody. Vím, že není v pořádku, když člen hlídky přijímá úplatky.")
            if "AML" in rauvin.asked:
                $ mc.say("Jsou to přesně ty obchody, o kterých jsme spolu už mluvili...")
            $ rauvin.say("Budu vás muset požádat, abyste teď nějakou dobu zůstali v našich celách. Začnu tu věc hned rozplétat a doufám, že se co nejdříve ukáže, kdo půjde domů a kdo před soud.")
            "Pak se Rauvin obrátí přímo k tobě."
            $ rauvin.say("Jedna věc je ale jistá. Tohle zatčení bylo velmi zbrklé a něco podobného si hlídka nemůže dovolit. Vrať mi svůj glejt, ať už tohle nikdy nemůžeš udělat.")
            "Rauvin od tebe převezme listinu a potom vás oba dovede do sklepení."
            scene bg cell
            "Nejdřív otevře jednu z prvních cel a uctivě pokyne mistru Rumelinovi, aby vstoupil. Tebe potom dovede na samý konec chodby."
            "Tvá cela se od ostatních nijak viditelně neliší, je stejně stísněná a slamník stejně tenký. Možná z ní je obtížnější dohlédnout ke vstupním dveřím a zcela určitě nelze zjistit, co o pár kroků dál dělá cechmistr."
            play sound audio.prisonDoorClose
            "Když za tebou zaklapne zámek, Rauvin se k tobě naposledy obrátí."
            $ rauvin.say("Upřímně doufám, že to obvinění o úplatcích se ukáže jako lež. Hlídku sloužící jen některým jsme tu už měli a všichni chtějí velmi jasně vidět, že ty časy už jsou pryč.", "angry")
            $ rauvin.say("Pranýř nemusí být těžký trest, ale když vůči odsouzenému celé město cítí zášť...")
            $ rauvin.say("Ale proč by zrovna o tom cechmistr lhal, že ano? Kdyby neměl dobrý důvod, jen by si tím zbytečně zkazil pověst.")
            "S tím se otočí a ponechá tě představám, jak asi bude tvůj osud vypadat."
    return
