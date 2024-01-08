label racismEncounter:
    $ racist.say("Kde si tady můžu stěžovat?", "angry")
    "Otočíš se za hlasem a spatříš menšího chlapíka v drahých barevných šatech, který si to rázuje k Rauvinovu stolu."
    $ racist.say("Právě mě okradli u brány! Chci okamžitou nápravu!", "angry")
    "Rauvin muži vyjde naproti a oba se zastaví přibližně uprostřed místnosti."
    $ rauvin.say("Pokud vás okradli, tak to samozřejmě vyšetříme. Co přesně se vám stalo?")
    $ racist.say("Tady to všechno máte sepsané. Naprostá nehoráznost! Co s tím uděláte?", "angry")
    "Rauvin si od druhého muže vezme list papíru a prostuduje ho."
    $ rauvin.say("To je potvrzení o zaplacení cla a vypadá v pořádku. Samozřejmě, pokud...")
    $ racist.say("Vám tohle přijde v pořádku? Vidíte tu částku? Vždyť to je zlodějina!", "angry")
    $ rauvin.say("Ano, takové clo je tu vyměřené.")
    "Muž v barevném oblečení se zamračí a udělá krok blíž k Rauvinovi. Ten zůstane stát na místě."
    $ racist.say("Možná pro lidi. Elfové ho budou mít tak poloviční.")
    # změna hudby
    "Na strážnici se náhle rozhostí napjaté ticho a všechny pohledy se stočí k obchodníkovi."
    $ rauvin.say("Clo je tu pro všechny stejně vysoké.")
    $ racist.say("Tomu tak věřím. Ten elfí parchant se na mně nakapsoval a vy ho teď kryjete. Máte z nich plné kalhoty, všichni lidi v hlídce.", "angry")
    $ rauvin.say("Nevím, co jste nepochopil. Elfové i lidi platí stejné clo a je to přesně tolik, co jste platil vy. Nikdo vás neokradl ani nepodvedl. Jestli se vám naše cla nelíbí, jeďte příště jinam.")
    $ racist.say("Nesmysly! Ale já to všem povím. Jak se nic nezměnilo. Jak se možná tváříte, kolik je v hlídce lidí, ale jak se třesete, aby si vás velitel nepodal. Jak...", "angry")
    $ rauvin.say("Můžu vám zařídit přijetí u Jeho Jasnosti barona.")
    $ racist.say("No to byste měl! Já mu to vyložím!")
    $ rauvin.say("Můžu vám zaručit, že ten to vezme naprosto vážně a že umí soudit velmi přísně.")
    $ racist.say("No to doufám. I když na můj vkus byl na povstalce až moc měkký. Doufám, že tady bude ráznější.", "happy")
    $ rauvin.say("Je velmi rázný. Obzvlášť u křivých obvinění. A ještě víc u křivých obvinění z útlaku jen kvůli tomu, jaké je kdo rasy.")
    $ rauvin.say("Jaký trest si myslíte, že by mohl za něco takového udělit?")
    $ racist.say("To… nevím? Ale… proč mluvíme o křivých obviněních, přece víte, jak to tu chodí.", "surprised")
    $ rauvin.say("Vím to velmi dobře. Sporů mezi lidmi a elfy už tu bylo dost a on je ve svém městě nestrpí. Nikdo z nás tu nestrpí jakékoli takové činy a jakákoli křivá obvinění z nich.")
    $ rauvin.say("Jestli trváte na svém obvinění, napíšu hned Jeho Jasnosti. Je hodně zaměstnaný na vévodském dvoře, ale kvůli tomuto přijede. Důkladně prověří celou hlídku a i vaše svědectví proti ní.")
    $ rauvin.say("A potom bude soudit. Přísně a rázně, jak jste doufal. Tak, aby dal příklad všem ostatním.")
    $ rauvin.say("Trváte na svém obvinění?")
    $ racist.say("No… možná přeci jen Jeho Jasnost barona nemusíme obtěžovat… Máte pravdu, že je hodně zaměstnaný, mělo mi to dojít hned...")
    $ rauvin.say("Dobrá.")
    $ rauvin.say("Pokud se někdy stanete obětí skutečného zločinu, prosím, obraťte se na nás, pokusíme se zjednat nápravu. To je poslání současné hlídky.")
    $ rauvin.say("Nyní už bych vás nerad zdržoval. Věřím, že se potřebujete věnovat svým obchodům.")
    "Obchodník se krátce rozhlédne a velmi rychle se ze strážnice vytratí. Hlídkaři v místnosti mlčky sledují pohledem nejdřív jeho a poté zavřené dveře, jež za ním zapadnou. Trvá několik dlouhých okamžiků, než první odvážlivec prolomí mlčení a ruch v místnosti se postupně obnoví."
    $ status.append("racism encounter")
    return

label kilianEncounter:
    $ kilian.rename("Kilian")
    "V místnosti téměř nikdo není, jen Hayfa právě něco probírá s Rauvinem a jeden z hlídkařů u stolu sepisuje cosi o clech."
    "Zvenčí se ozve nesmělé zaklepání na dveře, tak slabé, že možná šlo jen o klam. Hayfa jde přesto okamžitě otevřít a venku skutečně nalezne asi dvanáctiletého kluka."
    $ hayfa.say("Vítej na strážnici městské hlídky Marendaru. Jsem Hayfa. S čím můžeme pomoct?")
    "Kluk při pohledu na ni ucukne o krok a kousne se do rtu. Pak se nadechne."
    $ kilian.say("Dobrý den. Já… můžu prosím mluvit s panem velitelem?", "surprised")
    $ hayfa.say("Velitel je zaneprázdněný, ale cokoli můžeš řešit rovnou se mnou. Když to bude potřeba, tak mu to předám.")
    $ kilian.say("Ale… a můžu aspoň dovnitř?", "sad")
    "Hayfa ustoupí ze dveří, pokyne mu hlavou a kluk vstoupí do místnosti. Nejistě se rozhlédne a udělá několik kroků směrem k Rauvinovi, ale přímo ho neosloví."
    $ kilian.say("Já... včera se stala taková nehoda. Nedorozumění. Všechno jsme dělali bezpečně, ale někoho to asi vylekalo a...")
    $ hayfa.say("Co kdybys začal od začátku? Jak se jmenuješ? Z které jsi čtvrti?")
    $ kilian.say("Jsem Kilian. Přišli jsme do města na slavnosti, naše stará… tam, kde jsme bydleli předtím, už být nemůžeme. Já a moje sestra. Potřebovali jsme peníze, a tak začala tančit a všem se to moc líbilo a házeli nám mince do čepice.")
    $ hayfa.say("A potom jste se pokusili zapálit město?", "angry")
    $ kilian.say("Ne! Nikdy jsme nic nezapálili!", "surprised")
    $ hayfa.say("Kromě toho vozu, chceš říct.", "angry")
    $ kilian.say("To bylo to nedorozumění! Už jsme takhle byli v jiných městech a nikdy nic nechytlo!", "surprised")
    $ hayfa.say("Tady jsme v Marendaru, shořel vůz a spousta lidí musela hasit.", "angry")
    $ kilian.say("Ale...", "sad")
    "Kluk vrhne prosebný pohled na Rauvina."
    $ rauvin.say("Nošení otevřeného ohně na ulici je v Marendaru zakázané.")
    $ hayfa.say("A žháře tu nikdo nestrpí.", "angry")
    $ kilian.say("To přece nebylo... my jsme jen chtěli potěšit publikum, my jsme nevěděli, že vám oheň tak vadí.", "surprised")
    $ rauvin.say("Jsem si jistý, že to městská rada zohlední.")
    $ rauvin.say("Ale pořád ještě jsi nepřednesl svou žádost nebo stížnost.")
    $ kilian.say("Já... nemůžete nás nechat prostě vypadnout z tohohle města a celého vévodství a už nikdy se nevracet?", "sad")
    $ hayfa.say("To má být vtip?", "angry")
    $ rauvin.say("Obvinění ze žhářství je příliš závažné a musí ho projednat soud, nejspíš ještě před začátkem slavností. Po něm a po provedení případného trestu samozřejmě budete volní.")
    $ kilian.say("Ale...", "sad")
    "Kluk nedopoví, otočí se na místě a vyběhne ven ze strážnice. Hlídkaři ho sledují, dokud se neztratí za nejbližším rohem."
    $ rauvin.say("Zvláštní. Čekal jsem, že ji aspoň bude chtít vidět, když jí hrozí poprava.")
    "Hayfa jen pokrčí rameny a dojde zavřít dveře."
    show mcPic at menuImage
    menu:
        "Poprava? Za tanec s ohněm?":
            hide mcPic
            $ hayfa.say("Co jiného bys dělal[a] se žhářkou?", "angry")
            $ mc.say("Většina komediantů nic podpalovat nechce. Většina z nich jenom předvádí čísla, která vypadají dobře. Kdyby chtěla založit požár, nebude to dělat před obecenstvem.")
            $ hayfa.say("Chtít mohla cokoli, ale ten požár opravdu málem způsobila.", "angry")
            $ rauvin.say("Po tom velkém požáru před dvěma lety jsou tady hodně přísné zákony kolem neopatrného nošení otevřeného ohně. Bojím se, že její představení pod to spadá.")
        "Otravují vás takhle zločinci často?":
            hide mcPic
            $ rauvin.trust -= 1
            $ hayfa.say("Většinou nemají tu drzost.", "angry")
            $ rauvin.say("Ještě o něm přece nevíme, jestli je zločinec. Ani o jeho sestře.")
            $ hayfa.say("Děláš si legraci?", "surprised")
            $ rauvin.say("Vůbec. On ani není z ničeho obviněný a o té komediantce teprve soud posoudí, jestli měla špatné úmysly, nebo jestli je opravdu jenom zdaleka a nic o Marendaru neví.")
            $ rauvin.say("A na tom, že se někdo přijde zeptat na příbuzného, není nic špatného a občas se to děje.")
            $ hayfa.say("... já vím, nemluvit zbytečně o požáru, protože se jinak pohádáme. Ale občas mě štveš.", "angry")
        "Nebyli jste na něj příliš tvrdí?":
            hide mcPic
            $ rauvin.say("Myslíš? Proč?")
            $ mc.say("Vždyť už na začátku byl hrozně vyděšený a teď musí být úplně zoufalý.")
            $ rauvin.say("Řekl jsem mu přece, že jeho důvody soud zohlední.")
            $ hayfa.say("A žháři si tvrdost zaslouží.", "angry")
            $ mc.say("Ale my ještě nevíme, jestli on nebo jeho sestra jsou žháři. Od toho přece bude ten soud.")
            $ mc.say("Ale tohle znělo, že soud bude sloužit jen jako veřejný spektákl, kde si na té holce všichni vylijí zlost.")
            $ rauvin.say("To jsem přece neřekl... vážně ti přijde, že to tak mohl pochopit?")
            $ mc.say("Jinak o tom nezačínám.")
            $ hayfa.say("Nechceme se radši vrátit k práci? Už jsme kvůli té holce ztratili času až moc.")
        "{i}(Neříct nic){/i}":
            hide mcPic
    $ status.append("Killian encounter")
    return

label hayfasPastEncounter:
    "Rauvin je právě zabraný do hovoru s jakousi dobře oblečenou ženou, kterou neznáš. Zatímco tvůj velitel se snaží působit klidně, jeho společnice ho probodává pohledem a mírně zvyšuje hlas."
    "Jiní hlídkaři se alespoň zdánlivě věnují své práci a do rozhovoru nezasahují, neujde ti ale, že většina z nich dobře poslouchá."
    $ rauvin.say("“Jak říkám, takové rozhodnutí je plně v kompetenci každého člena hlídky a Hayfa jím své pravomoce nijak nepřekročila.")
    $ angryWoman.say("Vy mě pořád nechápete. Když něco rozhodnete vy nebo kdokoli v téhle místnosti, tak dobře. Ale jak něco podobného můžete dovolit zrovna jí?", "angry")
    $ rauvin.say("Je to členka hlídky stejně jako všichni ostatní.")
    $ angryWoman.say("Není! Nikdo z vás ostatních se nepokusil zabít purkmistra!", "angry")
    $ rauvin.say("Za to byla souzená a potrestaná.")
    $ angryWoman.say("Potrestaná? Vždyť vyvázla s tím, že jen pár měsíců opravovala škody po požáru, a teď je najednou zřejmě skoro nejdůležitější v celé hlídce. Copak je tohle trest?", "surprised")
    $ rauvin.say("Pracovat bez nároku na odměnu vám připadá málo?")
    $ angryWoman.say("Kdyby zůstala u stavění domů, budiž. Ale pustit ji do hlídky?", "angry")
    $ angryWoman.say("Nezapomínejte, že přivandrovala kdo ví odkud a uctívá nějakého pochybného boha. Nikdo z nás nemůže tušit, co dalšího ještě plánuje.", "angry")
    $ rauvin.say("Naše zákony vstup do hlídky nikomu nezakazují a Hayfa mnohokrát prokázala jak schopnosti, tak lásku k městu.")
    $ angryWoman.say("A co vaše soudnost, ta vám nic neříká? Co když to všechno jen hraje? Vždyť tu je tak krátce, že ani nezažila požár, co ona o městě ví, aby ho mohla opravdu tak milovat?", "angry")
    $ rauvin.say("Zřejmě dost na to, aby pro hlídku byla neocenitelná.")
    $ rauvin.say("Podívejte, rozhodnutí soudu ani jeden z nás nemůže zvrátit. Hayfina služba městu teď je příkladná. A snad vás může ubezpečit, že vzhledem k její minulosti je vyloučené, aby v hlídce získala výrazně vyšší postavení, než má teď.")
    $ rauvin.say("Nicméně aby mohla městu co nejlépe sloužit, potřebuji pomoc i od vás.")
    $ rauvin.say("Jestli se začne podezřele, potřebuji to hned vědět. A dokud dělá přesně to, co se od hlídkařů očekává, potřebuji naopak, abyste to od ní přijímala stejně jako od libovolného jiného hlídkaře.")
    $ angryWoman.say("... já jen doufám, že neděláte chybu, které budeme všichni litovat.", "sad")
    $ rauvin.say("“Já věřím tomu, že kdyby měla opravdu nekalé úmysly, odešla by do města, kde ji nikdo nezná, a nezůstala by tady, kde už byla souzená a kde všichni znají její tvář.")
    $ rauvin.say("Je tu ještě něco, s čím vám může hlídka pomoci?")
    "Žena si povzdychne."
    $ angryWoman.say("... asi ne. Budu spoléhat na váš úsudek. Ostatně město vám věří, že hlídku dokážete vést správně. Snad víte, co děláte.")
    "S tím se žena rozloučí a vyjde ven ze strážnice. Rauvin jí otevře dveře a chvíli za ní hledí."
    "Když se otočí zpět do místnosti, zůstává na jeho tváři stále stopa zmatení a možná únavy, kterou ale brzy opět vystřídá věcná přímost, na kterou jste od něj zvyklí."
    $ rauvin.say("Kde jsme to byli. Jak pokračujete se svojí prací? Objevilo se mezitím něco, co se mnou někdo potřebujete probrat?")
    $ globalClues.append("hayfa's past")
    $ globalClues.append("Hayfa's arrival to Marendar")
    $ status.append("Hayfa's past encounter")
    return
