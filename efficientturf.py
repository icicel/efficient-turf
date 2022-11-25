
### SETTINGS

# debug
debug_unused_connections = False # shows all connections that weren't used by any finished path
debug_central_zones = False # shows what zones are the most and least central
debug_show_zone_points = False # shows the zone points dictionary
debug_show_artipoints = False # shows articulation points and articulation point-related stuff
debug_show_random_path = False # shows a random active path after every process step
debug_print_zone_data = False # shows zone information in excel format (tab-separated)

# choice of algorithm (currently does nothing)
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

import time, datetime, requests, random, importlib, pickle
if debug_print_zone_data:
    maxdistance = 0
else:
    maxdistance = speed * int(input("Time in minutes:\n> "))
time_at_start = time.time()

# import and enumerate data 
try:
    data = importlib.import_module("data_" + data_set)
except ModuleNotFoundError:
    quit(print("ERROR: data_" + data_set + ".py not found"))
zid = {}
zname = {}
for i, zone in enumerate(data.zlist + data.clist): # generate numerical ids for zones
    zid[zone] = i
    zname[i] = zone
zlist = [zid[zone] for zone in data.zlist]
clist = [zid[zone] for zone in data.clist]
defined_zones = zlist + clist
start_zone = zid[data.start_zone]
end_zone = zid[data.end_zone]
blacklist = [zid[zone] for zone in data.blacklist]
whitelist = data.whitelist
connections = [(zid[z1], zid[z2], d) for z1, z2, d in data.connections]

# check validity
if start_zone not in defined_zones:
    quit(print("ERROR: Start zone is invalid"))
if end_zone not in defined_zones:
    quit(print("ERROR: End zone is invalid"))
for zone in blacklist:
    if zone not in defined_zones:
        print("WARNING: Blacklist contains invalid zone name: " + zone)
for zone1, zone2, _ in connections:
    if zone1 not in defined_zones:
        print("WARNING: Connection contains invalid zone name: " + zone1)
    if zone2 not in defined_zones:
        print("WARNING: Connection contains invalid zone name: " + zone2)

# converts an ISO8601 time format string to seconds (since epoch, probably? doesn't matter)
def str2time(s):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").timestamp()

# converts a list of zone ids to a list of zone names
def znames(zidlist):
    return [zname[zone] for zone in zidlist]
# the same but for dictionary keys
def znamed(ziddict):
    return {zname[zone]: ziddict[zone] for zone in ziddict}

# get round info with the turf API (specifically, how many hours are left)
try:
    rounds = requests.get("http://api.turfgame.com/v4/rounds").json()
    for month in rounds: # loop until the current round is found
        start_time = str2time(month["start"])
        if start_time > time.time():
            break
    round_hours_left = (start_time - time.time()) / 3600
    has_connection = True
except requests.exceptions.ConnectionError: # no wifi :)
    has_connection = False
    round_hours_left = 1000 # should be big enough to never matter (which is what we want here)








### PREPARE ZONES

# calculate zone points from the turf API (or if no connection, from the backup file)
if debug_print_zone_data == True: # debug
    if not has_connection:
        quit(print("ERROR: Can't print zone data without a connection"))
    print("name\tage\tpotential days\tpts on take\tpts per hour\tpts total\ttake age\trevisit pts\tneutral pts")
    zone_datas = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zname[zone]} for zone in zlist]).json()
    for i, zone_data in enumerate(zone_datas):
        zone = zlist[i]
        line = [zname[zone]]
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
        except KeyError: # no currentOwner - gives neutral bonus instead
            line.append("")
            line.append("")
            line.append(50)
        line = [str(x) for x in line]
        print("\t".join(line).replace(".",","))
    quit()
elif has_connection: # not debug
    zone_datas = requests.post("http://api.turfgame.com/v4/zones", json=[{"name": zname[zone]} for zone in zlist]).json()
    zone_points = {}
    for i, zone_data in enumerate(zone_datas):
        zone = zlist[i]

        hours_existed = (time.time() - str2time(zone_data["dateCreated"])) / 3600
        potential_hours = min(hours_existed / zone_data["totalTakeovers"], round_hours_left) # average hours before the zone is lost
        zone_points[zone] = int(zone_data["takeoverPoints"] + potential_hours * zone_data["pointsPerHour"])
        # if currentOwner is yourself, give revisit points if over 23 hours ago
        # give neutral points if no currentOwner
        if "currentOwner" in zone_data and zone_data["currentOwner"]["name"] == username:
                hours_since_taken = (time.time() - str2time(zone_data["dateLastTaken"])) / 3600
                if hours_since_taken > 23:
                    zone_points[zone] = int(zone_data["takeoverPoints"] / 2)
                else:
                    zone_points[zone] = 0
        else: # no currentOwner - gives neutral bonus instead
            zone_points[zone] += 50
    for zone in clist: # crossings don't give points
        zone_points[zone] = 0
    with open(dumpname + ".pk", "wb") as file:
        pickle.dump(zone_points, file)

# no connection, use backup file to get zone points instead
else:
    try:
        with open(dumpname + ".pk", "rb") as file:
            dump = pickle.load(file)
    except FileNotFoundError:
        quit(print("ERROR: No connection, no backup file found"))
    
    print("WARNING: No connection, loading backup file")
    with open(dumpname + ".pk", "rb") as file:
        zone_points = pickle.load(file)
    for zone in clist:
        zone_points[zone] = 0
    for zone in zlist:
        if zone not in zone_points:
            zone_points[zone] = 0

# collect all zones (and their connections)
zones = {}
if whitelist:
    for zone in zone_points:
        if zone in blacklist:
            zones[zone] = []
else:
    for zone in zone_points:
        if zone not in blacklist:
            zones[zone] = []
for zone1, zone2, length in connections:
    if zone1 in zones and zone2 in zones:
        zones[zone1].append((zone2, length))
        zones[zone2].append((zone1, length))

# filter out (kill) zones that can't be reached from start_zone
if blacklist:
    kill_list = list(zones.keys())
    def survive(zone):
        kill_list.remove(zone)
        for neighbor, _ in zones[zone]:
            if neighbor in kill_list:
                survive(neighbor)
    survive(start_zone)
    if end_zone in kill_list:
        quit(print("\nERROR: No possible paths found through non-blacklisted zones"))
    print("Unreachable zones were deleted: " + ", ".join(znames(kill_list)))
    for zone in list(zones.keys()): # remake zones without these unreachable zones
        if zone in kill_list:
            del zones[zone]
        zones[zone] = []
    for zone1, zone2, length in connections:
        if zone1 in zones and zone2 in zones:
            zones[zone1].append((zone2, length))
            zones[zone2].append((zone1, length))








### PRE-CALCULATIONS

# the fastest path from every zone to every other zone
fastest_path_between = {}
# the length of that path
zone_distance_between = {}

# fill out above dictionaries
for endzone in zones:
    endpaths = []
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
        if not endpaths:
            break
    # collects the information in the big dictionaries
    zone_distance_between[endzone] = endzonedistance
    fastest_path_between[endzone] = endzonepathto

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
get_artipoints(start_zone, 0)

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
    print(znames(artipoints), znames(arti3points), znamed(block_amount), sep="\n")
if debug_central_zones == True:
    tl = []
    for startzone in zone_distance_between:
        c = 0
        for endzone in zone_distance_between[startzone]:
            c += zone_distance_between[startzone][endzone]
        tl.append([c, startzone])
    tl.sort(key = lambda x:x[0])
    print("\nMost central zone: " + zname[tl[0][1]] + "\nMost isolated zone: " + zname[tl[-1][1]])
if debug_show_zone_points == True:
    print("\nZone points:")
    print(dict(sorted(znamed(zone_points).items(), key=lambda x:x[1], reverse=True)))

if maxdistance == 0: # no reason to even start the loop if this is the case
    quit(print("ERROR: Distance is zero, aborting"))
# initialize paths! let's go!
paths = [[0, zone_points[start_zone], start_zone, 0, start_zone]]








### PROCESS

print("\nStartup took " + str(round(time.time() - time_at_start, 2)) + " seconds\n")
time_at_start = time.time()
# a path is defined as: 
# [path distance, path points, last point giving zone visited, distance gone since it was visited, zone 0, zone 1, zone 2...]
finished_paths = []
best_points = 0 # finished paths are only accepted if they have the most points out of all finished paths so far
step = 1
# helper function gets the distance between four zones (minus the distance between zone2 and zone3, not needed for this)
def distance_between(zone1, zone2, zone3, zone4):
    return zone_distance_between[zone1][zone2] + zone_distance_between[zone3][zone4]

while True:
    toadd = []
    for path in paths:
        last_zone = path[-1]
        last2_zone = path[-2]
        last3_zone = path[-3]
        old_distance = path[0]
        points = path[1]
        last_captured_zone = path[2]
        last_captured_distance = path[3]
        path_zones = path[4:]
        for new_zone, new_distance in zones[last_zone]:
            distance = old_distance + new_distance
            new_zone_gives_points = zone_points[new_zone] != 0 and new_zone not in path_zones

            # and now, some optimizations!
            # if one of these situations happen it means that there (probably) exists another, better path, and this path is removed

            # PROBLEM: it can't be finished without exceeding the time limit
            if maxdistance - distance < zone_distance_between[end_zone][new_zone]:
                continue
            # PROBLEM: it returns to a zone without visiting any point-giving zones
            if new_zone == last_captured_zone:
                continue
            # PROBLEM: it hasn't taken the fastest path to the new zone
            if new_zone_gives_points and last_captured_distance + new_distance > zone_distance_between[last_captured_zone][new_zone]:
                continue
            # PROBLEM: it uses the same connection in the same direction twice
            used_connections = zip(path_zones, path_zones[1:])
            if (last_zone, new_zone) in used_connections:
                continue
            if new_zone in path_zones and new_zone != end_zone: # if it returns to a zone
                # PROBLEM: the new zone has been visited three times
                if path_zones.count(new_zone) > 1 and new_zone not in arti3points:
                    continue
                # PROBLEM: it doesn't return to the zone via the connection it left it with
                if (new_zone, last_zone) not in used_connections and new_zone not in artipoints:
                    continue
            if len(path) >= 7: # if it has visited 4+ zones including the new zone
                # PROBLEM: visiting the last four zones in another order would have been faster
                if distance_between(last3_zone, last2_zone, last_zone, new_zone) > distance_between(last3_zone, last_zone, last2_zone, new_zone):
                    continue

            if new_zone_gives_points:
                toadd.append([distance, points + zone_points[new_zone], new_zone, 0] + path_zones + [new_zone])
            else:
                toadd.append([distance, points, last_captured_zone, last_captured_distance + new_distance] + path_zones + [new_zone])
        if last_zone == end_zone and points >= best_points:
            best_points = points
            finished_paths.append(path)

    del paths
    paths = toadd
    if paths == []: # if all paths are finished
        break
    if debug_show_random_path:
        p = random.choice(paths)
        print(p[:4] + znames(p[4:]))

    print("At step " + str(step) + " there were " + str(len(paths)) + " active paths and " + str(len(finished_paths)) + " finished")
    step += 1
if len(finished_paths) == 0:
    quit(print("\nERROR: No possible paths found"))








### CLEANUP

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
    used_connections = []
    for path in finished_paths:
        for connection in zip(path[2:], path[3:]):
            if connection not in used_connections:
                used_connections.append(set(connection))
    
    # gathers all connections not in used_connections
    unused_connections = []
    for zone in zones:
        for neighbor, _ in zones[zone]:
            connection = {zone, neighbor}
            if connection not in used_connections and connection not in unused_connections:
                unused_connections.append(connection)
    unused_connections = [tuple(znames(sorted(list(x)))) for x in unused_connections]
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
            "-".join([zname[zone].upper() for zone in path[2:] if zone in zlist])))

# write the result
print("\nBest path:")
best = finished_paths[0]
best_zones = []
for i, zone in enumerate(best[2:], start=2):
    if zone in zlist and zone not in best[2:i]:
        best_zones.append(zname[zone].upper())
print("{} points, {} zones, {} min: {}\n\nTechnical representation:\n{}\n\nThe process took {} seconds".format(
    str(round(best[1], 1)),
    str(len(best_zones)),
    str(int(best[0] / speed)),
    "-".join(best_zones),
    str(best[:2] + znames(best[2:])),
    str(round(time.time() - time_at_start, 2))))
