import folium
import pandas

#Create map object
m = folium.Map(location= [39.11417, -94.62746], zoom_start = 5, tiles="openstreetmap")

#Lettura dati da Volcanons.txt
v_df=pandas.read_csv("Volcanoes.txt")
lat = list(v_df["LAT"])
lon = list(v_df["LON"])
name = list(v_df["NAME"])
elev = list(v_df["ELEV"])

def height2color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "orange"
    else:
        return "red"

fgs = []

for (lt, ln, n, el) in zip(lat, lon, name, elev):
    fg = folium.FeatureGroup(name=n, show=False).add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup= n + "\nm. " + str(el),
        fill_color=height2color(el),
        color="grey",
        fill_opacity=0.7))
    fgs.append(fg)

for fg in fgs:
    m.add_child(fg)

m.add_child(folium.LayerControl())
#Generate Map
m.save("map_leg.html")
