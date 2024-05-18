import json
from plotly import offline
from plotly.graph_objects import Scattergeo, Layout 

filename = 'data/last_30_days.json'

with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5 * mag if mag > 0 else 0.1 for mag in mags],
        'color': mags,
        'colorscale': 'Greens',
        'reversescale': True,
        'colorbar': {'title': 'Siła'},
}, }]
my_layout = Layout(title = "Trzęsienia ziemi na świecie w ciągu ostatnich 30 dni (18.05.2024r.)", titlefont = dict(size = 30))
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')

"""
readable_data = 'data/eq_last_hour.json'

with open(readable_data) as rd:
    json.dump(all_eq_data, f, indent= 4)
"""