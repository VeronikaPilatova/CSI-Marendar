label cellsController:
    play music audio.cells fadeout 0.5 if_changed
    scene bg cells entrance
    $ currentLocation = "cells"
    if "cells visited" not in status:
        call cellsFirst
        $ status.append("cells visited")
    elif cells and "arrest in progress" not in status:
        call cellsAgain
    if not cells:
        call cellsEmpty
        call leavingCells
        stop music
        return

    # choose prisoner to visit, load controller and call it
    if chosenChar == "":
        menu:
            "Promluvit si se Zeranem" if zeran in cells:
                $ chosenChar = "zeran"
            "Promluvit si s Kasparem" if kaspar in cells:
                $ chosenChar = "kaspar"
            "Promluvit si s Eckhardem" if eckhard in cells:
                $ chosenChar = "eckhard"
            "Promluvit si s Rumelinem" if rumelin in cells:
                $ chosenChar = "rumelin"
            "Promluvit si s Erle" if erle in cells:
                $ chosenChar = "erle"
            "Promluvit si s Aachimem" if son in cells:
                $ chosenChar = "son"
            "Promluvit si s mistrem Njalem" if njal in cells:
                $ chosenChar = "njal"
            "Promluvit si s Gerdem" if gerd in cells:
                $ chosenChar = "gerd"
            "Vrátit se zpět":
                call leavingCells
                return
    scene bg cell
    call expression chosenChar + "Notes"
    call expression chosenLocation
    $ chosenChar = ""

    call leavingCells
    stop music
    return

label cellsFirst:
    "Za Velinovy vlády prý cely bývaly plné jeho odpůrců nebo prostě jen lidí, kteří si dovolili stěžovat na nerovnost v zákonech pro lidi a pro ostatní."
    "Od té doby se vláda ve městě už dvakrát změnila a z dlouhé řady cel teď většina zůstává prázdná, mříže ale mají panty i zámky pečlivě vyčištěné ode rzi a jsou připravené na jediné otočení klíčem zapadnout za dalšími nešťastníky."
    "To spojení prázdnoty a připravenosti působí hrozivě, jako by se hlídka stále rozhodovala, jak se svým obávaným vězením naložit nebo proti komu ho namířit."
    return

label cellsAgain:
    "Znovu sejdeš do sklepa pod strážnicí. Z dlouhé řady cel teď většinu obývají jen krysy a pavouci, a tak snadno najdeš tu správnou."
    return

label cellsEmpty:
    "Pomalu projdeš podél řady cel až na konec chodby. Tvé kroky se rozléhají tichem a lampa, kterou neseš v ruce, kreslí na zdi stíny mříží."
    "V jedné z cel spatříš několik pytlů, další je naplněná nejrůznějším harampádím - v mihotavém světle si všimneš beden a stolu s chybějící nohou. Ve většině z nich však na tvůj pohled čeká jen prázdný kavalec a o to víc může tvá představivost vyvolávat obrazy těch všech, kteří zde našli svůj osud - a o to víc můžeš přemýšlet, jaký osud teď čeká cely samotné."
    return

label leavingCells:
    "Vyjdeš ze studeného sklepa zpět na světlo s pocitem úlevy, že jsi toto místo nikdy nemusel[a] poznat z té druhé strany."
    return
