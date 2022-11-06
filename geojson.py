import json

input_file=json.load(open("./data/places.json", "r", encoding="utf-8"))

geojs={
     "type": "FeatureCollection",
     "features":[
           {
                "type":"Feature",
                "geometry": {
                "type":"LineString",
                "coordinates":d["geojson"]["coordinates"],
            },
                "properties":d,

         } for d in input_file
    ]
 }

output_file=open("./data/geodata.json", "w", encoding="utf-8")
json.dump(geojs, output_file)


output_file.close()
