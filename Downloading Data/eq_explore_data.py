from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
# path = Path('eq_data/readable_eq_data_4.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat = lats, lon=lons, size = mags, title = title,
        color=mags,
        color_continuous_scale='Viridis'
        labels = {'color':'Magnitude'}
        projection='natural earth',
        hover_name=eq_titles,
        )
fig.show()

# print(mags[:10])
# print(longs[:5])
# print(lats[0:5])