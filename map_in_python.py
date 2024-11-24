
# from IPython.display import display
import folium
import webbrowser


map_center = [12.9716, 77.5946]
my_map = folium.Map(location = map_center, zoom_start = 15)

folium.Marker([12.9716, 77.5946],
              popup= "Bangalore, India",
              icon= folium.Icon(color="blue", icon="info-sign")).add_to(my_map)
# display(my_map)

file_path = "bangalore_map.html"
my_map.save(file_path)
webbrowser.open(file_path)