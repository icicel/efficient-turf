
### SETTINGS

# debug
debug_unused_connections = False # shows all connections that weren't used by any finished path
debug_central_zones = False # shows what zones are the most and least central
debug_show_zone_points = False # shows the zone points dictionary
debug_show_artipoints = False # shows articulation points and articulation point-related stuff
debug_show_random_path = False # shows a random active path after every process step
debug_print_zone_data = False # shows zone information in excel format (tab-separated)

# choice of algorithm (bruteforce, quickbrute) (currently does nothing)
algorithm = "bruteforce"

# separate file (data_*.py) containing data such as zone names, connections, start_zone/end_zone zone etc.
# check data_template.py for examples
data_set = "template"

# your turfing speed (m/min), used to convert distances to time
speed = 64

# turf username
username = "icicle"

# backup file name (*.pk)
dumpname = "turf"







### PREPARE DATA

import time, requests, random, importlib, pickle#rick
from datetime import datetime
if debug_print_zone_data:
    maxdistance = 0
else:
    maxdistance = speed * int(input("Time in minutes:\n> "))
data = importlib.import_module("data_" + data_set)
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
    for zone in data.zlist:
        if zone not in dump[0]:
            backup_bad = True # if not all zones exist in the backup
except FileNotFoundError:
    has_backup = False

if debug_print_zone_data == True:
    print("name\tage\tpotential days\tpts on take\tpts per hour\tpts total\ttake age\trevisit pts\tneutral pts")
    for zone in data.zlist:
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
        for zone in data.klist:
            zonepoints[zone] = 0
    else:
        if backup_old:
            print("Backup too old")
        elif backup_bad:
            print("Backup is incomplete")
        else:
            print("No backup file found")
        for zone in data.zlist:
            print("Getting zone data... (" + str(data.zlist.index(zone) + 1) + "/" + str(len(data.zlist)) + ")")
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
        for zone in data.klist: # crossings don't give points
            zonepoints[zone] = 0
        with open(dumpname + ".pk", "wb") as file:
            pickle.dump([zonepoints, time.time()], file)
else:
    if has_backup:
        print("No connection, loading backup file")
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
        zonepoints = dump[0]
        for zone in data.klist:
            zonepoints[zone] = 0
        for zone in data.zlist:
            if zone not in zonepoints:
                zonepoints[zone] = 0
    else:
        quit(print("No connection, no backup file found"))

# collect all zones (and their connections)
zones = {}
if data.whitelist:
    for zone in zonepoints:
        if zone in data.blacklist:
            zones[zone] = []
else:
    for zone in zonepoints:
        if zone not in data.blacklist:
            zones[zone] = []
for zone1, zone2, length in data.connections:
    if zone1 in zones and zone2 in zones:
        zones[zone1].append((zone2, length))
        zones[zone2].append((zone1, length))

# filter out (kill) zones that can't be reached from start_zone
if data.blacklist:
    kill_list = list(zones.keys())
    def survive(zone):
        kill_list.remove(zone)
        for neighbor, _ in zones[zone]:
            if neighbor in kill_list:
                survive(neighbor)
    survive(data.start_zone)
    if data.end_zone in kill_list:
        quit(print("\nNo possible paths found"))
    print("Unreachable zones were deleted: " + ", ".join(kill_list))
    for zone in list(zones.keys()): # remake zones without these unreachable zones
        if zone in kill_list:
            del zones[zone]
        zones[zone] = []
    for zone1, zone2, length in data.connections:
        if zone1 in zones and zone2 in zones:
            zones[zone1].append((zone2, length))
            zones[zone2].append((zone1, length))

# contains the fastest path from every zone to every other zone
zonedistance = {}
zonepathfromto = {}
endpaths = []
for endzone in zones:
    if zonepoints[endzone] != 0 or endzone == data.start_zone or endzone == data.end_zone:
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
def get_artipoints(zone, d):
    visited.append(zone)
    depth[zone] = d
    low[zone] = d
    children = 0
    is_artipoint = False
    for child, _ in zones[zone]:
        if not child in visited:
            parent[child] = zone
            get_artipoints(child, d + 1)
            children += 1
            if low[child] >= depth[zone]:
                is_artipoint = True
            low[zone] = min(low[zone], low[child])
        elif zone not in parent or child != parent[zone]:
            low[zone] = min(low[zone], depth[child])
    if (zone in parent and is_artipoint) or (zone not in parent and children > 1):
        artipoints.append(zone)
get_artipoints(data.start_zone, 0)

# finds articulation points connected to 3+ blocks specifically
arti3points = []
block_amount = {}
def visit(zone):
    visited.append(zone)
    for neighbor, _ in zones[zone]:
        if neighbor not in visited:
            visit(neighbor)
for zone in artipoints:
    connected_blocks = 0
    visited = [zone]
    for neighbor, _ in zones[zone]:
        if neighbor not in visited:
            visit(neighbor)
            connected_blocks += 1
    if connected_blocks >= 3:
        arti3points.append(zone)
    block_amount[zone] = connected_blocks

# debug stuff
if debug_show_artipoints == True:
    print("\nArtipoint stuff:")
    print(artipoints, arti3points, block_amount, sep="\n")
if debug_central_zones == True:
    tl = []
    for startzone in zonedistance:
        c = 0
        for endzone in zonedistance[startzone]:
            c += zonedistance[startzone][endzone]
        tl.append([c, startzone])
    tl.sort(key = lambda x:x[0])
    print("\nMost central zone: " + tl[0][1] + "\nMost isolated zone: " + tl[-1][1])
if debug_show_zone_points == True:
    print("\nZone points:")
    print(dict(sorted(zonepoints.items(), key=lambda x: x[1], reverse=True)))


if maxdistance == 0: # no reason to even start the loop if this is the case
    quit()
# initialize paths! let's go!
paths = [[0, zonepoints[data.start_zone], data.start_zone, 0, data.start_zone]]






### PROCESS

print("\nStartup took " + str(round(time.time() - time_at_start, 2)) + " seconds\n")
time_at_start = time.time()
# a path is defined as: 
# [path distance, path points, last point giving zone visited, distance gone since it was visited, zone 0, zone 1, zone 2...]
finished_paths = []
best_points = 0 # finished paths are only accepted if they have the most points out of all finished paths so far
step = 1

while True:
    toadd = []
    for path in paths:
        last_zone = path[-1]
        points = path[1]
        last_captured_zone = path[2]
        last_captured_distance = path[3]
        path_zones = path[4:]
        for new_zone, new_distance in zones[last_zone]:
            distance = path[0] + new_distance
            new_zone_gives_points = zonepoints[new_zone] != 0 and new_zone not in path_zones

            # and now, some optimizations!
            # if one of these situations happen it means that there (probably) exists another, better path, and this path is removed

            if maxdistance - distance < zonedistance[data.end_zone][new_zone]: # if it can't be finished without exceeding the time limit
                continue
            if new_zone == last_captured_zone: # if it returns to a zone without visiting any point-giving zones
                continue
            if new_zone_gives_points and last_captured_distance + new_distance > zonedistance[last_captured_zone][new_zone]: # if it hasn't taken the fastest path to the new zone
                continue
            used_connections = zip(path_zones, path_zones[1:])
            if (last_zone, new_zone) in used_connections: # if it uses the same connection in the same direction twice
                continue
            if new_zone in path_zones and new_zone != data.end_zone: # if it returns to a zone
                if path_zones.count(new_zone) > 1 and new_zone not in arti3points: # if the zone has been visited three times
                    continue
                if (new_zone, last_zone) not in used_connections and new_zone not in artipoints: # if it doesn't return to the zone via the connection it left it with
                    continue

            if new_zone_gives_points:
                toadd.append([distance, points + zonepoints[new_zone], new_zone, 0] + path_zones + [new_zone])
            else:
                toadd.append([distance, points, last_captured_zone, last_captured_distance + new_distance] + path_zones + [new_zone])
        if last_zone == data.end_zone and points >= best_points:
            best_points = points
            finished_paths.append(path)

    del paths
    paths = toadd
    if paths == []: # if all paths are finished
        break
    if debug_show_random_path:
        print(random.choice(paths))

    print("At step " + str(step) + " there were " + str(len(paths)) + " active paths and " + str(len(finished_paths)) + " finished")
    step += 1
if len(finished_paths) == 0:
    quit(print("\nNo possible paths found"))

# clean up the finished paths
finished_paths.sort(key=lambda x:x[1], reverse=True)
# remove paths not clearing this threshold
threshold = finished_paths[0][1] * 0.8
temp = []
for path in finished_paths:
    if path[1] >= threshold: 
        temp.append(path[:2] + path[4:]) # last_captured_zone and last_captured_distance removed
    else:
        finished_paths = temp
        break

if debug_unused_connections == True:
    # collects all connections that the finished paths use
    used_connections = set()
    for path in finished_paths:
        for connection in zip(path[2:], path[3:]):
            used_connections.add(set(connection))
    
    # gathers all connections not in used_connections
    unused_connections = []
    for zone in zones:
        for neighbor, _ in zones[zone]:
            connection = {zone, neighbor}
            if connection not in used_connections and connection not in unused_connections:
                unused_connections.append(connection)
    unused_connections = [tuple(x) for x in unused_connections]
    unused_connections.sort()
    print("\nUnused paths:")
    print(unused_connections)

# checks for practically identical paths
dupecheck = []
to_delete = []
for i, path in enumerate(finished_paths):
    dupe = set(path[2:])
    if dupe in dupecheck:
        to_delete.append(i)
    else:
        dupecheck.append(dupe)
for n in to_delete[::-1]:
    finished_paths.pop(n)

# shortest path at the front
finished_paths.sort(key=lambda x:x[0])
# path with most points at the front (with ties broken by length because of the above line)
finished_paths.sort(key=lambda x:x[1], reverse=True)

# writes all other acceptable paths
print("\nAll paths:")
if len(finished_paths) != 1: 
    for path in finished_paths:
        print("{} points, {} min: {}".format(
            round(path[1], 1),
            str(int(path[0] / speed)),
            "-".join([zone.upper() for zone in path[2:] if zone in data.zlist])))

# write the result
print("\nBest path:")
best = finished_paths[0]
best_zones = []
for i, zone in enumerate(best[2:]):
    if zone in data.zlist and zone not in best[2:i+2]:
        best_zones.append(zone.upper())
print("{} points, {} zones, {} min: {}\n\nTechnical representation:\n{}\n\nThe process took {} seconds".format(
    str(round(best[1], 1)),
    str(len(best_zones)),
    str(int(best[0] / speed)),
    "-".join(best_zones),
    str(best),
    str(round(time.time() - time_at_start, 2))))
