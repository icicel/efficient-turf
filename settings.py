
# debug
debug_unused_connections = False # shows all connections that weren't used by any fastest path
debug_central_zones = False # shows what zones are the most and least central
debug_show_zone_points = False # shows the zone points dictionary
debug_show_connections = False # shows the connections dictionary
debug_show_artipoints = False # shows articulation points and articulation point-related stuff
debug_show_random_path = False # shows a random active path after every process step
debug_print_zone_data = False # shows zone information in excel format (tab-separated)

# attempts to remove crossing zones in post by combining connections
remove_crossings = False

# the algorithm is disallowed from returning to a zone after already having visited it
# improves speed substantially but produces less optimal routes
no_revisit = False

# separate file (data/*.py) containing data such as zone names, connections, start_zone/end_zone zone etc.
# check data/template.py for examples
data_set = "template"

# where to get zones and connections from
# data - from the data file
# csv - from csv files (csv/*_c.csv, csv/*_z.csv, csv/*_con.csv) imported from google my maps
import_source = "data"

# m/min, used to convert distances to time
turfing_speed = 64

# turf username
username = "icicle"

# backup file name (*.pk)
dumpname = "turf"
