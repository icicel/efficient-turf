
# INSTÄLLNINGAR

# debug
debugunusedpaths = True # visar vilka förbindelser som inte använts av en finished path
debugcentralzones = False # visar vilka zoner som är mest och minst centralt belägna
debugshowpoints = True # visar zonernas poäng
debugshowartipoints = False # visar articulation points
debugrandompath = True # visar en slumpmässig pågående rutt efter varje steg i processen
debugzonedata = False # visar information om zonerna i excelformat

# start- och slutzon
start = "k-klassrum"
end = "k-gymnasiet"

# vilken algoritm (annealing, tabu, bruteforce, quickbrute)
algorithm = "quickbrute"

# inställningar för annealing
temperature = 100_000
iterations = 3
# inställningar för tabu
tabusize = 20
tabuiterations = 100_000

# zoner du inte kan eller vill ta
blacklist = []
# om ovan istället är en lista på de enda zoner du kan eller vill ta
whitelist = False

# turfhastighet i m/min
speed = 64

# turf-användarnamn
username = "icicle"

# namn på backupfil
dumpname = "turf"

# lista på zoner
zlist = ["campingpiren", "surfview", "nösnäsån", "gulzon", "bathview", "nösnäsbacken", "hallernazon", "kozon",
         "genomskogen", "sneezenose", "dragkamp", "inklämdpågräs", "solgårdsstig", "husarrondell", "movedwindmill",
         "kvarnskogen", "stenryttare", "kvarntäppan", "trädväg", "liteskogbara", "hasselbacke", "frispel", "tullaull",
         "yttreucklums", "ucklumcykel", "kringelikrok", "norumskyrka", "jansvy", "bakomängen", "torpzone", "sköntgrönt",
         "motfurufjäll", "gamlahallerna", "odlamedcykel"]
# komplett? lista på zoner
thezlist = ["campingpiren", "surfview", "nösnäsån", "gulzon", "bathview", "nösnäsbacken", "hallernazon", "kozon",
         "genomskogen", "sneezenose", "dragkamp", "inklämdpågräs", "solgårdsstig", "husarrondell", "movedwindmill",
         "kvarnskogen", "stenryttare", "kvarntäppan", "trädväg", "liteskogbara", "hasselbacke", "frispel", "tullaull",
         "yttreucklums", "ucklumcykel", "kringelikrok", "norumskyrka", "jansvy", "bakomängen", "torpzone", "sköntgrönt",
         "motfurufjäll", "gamlahallerna", "odlamedcykel", "lillaaskerön", "storaaskerön", "skåpesundsbro", "varekil",
         "stenungsbaden", "owenbeach", "denandrasidan", "källöudde", "källöhöjden", "tjörnbron", "monsterbridge",
         "almöbryggan", "paternoster", "myggebadet", "vågigbro", "almölivs", "myggeview", "tjörnbjörn", "stonerail",
         "kil", "busview", "räddaenbåt", "flagganitopp", "ungstenssund", "chapelzone", "rosecorner", "kajpromenad",
         "culturalpark", "stenungepiren", "rockyoungbath"]

# lista på korsningszoner
klist = ["k-klassrum", "k-nösnäs", "k-gymnasiet", "k-backen", "k-ucklum", "k-hallerna", "k-solgård", "k-kristinedal",
         "k-camping", "k-kvarnberg", "k-skogsbryn", "k-älvhem", "k-strandnorum", "k-tuvull", "k-kyrkenorum"]

# articulation points som håller samman tre+ block
arti3points = ["nösnäsån", "k-camping"]

# förbindelser mellan zoner i formatet ["zon1", "zon2", (längd i meter)]
connections = [
    ["campingpiren", "k-camping", 370],
    ["surfview", "k-camping", 280],
    ["k-camping", "nösnäsån", 730],
    ["nösnäsån", "gulzon", 370],
    ["gulzon", "bathview", 480],
    ["nösnäsån", "k-nösnäs", 100],
    ["k-nösnäs", "nösnäsbacken", 580],
    ["nösnäsbacken", "hallernazon", 620],
    ["hallernazon", "k-hallerna", 530],
    ["k-hallerna", "kozon", 330],
    ["k-hallerna", "genomskogen", 330],
    ["k-backen", "genomskogen", 330],
    ["genomskogen", "sneezenose", 540],
    ["sneezenose", "nösnäsbacken", 540],
    ["sneezenose", "k-gymnasiet", 80],
    ["k-nösnäs", "k-gymnasiet", 430],
    ["k-gymnasiet", "k-klassrum", 130],
    ["k-klassrum", "k-backen", 120],
    ["k-ucklum", "k-gymnasiet", 260],
    ["k-nösnäs", "k-solgård", 330],
    ["k-solgård", "dragkamp", 90],
    ["k-solgård", "inklämdpågräs", 230],
    ["inklämdpågräs", "solgårdsstig", 310],
    ["solgårdsstig", "k-kristinedal", 520],
    ["k-kristinedal", "husarrondell", 150],
    ["k-kristinedal", "stenryttare", 210],
    ["inklämdpågräs", "movedwindmill", 450],
    ["movedwindmill", "k-kvarnberg", 410],
    ["k-kvarnberg", "k-skogsbryn", 200],
    ["k-skogsbryn", "kvarnskogen", 200],
    ["k-skogsbryn", "stenryttare", 150],
    ["k-skogsbryn", "liteskogbara", 290],
    ["k-kvarnberg", "kvarntäppan", 230],
    ["k-kvarnberg", "liteskogbara", 330],
    ["kvarntäppan", "k-ucklum", 280],
    ["k-ucklum", "dragkamp", 190],
    ["kvarntäppan", "trädväg", 330],
    ["k-ucklum", "trädväg", 470],
    ["trädväg", "liteskogbara", 550],
    ["liteskogbara", "hasselbacke", 440],
    ["trädväg", "hasselbacke", 470],
    ["trädväg", "k-älvhem", 280],
    ["k-älvhem", "hasselbacke", 320],
    ["hasselbacke", "frispel", 260],
    ["k-älvhem", "frispel", 430],
    ["frispel", "tullaull", 260],
    ["k-älvhem", "yttreucklums", 330],
    ["yttreucklums", "ucklumcykel", 450],
    ["yttreucklums", "k-backen", 310],
    ["kringelikrok", "ucklumcykel", 630],
    ["kringelikrok", "norumskyrka", 450],
    ["norumskyrka", "kozon", 710],
    ["yttreucklums", "k-ucklum", 550],
    ["nösnäsbacken", "k-strandnorum", 540],
    ["hallernazon", "k-strandnorum", 330],
    ["k-strandnorum", "jansvy", 390],
    ["k-strandnorum", "bakomängen", 420],
    ["jansvy", "bakomängen", 390],
    ["tullaull", "k-tuvull", 230],
    ["k-tuvull", "kringelikrok", 310],
    ["k-tuvull", "torpzone", 530],
    ["kringelikrok", "k-kyrkenorum", 270],
    ["k-kyrkenorum", "torpzone", 410],
    ["k-kyrkenorum", "sköntgrönt", 360],
    ["norumskyrka", "sköntgrönt", 620],
    ["sköntgrönt", "motfurufjäll", 360],
    ["kozon", "gamlahallerna", 590],
    ["gamlahallerna", "norumskyrka", 670],
    ["gamlahallerna", "odlamedcykel", 250]
]



# här nere börjar själva ruttgenereringsprocessen
import time, requests, datetime, pickle#rick
if debugrandompath == True:
    import random
maxdistance = 0
if debugzonedata == False:
    if algorithm == "bruteforce":
        maxdistance = speed * int(input("Tid i minuter (max 120):\n> "))
    else:
        maxdistance = speed * int(input("Tid i minuter:\n> "))
timeatstart = time.time()
roundhoursleft = 0
hasconnection = True
hasbackup = True
backupold = False
backupbad = False

def datetimer(deta): # väldigt lång rad, vill inte skriva den fem gånger
    return datetime.datetime(int(deta[0].split("-")[0]),int(deta[0].split("-")[1]),int(deta[0].split("-")[2]),int(deta[1].split(":")[0]),int(deta[1].split(":")[1]),int(deta[1].split(":")[2])).timestamp()
# rund-info
try:
    rounds = requests.get("http://api.turfgame.com/v4/rounds").json()
    #print(rounds)
    date = str(rounds[-2]["start"])[:-5].split("T") # rounds[-2] är alltid nästa runda (tror jag)
    roundhoursleft = (datetimer(date) - time.time()) / 3600
except requests.exceptions.ConnectionError: # get wifi anywhere you go
    hasconnection = False

try:
    with open(dumpname + ".pk", "rb") as file:
        d = pickle.load(file)
    if time.time() - d[1] >= 3600:
        backupold = True # om mer än en timme har gått sedan föregående request
    for zone in zlist:
        if zone not in d[0]:
            backupbad = True # om inte alla zoner finns i backup
except FileNotFoundError:
    hasbackup = False

if debugzonedata == True:
    print("name\tage\tpotential\tpts on take\tpts per hour\tpts total\ttake age\trevisit pts\tneutral pts")
    for zone in thezlist:
        t = []
        while True:  # går man över en request i sekunden ger api:n garbage istället
            try:
                z = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                break
            except KeyError:
                pass
        cdate = str(z["dateCreated"])[:-5].split("T")
        hoursexisted = (time.time() - datetimer(cdate)) / 3600
        potentialhours = min(hoursexisted / z["totalTakeovers"], roundhoursleft)  # antal timmar innan zonen förloras
        t.append(int(hoursexisted / 24))
        t.append(round(potentialhours / 24, 1))
        t.append(int(z["takeoverPoints"]))
        t.append(int(z["pointsPerHour"]))
        t.append(int(z["takeoverPoints"] + potentialhours * z["pointsPerHour"]))

        try:
            if z["currentOwner"]["name"] == username:  # currentOwner är en själv - revisit-poäng om för över 23 timmar sedan
                tdate = str(z["dateLastTaken"])[:-5].split("T")
                hourssincetaken = (time.time() - datetimer(tdate)) / 3600
                t.append(int(hourssincetaken / 24))
                if hourssincetaken >= 23:
                    t.append(int(z["takeoverPoints"] / 2))
                else:
                    t.append(0)
            else:
                t.append("")
                t.append("")
            t.append("")
        except KeyError:  # ingen currentOwner - blir neutralbonus istället
            t.append("")
            t.append("")
            t.append(50)
        tt = zone
        for a in t:
            tt += "\t" + str(a).replace(".", ",")
        print(tt)
    quit()

zonepoints = {}
z = {}
if hasconnection == True:
    if backupold == False and backupbad == False and hasbackup == True:
        print("Laddar backupfil")
        with open(dumpname + ".pk", "rb") as file:
            d = pickle.load(file)
        zonepoints = d[0]
        for zone in klist:
            zonepoints[zone] = 0
    else:
        if backupold == True:
            print("Backupfil för gammal")
        elif backupbad == True:
            print("Ingen giltig backupfil hittad")
        else:
            print("Ingen backupfil hittad")
        for zone in zlist:
            print("Skickar efter data... (" + str(zlist.index(zone) + 1) + "/" + str(len(zlist)) + ")")
            if (whitelist == False and zone not in blacklist) or (whitelist == True and zone in blacklist):
                while True:  # går man över en request i sekunden ger api:n garbage istället
                    try:
                        z = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                        break
                    except KeyError:
                        pass
                cdate = str(z["dateCreated"])[:-5].split("T")
                hoursexisted = (time.time() - datetimer(cdate)) / 3600
                potentialhours = min(hoursexisted / z["totalTakeovers"], roundhoursleft)  # antal timmar innan zonen förloras
                zonepoints[zone] = int(z["takeoverPoints"] + potentialhours * z["pointsPerHour"])

                try:
                    if z["currentOwner"]["name"] == username:  # currentOwner är en själv - revisit-poäng om för över 23 timmar sedan
                        tdate = str(z["dateLastTaken"])[:-5].split("T")
                        hourssincetaken = (time.time() - datetimer(tdate)) / 3600
                        if hourssincetaken >= 23:
                            zonepoints[zone] = int(z["takeoverPoints"] / 2)
                        else:
                            zonepoints[zone] = 0
                except KeyError:  # ingen currentOwner - blir neutralbonus istället
                    zonepoints[zone] += 50
            else:
                zonepoints[zone] = 0
        for zone in klist:  # korsningar är ju inte zoner
            zonepoints[zone] = 0
        with open(dumpname + ".pk", "wb") as file:
            pickle.dump([zonepoints, time.time()], file)
else:
    if hasbackup == True:
        if backupbad == False:
            if backupold == False:
                print("Ingen anslutning, laddar backupfil")
                with open(dumpname + ".pk", "rb") as file:
                    d = pickle.load(file)
                zonepoints = d[0]
                for zone in klist:
                    zonepoints[zone] = 0
            else:
                print("Ingen anslutning, laddar gammal backupfil")
                with open(dumpname + ".pk", "rb") as file:
                    d = pickle.load(file)
                zonepoints = d[0]
                for zone in klist:
                    zonepoints[zone] = 0
        else:
            print("Ingen anslutning, laddar ogiltig backupfil")
            with open(dumpname + ".pk", "rb") as file:
                d = pickle.load(file)
            zonepoints = d[0]
            for zone in klist:
                zonepoints[zone] = 0
            for zone in zlist:
                if zone not in zonepoints:
                    zonepoints[zone] = 0
    else:
        quit(print("Ingen anslutning, ingen backupfil hittad"))

zones = {}
for zone in zonepoints:
    zones[zone] = []
for con in connections:
    zones[con[0]].append([con[1], con[2]])
    zones[con[1]].append([con[0], con[2]])
# annorlunda startrutt om man startar på en poänggivande zon
paths = [[0, 0, 1, 0, start]] if zonepoints[start] == 0 else [[0, zonepoints[start], 1, 0, start]]

# räknar ut den snabbaste rutten från varje zon till varje annan zon
zonedistance = {}
zonepathfromto = {}
endpaths = []
for endzone in zonepoints:
    if zonepoints[endzone] != 0 or endzone == start or endzone == end:
        endzonedistance = {endzone: 0}
        endzonepathto = {endzone: [endzone]}
        for connection in zones[endzone]:
            endpaths.append([connection[1], connection[0]])
        while True: # för varje loop, väljer den kortaste rutten och förlänger den
            endpaths.sort(key = lambda x:x[0])
            endpath = endpaths[0]
            if endpath[-1] not in endzonedistance:
                endzonepathto[endpath[-1]] = [endzone] + endpath[1:]
                endzonedistance[endpath[-1]] = endpath[0]
                for connection in zones[endpath[-1]]:
                    if connection[0] not in endzonedistance:
                        endpaths.append([endpath[0] + connection[1]] + endpath[1:] + [connection[0]])
            endpaths.pop(0)
            if endpaths == []:
                break
        zonedistance[endzone] = endzonedistance
        zonepathfromto[endzone] = endzonepathto

# räknar ut alla articulation points, en.wikipedia.org/wiki/Biconnected_component
# haha, jag stal den
artipoints = []
visited = []
depth = {}
low = {}
parent = {}
def extend(zon, dept):
    visited.append(zon)
    depth[zon] = dept
    low[zon] = dept
    for connectio in zones[zon]:
        child = connectio[0]
        if not child in visited:
            parent[child] = zon
            extend(child, dept + 1)
            if low[child] >= depth[zon]:
                if zon != end:
                    artipoints.append(zon)
            low[zon] = min(low[zon], low[child])
        elif zon not in parent or child != parent[zon]:
            low[zon] = min(low[zon], depth[child])
extend(start, 0)
extend(end, 0) # extend med två olika zoner ifall en av dem är en articulation point
if artipoints.count(start) == 1: # startzonen räknar alltid sig själv av någon anledning
    artipoints.remove(start)
artipoints = list(dict.fromkeys(artipoints))
if debugshowartipoints == True:
    print(artipoints)

# debug-grejer
if debugcentralzones == True:
    tl = []
    for startzone in zonedistance:
        c = 0
        for endzone in zonedistance[startzone]:
            c += zonedistance[startzone][endzone]
        tl.append([c, startzone])
    tl.sort(key = lambda x:x[0])
    print("\nMest centrala zon: " + tl[0][1] + "\nMest isolerade zon: " + tl[-1][1] + "\n")
if debugshowpoints == True:
    print(dict(sorted(zonepoints.items(), key=lambda x: x[1], reverse=True)))
if maxdistance == 0: # ingen idé att ens påbörja loopen om detta är fallet
    quit()



# den stora genereringsloopen
print("\nUppstart tog " + str(round(time.time() - timeatstart, 2)) + " sekunder\n")
timeatstart = time.time()
if algorithm == "bruteforce" or algorithm == "quickbrute":
    # en rutt är uppbyggd som så: id: [sträcka, rutt-poäng, antal zoner sedan den senaste poänggivande, dessas sträcka, zoner...]
    finishedpaths = []
    largestnum = 0 # färdiga rutter accepteras bara om de har mer än den hittills bästa färdiga ruttens poäng
    cc = 1 # räknar loop-steg

    while True:
        toadd = []
        for path in paths:
            lastzone = path[-1]
            lastlastzone = path[-2]
            for connection in zones[lastzone]: # där connection har formatet [zon, avstånd]
                points = path[1]
                conseczones = path[2]
                consecdist = path[3]
                lastcapturedzone = path[-conseczones]
                newzone = connection[0]
                newdistance = connection[1]
                distance = path[0] + newdistance

                # nu följer: lite optimiseringar av "algoritmen"!
                # om dessa händelser inträffar finns det garanterat en annan, bättre rutt någonstans i processen, och rutten avbryts därför
                if maxdistance - distance < zonedistance[end][newzone]: # om den omöjligt kan avsluta rutten utan att överskrida tidsgränsen
                    continue
                if zonepoints[lastzone] == 0 or lastzone in path[:-1]:
                    if newzone == lastlastzone: # om den går till en ej poänggivande zon och sedan tillbaka
                        continue
                if newzone == lastcapturedzone: # om den gör en runda enbart på ej poänggivande zoner
                    continue
                if zonepoints[newzone] != 0 and newzone not in path:
                    if consecdist + newdistance > zonedistance[lastcapturedzone][newzone]: # om den inte tagit den snabbaste rutten till den nya zonen
                        continue
                if newzone in path and newzone != end:
                    if newzone in path[path.index(newzone) + 1:]: # om den varit på en zon tre gånger
                        if newzone not in arti3points:
                            continue
                    if path[5] != newzone or path.count(newzone) > 1: # om den inte återvänder till en zon via förbindelsen den lämnade zonen med (alltså, en loop)
                        if newzone not in artipoints:
                            reversepath = path[::-1]
                            if reversepath[reversepath.index(newzone) - 1] != lastzone:
                                continue
                if (lastzone, newzone) in list(zip(path[4:], path[5:])): # om den använder samma förbindelse åt samma håll två gånger
                    continue

                if zonepoints[newzone] != 0 and newzone not in path: # om zonen ger poäng
                    points += zonepoints[newzone]
                    conseczones = 1
                    consecdist = 0
                else: # om zonen inte gör det
                    conseczones += 1
                    consecdist += newdistance
                toadd.append([distance, points, conseczones, consecdist] + path[4:] + [newzone])
            if lastzone == end and path[1] >= largestnum:
                largestnum = path[1]
                finishedpaths.append(path)

        paths = [path for path in toadd]
        if paths == []: # om alla rutter är avslutade
            break
        if debugrandompath == True:
            print(random.choice(paths))

        # tar bort identiska rutter
        if algorithm == "quickbrutez":
            dupecheck = []
            todelete = []
            c = 0
            for path in paths:
                dupe = set(path[4:])
                if dupe in dupecheck:
                    todelete.append(c)
                else:
                    dupecheck.append(dupe)
                c += 1
            todelete.sort(reverse = True)
            for n in todelete:
                del paths[n]
        
        if algorithm == "quickbrutex":
            dupecheck = []
            dupechecki = []
            dupes = {}
            todelete = []
            c = 0
            for path in paths:
                dupe = set(path[4:])
                if dupe in dupecheck:
                    og = dupechecki[dupecheck.index(dupe)]
                    if og in dupes:
                        dupes[og].append(c)
                    else:
                        dupes[og] = [c]
                else:
                    dupecheck.append(dupe)
                    dupechecki.append(c)
                c += 1
            for n in dupes:
                alldupes = dupes[n] + [n]
                alldupes.remove(min(dupes[n] + [n], key=lambda x:paths[x][0]))
                todelete.extend(alldupes)
            todelete.sort(reverse = True)
            for n in todelete:
                del paths[n]

        print("Vid steg " + str(cc) + " finns " + str(len(paths)) + " pågående rutter och " + str(len(finishedpaths)) + " färdiga")
        cc += 1
    if len(finishedpaths) == 0:
        quit(print("\nInga möjliga rutter hittade"))

    # renskrivning av de färdiga rutterna
    finishedpaths.sort(key = lambda x:x[1], reverse = True)
    paths = []
    for path in finishedpaths:
        if path[1] >= finishedpaths[0][1] * 0.8:
            paths.append(path[:2]) # conseczones och consecdist tas bort
            for zone in path[4:]:
                paths[-1].append(zone)
        else:
            break

    if debugunusedpaths == True:
        pairs = []
        for path in paths:
            for pair in list(zip(path[2:], path[3:])):
                x = list(pair)
                x.sort()
                pairs.append(list(x))
        unuseds = []
        for zone in zonepoints:
            for connection in zones[zone]:
                pair = [zone, connection[0]]
                pair.sort()
                if pair not in pairs and pair not in unuseds:
                    unuseds.append(pair)
        unuseds.sort()
        print("\n" + str(unuseds))


    # kollar efter rutter som praktiskt sett är identiska
    dupecheck = []
    todelete = []
    c = 0
    for path in paths:
        dupe = path[2:]
        dupe.sort()
        if dupe in dupecheck:
            todelete.append(c)
        else:
            dupecheck.append(dupe)
        c += 1
    todelete.sort(reverse = True)
    for n in todelete:
        paths.pop(n)

    # en sista sortering
    paths.sort(key = lambda x:x[1], reverse = True)
    print("\nAlla rutter:")
    if len(paths) > 1: # skriver ut alla andra acceptabla rutter
        for path in paths:
            result = str(round(path[1], 1)) + " poäng, " + str(int(path[0] / speed)) + " min: "
            for zone in path[2:]:
                if zone[:2] != "k-":
                    result += zone.upper() + "-"
            print(result[:-1])
        print()

    # skriv ut resultatet
    print("Bästa rutt:")
    best = paths[0].copy()
    result = str(round(best[1], 1)) + " poäng, " + str(len(best[2:])) + " st, " + str(int(best[0] / speed)) + " min: "
    c = 2
    for zone in best[2:]:
        if zone[:2] != "k-" and zone not in best[2:c]:
            result += zone.upper() + "-"
        c += 1
    print(result[:-1] + "\n\n" + str(best) + "\n\nProcessen tog " + str(round(time.time() - timeatstart, 2)) + " sekunder")


elif algorithm == "annealing":
    path = [z for z in zonepathfromto[start][end] if z in zlist + [start, end]]  # only point-giving zones
    dist = 1
    if len(path) == 1:
        pts = zonepoints[path[0]]
        path *= 2
    else:
        pts = 1
        for n in range(0, len(path) - 1):  # first zone to next-to-last zone
            pts += zonepoints[path[n]]
            dist += zonedistance[path[n]][path[n + 1]]
        pts += zonepoints[path[-1]]

    def nrg(d, p):
        return (d * 1000) / (p * (d + 1000))  # energifunktion som värderar poäng mycket högre än avstånd

    for i in range(1, iterations + 1):
        print("Påbörjat iteration " + str(i) + "/" + str(iterations))
        newpath = []
        newdist = 0
        newpts = 0
        # mutationstyper: lägg till zon, ta bort zon (vald slumpmässigt)
        for k in range(0, temperature):
            t = 1 - (k + 1) / temperature  # chansen att en sämre mutation accepteras (modifierat med hur mycket sämre den är)
            z = random.choice(path[:-1])  # zonen som används för att mutera
            remove = True

            if random.random() > .5 or len(path) == 2:  # addition
                x = random.choice(zlist)
                pos = random.randint(1, len(path) - 1)
                pp = path[pos]
                pp1_ = path[pos - 1]
                newdist = dist + zonedistance[x][pp1_] + zonedistance[x][pp] - zonedistance[pp1_][pp]
                if newdist <= maxdistance:
                    if x not in path:
                        newpts = pts + zonepoints[x]
                    else:
                        newpts = pts
                    newpath = path.copy()
                    newpath.insert(pos, x)
                    remove = False
            if remove == True:  # subtraktion
                pos = random.randint(1, len(path) - 2)
                pp = path[pos]
                pp1 = path[pos + 1]
                pp1_ = path[pos - 1]
                newdist = dist + zonedistance[pp1_][pp1] - zonedistance[pp][pp1] - zonedistance[pp][pp1_]
                if newdist <= maxdistance:
                    newpath = path.copy()
                    newpath.pop(pos)
                    if pp not in newpath:
                        newpts = pts - zonepoints[pp]
                    else:
                        newpts = pts

            e = nrg(dist, pts)
            enew = nrg(newdist, newpts)
            if enew >= e:  # sämre
                if random.random() <= t * e / enew:
                    path = newpath
                    pts = newpts
                    dist = newdist
            else:  # bättre
                path = newpath
                pts = newpts
                dist = newdist
        newpath = []
        donelist = []
        for zone in path:
            if zone in zlist and zone not in donelist:
                donelist.append(zone)
                newpath.append(zone)
        path = [start] + newpath + [end]

        if debugrandompath == True:
            print(path)
        print("...")

        newpath = []
        newdist = 0
        px = ""
        py = ""
        x = 0
        y = 0
        # dags att optimisera avståndet, enda mutationstypen är nu att byta plats på två zoner
        for k in range(0, int(temperature / 10)):
            t = 1 - (k + 1) / (temperature / 10)

            while True:
                x = random.randint(1, len(path) - 2)
                while True:
                    y = random.randint(1, len(path) - 2)
                    if y != x:
                        break
                px = path[x]
                px1 = path[x + 1]
                px1_ = path[x - 1]
                py = path[y]
                py1 = path[y + 1]
                py1_ = path[y - 1]
                newdist = 0
                if px1 == py:  # y efter x
                    newdist = dist - zonedistance[px][px1_] + zonedistance[py][px1_] - zonedistance[py][py1] + zonedistance[px][py1]
                elif py1 == px:  # x efter y
                    newdist = dist - zonedistance[px][px1] + zonedistance[py][px1] - zonedistance[py][py1_] + zonedistance[px][py1_]
                else:
                    newdist = dist - zonedistance[px][px1] - zonedistance[px][px1_] + zonedistance[py][px1] + zonedistance[py][px1_] \
                                   - zonedistance[py][py1] - zonedistance[py][py1_] + zonedistance[px][py1] + zonedistance[px][py1_]
                if newdist <= maxdistance:
                    newpath = path.copy()
                    newpath[x] = py
                    newpath[y] = px
                    break
            if newdist <= dist:  # bättre
                path = newpath
                dist = newdist

        if debugrandompath == True:
            print(path)

    newpath = [start]
    for n in range(1, len(path)):
        newpath += zonepathfromto[path[n - 1]][path[n]][1:]
    path = newpath

    # skriv ut resultatet
    print("Hittad rutt:")
    result = str(pts) + " poäng, " + str(len(path)) + " st, " + str(int(dist / speed)) + " min: "
    c = 0
    for zone in path:
        if zone[:2] != "k-" and zone not in path[2:c]:
            result += zone.upper() + "-"
        c += 1
    print(result[:-1] + "\n\n" + str(path) + "\n\nProcessen tog " + str(round(time.time() - timeatstart, 2)) + " sekunder")


elif algorithm == "tabu":
    tabulist = [[start, end]]
    def nrg(d, p):
        if p != 0:
            return 1 / (p + d / 1000)  # energifunktion som värderar poäng mycket högre än avstånd
        else:
            return 999
    bestever = [start, end]
    bestever_dist = zonedistance[start][end]
    bestever_pts = zonepoints[start] + zonepoints[end]
    bestpath = [start, end]
    bestpath_dist = zonedistance[start][end]
    bestpath_pts = zonepoints[start] + zonepoints[end]

    for k in range(tabuiterations): # fungerar likt annealing: varje iteration muteras pathen bestpath på alla möjliga
                                    # sätt, den bästa nya pathen jämförs och accepteras kanske som ny bestpath
        bestcandidate = None
        bestcandidate_dist = 1
        bestcandidate_pts = 0
        seed = random.random()
        #print(bestpath, bestpath_dist, bestpath_pts)
        if seed <= 1/3:
            for zone in zlist: # mutation: addera
                if zone not in bestpath:
                    for x in range(1, len(bestpath)): # testar sätta in som så: [...z1, zone, z2...]
                        z1 = bestpath[x - 1]
                        z2 = bestpath[x]
                        newdist = bestpath_dist - zonedistance[z1][z2] + zonedistance[z1][zone] + zonedistance[z2][zone]
                        newpts = bestpath_pts + zonepoints[zone]
                        if nrg(newdist, newpts) < nrg(bestcandidate_dist, bestcandidate_pts) and newdist <= maxdistance:
                            newpath = bestpath[:x] + [zone] + bestpath[x:]
                            if newpath not in tabulist:
                                bestcandidate = newpath.copy()
                                bestcandidate_dist = newdist
                                bestcandidate_pts = newpts

        elif seed >= 2/3:
            if len(bestpath) >= 3: # mutation: subtrahera
                for x in range(1, len(bestpath) - 1): # [...z1, (z, )z2...]
                    z = bestpath[x]
                    z1 = bestpath[x - 1]
                    z2 = bestpath[x + 1]
                    newdist = bestpath_dist + zonedistance[z1][z2] - zonedistance[z1][z] - zonedistance[z2][z]
                    newpts = bestpath_pts - zonepoints[z]
                    if nrg(newdist, newpts) < nrg(bestcandidate_dist, bestcandidate_pts) and newdist <= maxdistance:
                        newpath = [zz for zz in bestpath if zz != z]
                        if newpath not in tabulist:
                            bestcandidate = newpath.copy()
                            bestcandidate_dist = newdist
                            bestcandidate_pts = newpts

        else:
            if len(bestpath) >= 4:  # mutation: swap
                for x in range(1, len(bestpath) - 1):
                    for y in range(1, len(bestpath) - 1):
                        if y != x:
                            zx = bestpath[x]
                            z1x = bestpath[x - 1]
                            z2x = bestpath[x + 1]
                            zy = bestpath[y]
                            z1y = bestpath[y - 1]
                            z2y = bestpath[y + 1]
                            newpts = bestpath_pts
                            if z2x == zy:  # y efter x
                                newdist = bestpath_dist - zonedistance[zx][z1x] + zonedistance[zy][z1x] - \
                                          zonedistance[zy][z2y] + zonedistance[zx][z2y]
                            elif z2y == zx:  # x efter y
                                newdist = bestpath_dist - zonedistance[zx][z2x] + zonedistance[zy][z2x] - \
                                          zonedistance[zy][z1y] + zonedistance[zx][z1y]
                            else:  # x och y ej bredvid
                                newdist = bestpath_dist - zonedistance[zx][z2x] - zonedistance[zx][z1x] + \
                                          zonedistance[zy][z2x] + zonedistance[zy][z1x] - zonedistance[zy][z2y] - \
                                          zonedistance[zy][z1y] + zonedistance[zx][z2y] + zonedistance[zx][z1y]
                            if nrg(newdist, bestcandidate_pts) < nrg(bestcandidate_dist, bestcandidate_pts) \
                            and newdist <= maxdistance:
                                newpath = bestpath.copy()
                                newpath[x] = zy
                                newpath[y] = zx
                                if newpath not in tabulist:
                                    bestcandidate = newpath.copy()
                                    bestcandidate_dist = newdist
                                    bestcandidate_pts = newpts

        if bestcandidate is not None:
            if nrg(bestcandidate_dist, bestcandidate_pts) < nrg(bestever_dist, bestever_pts):
                bestever = bestcandidate.copy()
                bestever_dist = bestcandidate_dist
                bestever_pts = bestcandidate_pts
            bestpath = bestcandidate.copy()
            bestpath_dist = bestcandidate_dist
            bestpath_pts = bestcandidate_pts
            tabulist.append(bestcandidate)
            if len(tabulist) > tabusize:
                tabulist.pop(0)

    newpath = [start]
    for n in range(1, len(bestever)):
        newpath += zonepathfromto[bestever[n - 1]][bestever[n]][1:]
    bestever = newpath

    # skriv ut resultatet
    print("Hittad rutt:")
    result = str(bestever_pts) + " poäng, " + str(len(bestever)) + " st, " + str(int(bestever_dist / speed)) + " min: "
    c = 0
    for zone in bestever:
        if zone[:2] != "k-" and zone not in bestever[2:c]:
            result += zone.upper() + "-"
        c += 1
    print(result[:-1] + "\n\n" + str(bestever) + "\n\nProcessen tog " + str(round(time.time() - timeatstart, 2)) + " sekunder")
