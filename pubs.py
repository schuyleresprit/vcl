import pandas as pd
from mapboxgl.utils import *

# Load gage data from sample csv
data_url = "data/publications.json"
df = pd.read_json(data_url)
df_json = globals()['df'].to_json(orient='split')
read_to_json = pd.read_json(df_json, orient='split')



# Convert Elevation series to float
df['Elevation (feet)'] = df['Elevation (feet)'].astype(float)

# Clean up by dropping null rows
df.dropna(axis=1, how='all', inplace=True)

# Create geojson file output
df_to_geojson(
      df.fillna(''),
      filename="cdec.geojson",
      properties=['Author', 'Descriptor' 'Genre', 'Language', 'Pub_id', 'Pubdate', 'Publisher', 'Title', 'Translation'],
      precision=9
)
{'feature_count': 5, 'filename': 'pubs.geojson', 'type': 'file'}

# Create geojson FeatureCsollection python dict saved to a variable named data
data = df_to_geojson(
      df.fillna(''),
      properties=['Author', 'Descriptor' 'Genre', 'Language', 'Pub_id', 'Pubdate', 'Publisher', 'Title', 'Translation'],
      precision=9
)
