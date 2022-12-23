

### Wtf is a turf...

(from turfgame.com)  
Turf is a location-based game using GPS technology, which requires you to go to the physical location of the virtual zones in order to take them. Try to take as many zones as you can to rack up points, earn medals, level up and climb the leaderboards!

### Ok but what does this even do?!

This, thing, calculates the route between two zones which gets you the most possible points, while not exceeding the given time limit.

---

# How to use

(Imagine your input method being so convoluted that you need to write a tutorial specifically so your fancy little program could potentially be used by someone other than yourself. Couldn't be me.)

## Basics

In order to generate a route, Turf zones are treated as nodes on a graph, with edges (**connections**) having weights according to their length in the real world.  
Of course, Turf zones don't correspond as well to a proper graph as we'd like, and so we also have to define **crossings** - custom, non-point giving, purely functional zones - to keep the amount of edges in control.  

The zones, crossings and connections defined in the template files correspond to this map of southern Stenungsund, Sweden: https://www.google.com/maps/d/u/0/edit?mid=1iv00_Yvkj4J3LrPsgByOfHsf2090pNg

## The data file

This file is located at data/[data_set].py, with [data_set] being defined in settings.py. It contains information like defined zones, crossings, connections between zones, start and end zone, and other stuff.

If you, for some reason, want to actually use this tool for yourself you can just copy the template and edit the data.

## Import from CSV files

By setting import_source in settings to "csv", you can import zones, crossings and connections from Google My Maps instead of having to input them manually in the data file!

In My Maps, create one layer for zones, one for crossings and one for connections. Create zones and crossings using **markers** and connections using **lines**. Then, export each layer through *Layer options → Export data → CSV*. Rename the zones file to [data_set]_z.csv, crossings to [data_set]_c.csv and connections to [data_set]_con.csv, then put them all in csv/. Should be ready to use!  
(The zones, crossings and connections defined in [data_set].py are ignored when using this method.)

Tip: Using https://turf.urbangeeks.org/ you can export Turf zones to My Maps. Draw a polygon containing all relevant zones, and then *Download polygon as → KML - POIs* (or *KML - Zone polygons* for the actual zone shapes).  
Then in My Maps you can either 1. create a new layer and import this KML file into it, or 2. in an already existing layer, go to *Layer options → Reimport and merge → Add more items* and import the KML file there.