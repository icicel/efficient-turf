
# list of regular zones
zone_list = ["campingpiren", "surfview", "nösnäsån", "gulzon", "bathview", "nösnäsbacken", "hallernazon", "kozon",
         "genomskogen", "sneezenose", "dragkamp", "inklämdpågräs", "solgårdsstig", "husarrondell", "movedwindmill",
         "kvarnskogen", "stenryttare", "kvarntäppan", "trädväg", "liteskogbara", "hasselbacke", "frispel", "tullaull",
         "yttreucklums", "ucklumcykel", "kringelikrok", "norumskyrka", "jansvy", "bakomängen", "torpzone", "sköntgrönt",
         "motfurufjäll", "gamlahallerna", "odlamedcykel"]

# list of crossing zones
crossing_list = ["k-klassrum", "k-nösnäs", "k-gymnasiet", "k-backen", "k-ucklum", "k-hallerna", "k-solgård", "k-kristinedal",
         "k-camping", "k-kvarnberg", "k-skogsbryn", "k-älvhem", "k-strandnorum", "k-tuvull", "k-kyrkenorum"]

# start and end zone
start_zone = "k-klassrum"
end_zone = "k-gymnasiet"

# blacklist certain zones (the algorithm can't use them for paths)
blacklist = []
# convert above to a whitelist (the algorithm can ONLY use them for paths)
is_whitelist = False

# list of zones that MUST be visited
prioritylist = []

# connections between zones as (zone 1, zone 2, length in meters)
connections = [
    ("campingpiren", "k-camping", 370),
    ("surfview", "k-camping", 280),
    ("k-camping", "nösnäsån", 730),
    ("nösnäsån", "gulzon", 370),
    ("gulzon", "bathview", 480),
    ("nösnäsån", "k-nösnäs", 100),
    ("k-nösnäs", "nösnäsbacken", 580),
    ("nösnäsbacken", "hallernazon", 620),
    ("hallernazon", "k-hallerna", 530),
    ("k-hallerna", "kozon", 330),
    ("k-hallerna", "genomskogen", 330),
    ("k-backen", "genomskogen", 330),
    ("genomskogen", "sneezenose", 540),
    ("sneezenose", "nösnäsbacken", 540),
    ("sneezenose", "k-gymnasiet", 80),
    ("k-nösnäs", "k-gymnasiet", 430),
    ("k-gymnasiet", "k-klassrum", 130),
    ("k-klassrum", "k-backen", 120),
    ("k-ucklum", "k-gymnasiet", 260),
    ("k-nösnäs", "k-solgård", 330),
    ("k-solgård", "dragkamp", 90),
    ("k-solgård", "inklämdpågräs", 230),
    ("inklämdpågräs", "solgårdsstig", 310),
    ("solgårdsstig", "k-kristinedal", 520),
    ("k-kristinedal", "husarrondell", 150),
    ("k-kristinedal", "stenryttare", 210),
    ("inklämdpågräs", "movedwindmill", 450),
    ("movedwindmill", "k-kvarnberg", 410),
    ("k-kvarnberg", "k-skogsbryn", 200),
    ("k-skogsbryn", "kvarnskogen", 200),
    ("k-skogsbryn", "stenryttare", 150),
    ("k-skogsbryn", "liteskogbara", 290),
    ("k-kvarnberg", "kvarntäppan", 230),
    ("k-kvarnberg", "liteskogbara", 330),
    ("kvarntäppan", "k-ucklum", 280),
    ("k-ucklum", "dragkamp", 190),
    ("kvarntäppan", "trädväg", 330),
    ("k-ucklum", "trädväg", 470),
    ("trädväg", "liteskogbara", 550),
    ("liteskogbara", "hasselbacke", 440),
    ("trädväg", "hasselbacke", 470),
    ("trädväg", "k-älvhem", 280),
    ("k-älvhem", "hasselbacke", 320),
    ("hasselbacke", "frispel", 260),
    ("k-älvhem", "frispel", 430),
    ("frispel", "tullaull", 260),
    ("k-älvhem", "yttreucklums", 330),
    ("yttreucklums", "ucklumcykel", 450),
    ("yttreucklums", "k-backen", 310),
    ("kringelikrok", "ucklumcykel", 630),
    ("kringelikrok", "norumskyrka", 450),
    ("norumskyrka", "kozon", 710),
    ("yttreucklums", "k-ucklum", 550),
    ("nösnäsbacken", "k-strandnorum", 540),
    ("hallernazon", "k-strandnorum", 330),
    ("k-strandnorum", "jansvy", 390),
    ("k-strandnorum", "bakomängen", 420),
    ("jansvy", "bakomängen", 390),
    ("tullaull", "k-tuvull", 230),
    ("k-tuvull", "kringelikrok", 310),
    ("k-tuvull", "torpzone", 530),
    ("kringelikrok", "k-kyrkenorum", 270),
    ("k-kyrkenorum", "torpzone", 410),
    ("k-kyrkenorum", "sköntgrönt", 360),
    ("norumskyrka", "sköntgrönt", 620),
    ("sköntgrönt", "motfurufjäll", 360),
    ("kozon", "gamlahallerna", 590),
    ("gamlahallerna", "norumskyrka", 670),
    ("gamlahallerna", "odlamedcykel", 250)
]
