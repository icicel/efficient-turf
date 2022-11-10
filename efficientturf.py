
### SETTINGS

# debug
debug_unused_paths = True # shows all connections that weren't used by any finished path
debug_central_zones = False # shows what zones are the most and least central
debug_show_zone_points = True
debug_show_artipoints = True # shows articulation points
debug_show_random_path = True # shows a random active path after every process step
debug_print_zone_data = False # shows zone information in excel format (tab-separated)

# start and end zone
start = "k-klassrum"
end = "k-gymnasiet"

# choice of algorithm (bruteforce, quickbrute) (currently does nothing)
algorithm = "bruteforce"

# blacklist certain zones
blacklist = []
# convert above to a whitelist
whitelist = False

# your turfing speed (m/min), used to convert distances to time
speed = 64

# turf username
username = "icicle"

# backup file name (*.pk)
dumpname = "turf"

# list of all zones
zlist = ["campingpiren", "surfview", "nösnäsån", "gulzon", "bathview", "nösnäsbacken", "hallernazon", "kozon",
         "genomskogen", "sneezenose", "dragkamp", "inklämdpågräs", "solgårdsstig", "husarrondell", "movedwindmill",
         "kvarnskogen", "stenryttare", "kvarntäppan", "trädväg", "liteskogbara", "hasselbacke", "frispel", "tullaull",
         "yttreucklums", "ucklumcykel", "kringelikrok", "norumskyrka", "jansvy", "bakomängen", "torpzone", "sköntgrönt",
         "motfurufjäll", "gamlahallerna", "odlamedcykel"]

# list of crossing zones (k for "korsning")
klist = ["k-klassrum", "k-nösnäs", "k-gymnasiet", "k-backen", "k-ucklum", "k-hallerna", "k-solgård", "k-kristinedal",
         "k-camping", "k-kvarnberg", "k-skogsbryn", "k-älvhem", "k-strandnorum", "k-tuvull", "k-kyrkenorum"]

# articulation points connected to 3+ blocks (not detected by the algorithm)
arti3points = ["nösnäsån", "k-camping"]

# connections between zones as ["zone 1", "zone 2", (length in meters)]
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






### PREPARE DATA

import time, requests, pickle#rick
from datetime import datetime
if debug_show_random_path == True:
    import random
maxdistance = 0
if debug_print_zone_data == False:
    if algorithm == "bruteforce":
        maxdistance = speed * int(input("Time in minutes (max 120):\n> "))
    else:
        maxdistance = speed * int(input("Time in minutes:\n> "))
time_at_start = time.time()
round_hours_left = 0
has_connection = True
has_backup = True
backup_old = False
backup_bad = False

def str2time(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").timestamp()

# round info
try:
    rounds = requests.get("http://api.turfgame.com/v4/rounds").json()
    for month in rounds: # loop until the current round is found
        start_time = str2time(month["start"])
        if start_time > time.time():
            break
    round_hours_left = (start_time - time.time()) / 3600
except requests.exceptions.ConnectionError: # no wifi?
    has_connection = False

try:
    with open(dumpname + ".pk", "rb") as file:
        dump = pickle.load(file)
    if time.time() - dump[1] >= 3600 * 24:
        backup_old = True # if the backup is older than 24 hours
    for zone in zlist:
        if zone not in dump[0]:
            backup_bad = True # if not all zones exist in the backup
except FileNotFoundError:
    has_backup = False

if debug_print_zone_data == True:
    print("name\tage\tpotential days\tpts on take\tpts per hour\tpts total\ttake age\trevisit pts\tneutral pts")
    for zone in zlist:
        line = [zone]
        while True:
            try:
                zone_data = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                break
            except KeyError:
                pass
        hours_existed = (time.time() - str2time(zone_data["dateCreated"])) / 3600
        potential_hours = min(hours_existed / zone_data["totalTakeovers"], round_hours_left)
        line.append(int(hours_existed / 24))
        line.append(round(potential_hours / 24, 1))
        line.append(int(zone_data["takeoverPoints"]))
        line.append(int(zone_data["pointsPerHour"]))
        line.append(int(zone_data["takeoverPoints"] + potential_hours * zone_data["pointsPerHour"]))

        try:
            if zone_data["currentOwner"]["name"] == username:
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
        except KeyError:
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
        print("Loading backup file")
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
        zonepoints = dump[0]
        for zone in klist:
            zonepoints[zone] = 0
    else:
        if backup_old:
            print("Backup too old")
        elif backup_bad:
            print("Backup is incomplete")
        else:
            print("No backup file found")
        for zone in zlist:
            print("Getting zone data... (" + str(zlist.index(zone) + 1) + "/" + str(len(zlist)) + ")")
            if (whitelist == False and zone not in blacklist) or (whitelist == True and zone in blacklist):
                while True: # if you go over one request per second the api gives garbage instead
                    try:
                        zone_data = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zone}]).json()[0]
                        break
                    except KeyError:
                        pass
                hours_existed = (time.time() - str2time(zone_data["dateCreated"])) / 3600
                potential_hours = min(hours_existed / zone_data["totalTakeovers"], round_hours_left) # average hours before the zone is lost
                zonepoints[zone] = int(zone_data["takeoverPoints"] + potential_hours * zone_data["pointsPerHour"])

                try:
                    if zone_data["currentOwner"]["name"] == username: # if currentOwner is yourself - revisit points if over 23 hours ago
                        hours_since_taken = (time.time() - str2time(zone_data["dateLastTaken"])) / 3600
                        if hours_since_taken > 23:
                            zonepoints[zone] = int(zone_data["takeoverPoints"] / 2)
                        else:
                            zonepoints[zone] = 0
                except KeyError: # no currentOwner - gives neutral bonus instead
                    zonepoints[zone] += 50
            else:
                zonepoints[zone] = 0
        for zone in klist: # crossings don't give points
            zonepoints[zone] = 0
        with open(dumpname + ".pk", "wb") as file:
            pickle.dump([zonepoints, time.time()], file)
else:
    if has_backup:
        print("No connection, loading backup file")
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
        zonepoints = dump[0]
        for zone in klist:
            zonepoints[zone] = 0
        for zone in zlist:
            if zone not in zonepoints:
                zonepoints[zone] = 0
    else:
        quit(print("No connection, no backup file found"))

# collect all zones (and their connections)
zones = {}
for zone in zonepoints:
    zones[zone] = []
for con in connections:
    zones[con[0]].append((con[1], con[2]))
    zones[con[1]].append((con[0], con[2]))

# contains the fastest path from every zone to every other zone
zonedistance = {}
zonepathfromto = {}
endpaths = []
for endzone in zonepoints:
    if zonepoints[endzone] != 0 or endzone == start or endzone == end:
        # sub-algorithm, calculates the fastest path from "endzone" to every other zone
        endzonedistance = {endzone: 0}
        endzonepathto = {endzone: [endzone]}
        for connection in zones[endzone]:
            endpaths.append([connection[1], connection[0]])
        while True: # for every loop, the shortest path is chosen and extended
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
        # collects the information in the big dictionaries
        zonedistance[endzone] = endzonedistance
        zonepathfromto[endzone] = endzonepathto

# finds all articulation points, en.wikipedia.org/wiki/Biconnected_component
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
extend(end, 0) # run the algorithm with two different zones in case one of them is an articulation point
if artipoints.count(start) == 1: # the starting zone always counts itself for some reason
    artipoints.remove(start)
artipoints = list(dict.fromkeys(artipoints))
if debug_show_artipoints == True:
    print(artipoints)

# debug stuff
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


if maxdistance == 0: # no reason to even start the loop if this is the case
    quit()
# the starting path is different if the starting zone gives points
paths = [[0, 0, 1, 0, start]] if zonepoints[start] == 0 else [[0, zonepoints[start], 1, 0, start]]






### PROCESS

print("\nUppstart tog " + str(round(time.time() - time_at_start, 2)) + " sekunder\n")
time_at_start = time.time()
# a path is defined as: 
# [path distance, path points, zones since the last point giving one, the distance between these zones, zone 0, zone 1, zone 2...]
finishedpaths = []
largestnum = 0 # finished paths are only accepted if they have the most points out of all finished paths so far
step = 1

while True:
    toadd = []
    for path in paths:
        lastzone = path[-1]
        lastlastzone = path[-2]
        for newzone, newdistance in zones[lastzone]:
            points = path[1]
            conseczones = path[2]
            consecdist = path[3]
            lastcapturedzone = path[-conseczones]
            newzone = connection[0]
            newdistance = connection[1]
            distance = path[0] + newdistance

            # and now, some optimizations!
            # if one of these situations happen it means that there exists another, better path, and this path is removed
            if maxdistance - distance < zonedistance[end][newzone]: # if it can't be finished without exceeding the time limit
                continue
            if newzone == lastcapturedzone: # if it returns to a zone without visiting any point-giving zones
                continue
            if zonepoints[newzone] != 0 and newzone not in path:
                if consecdist + newdistance > zonedistance[lastcapturedzone][newzone]: # if it hasn't taken the fastest path to the new zone
                    continue
            if newzone in path and newzone != end:
                if path.count(newzone) > 1: # if a zone has been visited three times
                    if newzone not in arti3points: # (unless it might have been necessary)
                        continue
                if path[5] != newzone: # if it doesn't return to a zone via the connection it left it with
                    if newzone not in artipoints:
                        reversepath = path[::-1]
                        if reversepath[reversepath.index(newzone) - 1] != lastzone:
                            continue
            if (lastzone, newzone) in zip(path[4:], path[5:]): # if it uses the same connection in the same direction twice
                continue

            if zonepoints[newzone] != 0 and newzone not in path: # point giving
                points += zonepoints[newzone]
                conseczones = 1
                consecdist = 0
            else: # not point giving
                conseczones += 1
                consecdist += newdistance
            toadd.append([distance, points, conseczones, consecdist] + path[4:] + [newzone])
        if lastzone == end and path[1] >= largestnum:
            largestnum = path[1]
            finishedpaths.append(path)

    paths = [path for path in toadd]
    if paths == []: # if all paths are finished
        break
    if debug_show_random_path:
        print(random.choice(paths))

    # removes identical paths
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

    print("At step " + str(step) + " there were " + str(len(paths)) + " active paths and " + str(len(finishedpaths)) + " finished")
    step += 1
if len(finishedpaths) == 0:
    quit(print("\nNo possible paths found"))

# clean up the finished paths
finishedpaths.sort(key = lambda x:x[1], reverse = True)
paths = []
for path in finishedpaths:
    if path[1] >= finishedpaths[0][1] * 0.8: # removes really short finished paths
        paths.append(path[:2] + path[4:]) # conseczones and consecdist removed
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


# checks for practically identical paths
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

# one last sort!
paths.sort(key = lambda x:x[1], reverse = True)

# writes all other acceptable paths
print("\nAll paths:")
if len(paths) > 1: 
    for path in paths:
        result = str(round(path[1], 1)) + " points, " + str(int(path[0] / speed)) + " min: "
        for zone in path[2:]:
            if zone[:2] != "k-":
                result += zone.upper() + "-"
        print(result[:-1])
    print()

# write the result
print("Best path:")
best = paths[0].copy()
zone_count = 0
path_str = ""
c = 2
for zone in best[2:]:
    if zone[:2] != "k-" and zone not in best[2:c]:
        path_str += zone.upper() + "-"
        zone_count += 1
    c += 1
result = str(round(best[1], 1)) + " points, " + str(zone_count) + " zones, " + str(int(best[0] / speed)) + " min: " + path_str
print(result[:-1] + "\n\n" + str(best) + "\n\nThe process took " + str(round(time.time() - time_at_start, 2)) + " seconds")
