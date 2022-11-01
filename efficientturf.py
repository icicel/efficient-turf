
# INSTÄLLNINGAR

# debug
debug_unused_paths = True # visar vilka förbindelser som inte använts av en finished path
debug_central_zones = False # visar vilka zoner som är mest och minst centralt belägna
debug_show_zone_points = True # visar zonernas poäng
debug_show_artipoints = True # visar articulation points
debug_show_random_path = True # visar en slumpmässig pågående rutt efter varje steg i processen
debug_print_zone_data = False # visar information om zonerna i excelformat

# start- och slutzon
start = "k-klassrum"
end = "k-gymnasiet"

# vilken algoritm (bruteforce, quickbrute)
algorithm = "quickbrute"

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
import time, requests, pickle#rick
from datetime import datetime
if debug_show_random_path == True:
    import random
maxdistance = 0
if debug_print_zone_data == False:
    if algorithm == "bruteforce":
        maxdistance = speed * int(input("Tid i minuter (max 120):\n> "))
    else:
        maxdistance = speed * int(input("Tid i minuter:\n> "))
time_at_start = time.time()
round_hours_left = 0
has_connection = True
has_backup = True
backup_old = False
backup_bad = False

def str2time(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").timestamp()

# rund-info
try:
    rounds = requests.get("http://api.turfgame.com/v4/rounds").json()
    for month in rounds: # loopa tills aktiv runda hittats
        start_time = str2time(month["start"])
        if start_time > time.time():
            break
    round_hours_left = (start_time - time.time()) / 3600
except requests.exceptions.ConnectionError: # get wifi anywhere you go
    has_connection = False

try:
    with open(dumpname + ".pk", "rb") as file:
        dump = pickle.load(file)
    if time.time() - dump[1] >= 3600 * 24:
        backup_old = True # om mer än en dag har gått sedan föregående request
    for zone in zlist:
        if zone not in dump[0]:
            backup_bad = True # om inte alla zoner finns i backup
except FileNotFoundError:
    has_backup = False

if debug_print_zone_data == True:
    print("name\tage\tpotential days\tpts on take\tpts per hour\tpts total\ttake age\trevisit pts\tneutral pts")
    for zone in zlist:
        line = [zone]
        while True:  # går man över en request i sekunden ger api:n garbage istället
            try:
                zone_data = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                break
            except KeyError:
                pass
        hours_existed = (time.time() - str2time(zone_data["dateCreated"])) / 3600
        potential_hours = min(hours_existed / zone_data["totalTakeovers"], round_hours_left)  # antal timmar innan zonen förloras
        line.append(int(hours_existed / 24))
        line.append(round(potential_hours / 24, 1))
        line.append(int(zone_data["takeoverPoints"]))
        line.append(int(zone_data["pointsPerHour"]))
        line.append(int(zone_data["takeoverPoints"] + potential_hours * zone_data["pointsPerHour"]))

        try:
            if zone_data["currentOwner"]["name"] == username:  # currentOwner är en själv - revisit-poäng om för över 23 timmar sedan
                hours_since_taken = (time.time() - str2time(zone_data["dateLastTaken"])) / 3600
                line.append(int(hours_since_taken / 24))
                if hours_since_taken >= 23:
                    line.append(int(zone_data["takeoverPoints"] / 2))
                else:
                    line.append(0)
            else:
                line.append("")
                line.append("")
            line.append("")
        except KeyError:  # ingen currentOwner - blir neutralbonus istället
            line.append("")
            line.append("")
            line.append(50)
        line = [str(x) for x in line]
        print("\t".join(line).replace(".",","))
    quit()

zonepoints = {}
zone_data = {}
if has_connection:
    if not backup_old and not backup_bad and has_backup:
        print("Laddar backupfil")
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
        zonepoints = dump[0]
        for zone in klist:
            zonepoints[zone] = 0
    else:
        if backup_old:
            print("Backupfil för gammal")
        elif backup_bad:
            print("Ingen giltig backupfil hittad")
        else:
            print("Ingen backupfil hittad")
        for zone in zlist:
            print("Skickar efter data... (" + str(zlist.index(zone) + 1) + "/" + str(len(zlist)) + ")")
            if (whitelist == False and zone not in blacklist) or (whitelist == True and zone in blacklist):
                while True:  # går man över en request i sekunden ger api:n garbage istället
                    try:
                        zone_data = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                        break
                    except KeyError:
                        pass
                hours_existed = (time.time() - str2time(zone_data["dateCreated"])) / 3600
                potential_hours = min(hours_existed / zone_data["totalTakeovers"], round_hours_left)  # antal timmar innan zonen förloras
                zonepoints[zone] = int(zone_data["takeoverPoints"] + potential_hours * zone_data["pointsPerHour"])

                try:
                    if zone_data["currentOwner"]["name"] == username:  # currentOwner är en själv - revisit-poäng om för över 23 timmar sedan
                        hours_since_taken = (time.time() - str2time(zone_data["dateLastTaken"])) / 3600
                        if hours_since_taken > 23:
                            zonepoints[zone] = int(zone_data["takeoverPoints"] / 2)
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
    if has_backup:
        if not backup_bad:
            if not backup_old:
                print("Ingen anslutning, laddar backupfil")
            else:
                print("Ingen anslutning, laddar gammal backupfil")
        else:
            print("Ingen anslutning, laddar ogiltig backupfil")
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
        zonepoints = dump[0]
        for zone in klist:
            zonepoints[zone] = 0
        for zone in zlist:
            if zone not in zonepoints:
                zonepoints[zone] = 0
    else:
        quit(print("Ingen anslutning, ingen backupfil hittad"))

# samla alla zoner
zones = {}
for zone in zonepoints:
    zones[zone] = []
for con in connections:
    zones[con[0]].append([con[1], con[2]])
    zones[con[1]].append([con[0], con[2]])

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
if debug_show_artipoints == True:
    print(artipoints)

# debug-grejer
if debug_central_zones == True:
    tl = []
    for startzone in zonedistance:
        c = 0
        for endzone in zonedistance[startzone]:
            c += zonedistance[startzone][endzone]
        tl.append([c, startzone])
    tl.sort(key = lambda x:x[0])
    print("\nMest centrala zon: " + tl[0][1] + "\nMest isolerade zon: " + tl[-1][1] + "\n")
if debug_show_zone_points == True:
    print(dict(sorted(zonepoints.items(), key=lambda x: x[1], reverse=True)))
if maxdistance == 0: # ingen idé att ens påbörja loopen om detta är fallet
    quit()



# annorlunda startrutt om man startar på en poänggivande zon
paths = [[0, 0, 1, 0, start]] if zonepoints[start] == 0 else [[0, zonepoints[start], 1, 0, start]]

# den stora genereringsloopen
print("\nUppstart tog " + str(round(time.time() - time_at_start, 2)) + " sekunder\n")
time_at_start = time.time()
# en rutt är uppbyggd som så: id: [sträcka, rutt-poäng, antal zoner sedan den senaste poänggivande, dessas sträcka, zoner...]
finishedpaths = []
largestnum = 0 # färdiga rutter accepteras bara om de har mer än den hittills bästa färdiga ruttens poäng
step = 1

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
                if path.count(newzone) > 1: # om den varit på en zon tre gånger
                    if newzone not in arti3points:
                        continue
                if path[5] != newzone: # om den inte återvänder till en zon via förbindelsen den lämnade zonen med (alltså, en loop)
                    if newzone not in artipoints:
                        reversepath = path[::-1]
                        if reversepath[reversepath.index(newzone) - 1] != lastzone:
                            continue
            if (lastzone, newzone) in zip(path[4:], path[5:]): # om den använder samma förbindelse åt samma håll två gånger
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
    if debug_show_random_path:
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

    print("Vid steg " + str(step) + " finns " + str(len(paths)) + " pågående rutter och " + str(len(finishedpaths)) + " färdiga")
    step += 1
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

if debug_unused_paths == True:
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
zone_count = 0
path_str = ""
c = 2
for zone in best[2:]:
    if zone[:2] != "k-" and zone not in best[2:c]:
        path_str += zone.upper() + "-"
        zone_count += 1
    c += 1
result = str(round(best[1], 1)) + " poäng, " + str(zone_count) + " st, " + str(int(best[0] / speed)) + " min: " + path_str
print(result[:-1] + "\n\n" + str(best) + "\n\nProcessen tog " + str(round(time.time() - time_at_start, 2)) + " sekunder")
