label prepareInterludes:
    $ eventsList = []
    $ eventsList.append(Event(Calendar(0, 16), "hayfaRecruiting", 2))
    $ eventsList.append(Event(Calendar(0, 18), "supperInvitation", 2))
    return

label supperInvitation:
    return

label interludeController:
    if time.hours > 20:
        call endOfDay
        return

    python:
        eventsList.sort(key=lambda x: x.priority, reverse=False)
        for item in eventsList:
            if item.when.isBefore(time):
                if item.code == "STATUS":
                    status.append(item.status)
                    if item.status + " added" in status:
                        status.remove(item.status + " added")
                    if item.checkAfter > 0:
                        item.code = "CHECK"
                        item.when.addHours(item.checkAfter)
                        item.checkAfter = 0
                    else:
                        eventsList.remove(item)
                elif item.code == "CHECK":
                    if item.status in status:
                        if item.checkReason == "complaint":
                            newEvent = Event(copy.deepcopy(time), "visitGuardhouseReminder", 1, "", 0, "complaint")
                        elif item.checkReason == "info":
                            newEvent = Event(copy.deepcopy(time), "visitGuardhouseReminder", 1, "", 0, "info")
                        eventsList.append(newEvent)
                        eventsList.remove(item)
                else:
                    if item.checkReason != "":
                        visitGuardhouseReminder = item.checkReason
                    calling = item.code
                    eventsList.remove(item)
                    renpy.call(calling)
                    break
    return

label preludeController:
    if currentLocation != "cells":
        $ evidenceWallCount += 1
        if evidenceWallCount == 3:
            call hayfaMentoring
    return
