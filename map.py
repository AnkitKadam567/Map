import folium
import pandas
import json

data=pandas.read_excel("Coord.xlsx")
LAT=list(data["lat"])
LON=list(data["lon"])
LOC=list(data["loc"])

map=folium.Map(location=[17.753181,73.1880558])
fgc=folium.FeatureGroup(name="circles")

def color_generater(k):
    if len(k)<3:
        return 'red'
    elif 3<=len(k)<5:
        return 'orange'
    else:
        return 'black'

for i,j,k in zip(LAT,LON,LOC):
    fgc.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=str(k),fill='true',
    fill_color=color_generater(k),color='grey',fill_opacity=0.7))
#map.add_child(folium.Marker(location=[coord],popup="this is marker 2",icon=folium.Icon(color='green')))

fgp=folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open("world.json",encoding='utf-8-sig').read(),
style_function=lambda x :{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'green' if 10000000<=x['properties']['POP2005']<=20000000 else 'red'}))
#fg.add_child(folium.GeoJson(open('world.json')))

map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map5.html")
