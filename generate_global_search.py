import os
import json

data_dir = os.getcwd() + '/data/'

file_list = [
  "authors",
  "essay",
  "countries",
  "languages"
]

data_store = []

for i in range(len(file_list)) :
  file_name = file_list[i] + ".json"

  data = None
  with open(data_dir + file_name) as f:
    data = json.load(f)

  if file_list[i] == "authors" :
    for author in data :
      data_store.append({
        "flavorText" : data[author]["Author"],
        "id" : data[author]["author_id"],
        "type" : "author"
      })
  elif file_list[i] == "essay" :
    for author_id in data :
      for a in range(len(data[author_id])) :
        data_store.append({
          "flavorText" : data[author_id][a]["Title"],
          "type" : "essay"
        })
  elif file_list[i] == "countries" :
    for country in data :
      data_store.append({
        "flavorText" : country,
        "type" : "country"
      })
  elif file_list[i] == "languages" :
    for language in data :
      data_store.append({
        "flavorText" : language,
        "type" : "language"
      })

json_data = json.dumps(data_store, indent=2)
with open(data_dir + "global_data.json", "w") as output:
  output.write(json_data)