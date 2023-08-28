label libraryIntro:
    if "library visited" not in status:
        if origin == "born here":
            "Marendarskou knihovnu si pamatuješ z dětství. Bývala to elegantní budova s vysokými policemi a studovnou, kde se dalo ztratit na dlouhé hodiny - nebo aspoň na tak dlouho, než tě někdo vyhnal zase ven."
            "Pamatuješ si na všeprostupující vůni papíru a kožených desek, pocit tepla a bezpečí, a především na laskavého knihovníka, který v tobě podporoval sny o lepším životě."
            if gender == "M":
                "Tehdy jsi byl přesvědčený, že se tam dá najít snad každá kniha na světě. A přestože stará knihovna nepřežila požár, který před dvěma lety město změnil téměř k nepoznání, určitě tu musela zbýt aspoň část jejího kouzla."
                "Dnes knihovna dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito a i přes provizorní umístění je očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal, ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu zase celý den."
            else:
                "Tehdy jsi byla přesvědčená, že se tam dá najít snad každá kniha na světě. A přestože stará knihovna nepřežila požár, který před dvěma lety město změnil téměř k nepoznání, určitě tu musela zbýt aspoň část jejího kouzla."
                scene bg library
                "Dnes knihovna dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito a i přes provizorní umístění je očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufala, ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu zase celý den."
        else:
            "Marendar míval krásnou knihovnu s mnoha svazky, ale ta bohužel padla za oběť ničivému požáru města před dvěma lety. Na její obnovu v plné slávě se stále hledají prostředky a mnohem menší sbírka dnes dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito."
            scene bg library
            if gender == "M":
                "I přes provizorní umístění je knihovna očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal, ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu celý den."
            else:
                "I přes provizorní umístění je knihovna očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufala, ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu celý den."
        $ status.append("library visited")
    else:
        "TBD: knihovna znovu"
    return

label stealPoetry:
    call libraryIntro
    if gender == "M":
        "Dnes jsi ale přišel za konkrétním účelem a po chvilce se zastavíš u regálu s poezií."
        scene bg books
        "Po chvíli hledání vezmeš do ruky útlou knihu básní. Se jménem autora ses ještě nesetkal, ale většina básní uvnitř mluví o citech nebo pracuje s přírodními motivy. Opíšeš si náhodnou z nich a doufáš, že na Zairise udělá dostatečně dobrý dojem."
    else:
        "Dnes jsi ale přišla za konkrétním účelem a po chvilce se zastavíš u regálu s poezií."
        "Po chvíli hledání vezmeš do ruky útlou knihu básní. Se jménem autora ses ještě nesetkala, ale většina básní uvnitř mluví o citech nebo pracuje s přírodními motivy. Opíšeš si náhodnou z nich a doufáš, že na Zairise udělá dostatečně dobrý dojem."
    show expression ("stolen poem [race].png") at truecenter
    pause
    hide expression ("stolen poem [race].png") at truecenter
    return
