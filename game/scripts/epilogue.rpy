label mcArrested:
    call otherPrisoners
    if time.days == 3 or (time.days == 2 and time.hours > 21):
        "Rauvin se zanedlouho vrátí k tvé cele. Ve tmě mu nevidíš dobře do tváře, ale skutečně vypadá vyčerpaně."
    if gender == "M":
        $ rauvin.say("Ještě tě musím požádat o vrácení glejtu, který tě opravňuje jednat za městskou hlídku. Pokud se ukáže, že ses nedopustil zločinného jednání, dostaneš ho pochopitelně zpátky. Ačkoli naději na něco podobného nevidím velkou.")
    else:
        $ rauvin.say("Ještě tě musím požádat o vrácení glejtu, který tě opravňuje jednat za městskou hlídku. Pokud se ukáže, že ses nedopustila zločinného jednání, dostaneš ho pochopitelně zpátky. Ačkoli naději na něco podobného nevidím velkou.")
    menu:
        "{i}(Odevzdat listinu){/i}":
            "Prostrčíš listinu mřížemi. Rauvin se na ni sotva podívá a uloží si ji do kapsy."
        "{i}(Odmítnout){/i}":
            "Namísto odpovědi jen lehce zavrtíš hlavou."
            $ rauvin.say("Toto odmítnutí znamená porušení městských zákonů z tvé strany a soud k němu přihlédne.")
            if time.hours > 21:
                $ rauvin.say("Někdo se tě znovu zeptá ráno. Doporučuji vyhovět, tvoje vyhlídky už tak nejsou dobré.")
            else:
                $ rauvin.say("Někdo se tě ještě před začátkem procesu zeptá znovu. Doporučuji vyhovět, tvoje vyhlídky už tak nejsou dobré.")
    if "arrested during break in" in status:
        if mc.imageParameter == "beaten":
            if gender == "M":
                $ rauvin.say("Jelikož rozumím, že jsi mistra Heinricha a jeho syna ohrožoval na zdraví, budeš nakonec rád, když vyvázneš živý.")
            else:
                $ rauvin.say("Jelikož rozumím, že jsi mistra Heinricha a jeho syna ohrožovala na zdraví, budeš nakonec ráda, když vyvázneš živá.")
        else:
            if gender == "M":
                $ rauvin.say("Když ti bude soud nakloněný, můžeš vyváznout jen s pranýřem. Pokud se ale zjistí, že jsi zneužil důvěry mistra Heinricha, když tě vpustil do svého domu, nebo že jsi jeho nebo jeho rodinu ohrožoval na zdraví, budeš nakonec rád, když vyvázneš živý.")
            else:
                $ rauvin.say("Když ti bude soud nakloněný, můžeš vyváznout jen s pranýřem. Pokud se ale zjistí, že jsi zneužila důvěry mistra Heinricha, když tě vpustil do svého domu, nebo že jsi jeho nebo jeho rodinu ohrožovala na zdraví, budeš nakonec ráda, když vyvázneš živá.")
    if time.hours > 21:
        $ rauvin.say("S vyšetřováním začneme zítra.")
        "S těmito slovy tě opustí a zanechá tě v cele bez možnosti výrazně ovlivnit svůj osud."
        jump thrownOut
    return

label workshopNightArrestAfter:
    scene bg black
    "Tvůj odpočinek je však kratší, než doufáš."
    $ runa.say("Dovol, %(callingMc)s, jen tě takhle chytnu, ať nikam neutečeš.")
    scene bg hayloft night
    "Probudí tě pevný dotyk na rameni. Škubneš sebou a zkusíš se odtáhnout, ale zjistíš, že tě drží víc než jeden pár rukou a že ten úchop je pevný."
    $ solian.say("Klídek, nemá smysl se prát. Jen se zeptáme na pár věcí, a jestli je všechno v pořádku, můžeš za chvíli zase běžet.")
    "Rozhlédneš se lépe a o pár kroků dále spatříš Rauvina. Vypadá bledší než obvykle, možná to je světlem, možná nedostatkem spánku."
    if gender == "M":
        $ rauvin.say("Mistr Heinrich tvrdí, že tě jeho syn přistihl při vloupání do jejich dílny dnes v noci. Byl jsi tam?")
    else:
        $ rauvin.say("Mistr Heinrich tvrdí, že tě jeho syn přistihl při vloupání do jejich dílny dnes v noci. Byla jsi tam?")
    show mcPic at menuImage
    menu:
        "Ano, ale nic jsem tam nevzal." if gender == "M":
            hide mcPic
            $ status.append("confessed to break-in")
            $ rauvin.say("To je pouze tvé tvrzení a beztak se jedná o neoprávněné vniknutí.")
        "Ano, ale nic jsem tam nevzala." if gender == "F":
            hide mcPic
            $ status.append("confessed to break-in")
            $ rauvin.say("To je pouze tvé tvrzení a beztak se jedná o neoprávněné vniknutí.")
        "Ano, ale jen jako součást vyšetřování.":
            hide mcPic
            $ status.append("confessed to break-in")
            $ runa.say("Co že jsi?", "surprised")
            $ rauvin.say("Tohle ale není způsob, jak by hlídka měla vyšetřovat. Pořád se jedná o neoprávněné vniknutí.")
        "Ne, co to je za nesmysl?":
            hide mcPic
            $ rauvin.say("Pak je to tvrzení proti tvrzení. To obvinění je vážné, nemůžu ho jen tak smést se stolu.")
    $ rauvin.say("Budeme tě muset dát do cely, než se to aspoň trochu prošetří. Je to hlavně, aby to nevypadalo, že to nebereme dost vážně. Jestli v tom jsi nevinně, nemělo by to být na dlouho.")
    $ rauvin.say("Aspoň se tam budeš moct dospat.")
    "Tvůj velitel si povzdychne a promne si obličej. Pak se otočí a vyjde z místnosti. Runa a Solian se po sobě podívají a potom ti naznačí, že se máš zvednout a spolu s nimi Rauvina následovat."
    scene bg street01 dark
    "Cesta na strážnici netrvá dlouho. Rauvin jde pár kroků před vámi, má skloněnou hlavu a jako by vůbec nevnímal, co se kolem něj děje. Druzí dva strážní tě nicméně drží pevně a nedají ti žádnou příležitost k útěku."
    scene guardhouse dark
    "Brzy tak znovu dorazíte na strážnici. Její prostory už znáš, s hlídkařem po každém boku však působí o poznání pochmurněji."
    scene bg cell night
    "I cela je zevnitř mnohem stísněnější, než se ti kdy předtím zdálo."
    play sound audio.prisonDoorClose
    "Potom zaklapne zámek, a aniž by se tě tví kolegové na cokoli dalšího ptali, zanechají tě ve tmě."
    call otherPrisoners
    scene bg cell with dissolve
    if len(cells) > 0:
        "Čekání trvá několik hodin. Prostor se alespoň trochu prosvětlí, jak venku vyjde slunce, a dostaneš jednoduchou kaši k snídani. Potom se ozvou spěšné kroky a před tvou celou se objeví Solian. Mluví rychleji než obvykle a působí, že se kromě rozhovoru soustředí i na nějaké úplně jiné myšlenky nebo úkoly."
    else:
        "Čekání trvá několik hodin. Prostor se alespoň trochu prosvětlí, jak venku vyjde slunce, a dostaneš jednoduchou kaši k snídani. Potom se ozvou spěšné kroky a před tvou celou se objeví Solian. Mluví rychleji než obvykle a působí, že se kromě rozhovoru soustředí i na nějaké úplně jiné myšlenky nebo úkoly."
    if "confessed to break-in" in status:
        $ solian.say("Prý musíme obviněné držet v obraze, jak si na tom stojí, tak tedy dobře, ať mě Rauvin neseřve, jakmile se uzdraví.", "angry")
        $ solian.say("Prověřili jsme tvůj výlet v noci a nevypadá to s tebou dobře. Soudce tě bude chtít vidět během pár dní.")
    else:
        $ solian.say("Prý musíme všem vždy říkat obvinění, tak tedy dobře, ať mě Rauvin neseřve, jakmile se uzdraví. Zatýkám tě za vloupání do dílny mistra Heinricha.", "angry")
        $ solian.say("Doteď to bylo jen zadržení pro jistotu, aby mistr viděl, že jeho stížnost bereme vážně, ale teď už to je opravdu zatčení a půjdeš před soud.")
    $ solian.say("V dílně tě viděl jeho syn a jeden zámečník dosvědčil, že pro tebe vyrobil kopii klíče, který je podezřele podobný tomu od dílny. A že se k tobě ten klíč dostal, to také víme. To je dost na to, aby to šlo k soudu, bez ohledu na přiznání.")
    if gender == "M":
        $ solian.say("Při troše štěstí můžeš vyváznout jen s pranýřem, ale jestli ti vážně mistr Heinrich svěřil svůj klíč a ty jsi ho takhle zneužil, no nevím nevím.", "angry")
    else:
        $ solian.say("Při troše štěstí můžeš vyváznout jen s pranýřem, ale jestli ti vážně mistr Heinrich svěřil svůj klíč a ty jsi ho takhle zneužila, no nevím nevím.", "angry")
    $ solian.say("Nepočítej s tím, že tě hlídka nepodrží. Naopak, Rauvin i velitel Galar se budou snažit všechny upokojit, že hlídka v žádném případě nedělá nic špatného, a když to nějaký jednotlivec udělá, tak se ho rychle a rázně zbaví.")
    $ solian.say("Být tebou si tedy připravím nějakou hodně dobrou obhajobu.")
    $ solian.say("A já teď ke všem ostatním věcem musím nějak uklidnit mistra Heinricha a ještě mu za půl dne najít toho zatraceného zloděje, prostě nádhera.", "angry")
    "S tím se otočí a zanechá tě v cele čekat, zda bude soud milosrdný."
    jump thrownOut

label otherPrisoners:
    if zeran in cells or rumelin in cells:
        if zeran in cells:
            $ zeran.say("Copak, někdo si všiml, že jsi také nuzák, co nebude nikomu chybět? Jaké bylo probuzení?")
        if rumelin in cells:
            $ rumelin.say("Jsem rád, že hlídka začala dávat věci do pořádku. Konečně. Ale stejně se z mého zatčení budete zodpovídat.", "angry")
    elif kaspar in cells or njal in cells:
        if kaspar in cells:
            if gender == "M":
                $ kaspar.say("Tak už jste konečně pochopili, co je tenhle rádoby hlídkař za špínu? Tak to byste mě měli konečně pustit, jinak si to někdo odskáče!", "angry")
            else:
                $ kaspar.say("Tak už jste konečně pochopili, co je tahle rádoby hlídkařka za špínu? Tak to byste mě měli konečně pustit, jinak si to někdo odskáče!", "angry")
        if njal in cells:
            $ njal.say("Co je tohle za hry? Jsem připravený na soud. Nic špatného jsem neudělal. Kdy to konečně budu moct vysvětlit?", "angry")
    elif eckhard in cells or son in cells or gerd in cells:
        if gerd in cells:
            $ gerd.say("Myslím, že jste něco nepochopili, teď neměl jít další člověk dovnitř, ale jeden člověk ven, a to já. Jestli si zatknete celou hlídku, kdo nás potom všechny zase pustí?", "surprised")
        if eckhard in cells:
            $ eckhard.say("Já myslel, že hlídkaři zatýkají ostatní, ne že končí sami v celách… Komu teď mám vysvětlit, že za nic nemůžu?", "surprised")
        if son in cells:
            $ son.say("Nebude tohle znamenat, že se všechno ještě zdrží, že ne? Já už odtud chci vypadnout, ať už jakkoli.", "sad")
    return
