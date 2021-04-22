import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium

NYC_locs = pd.read_csv(r'C:\Users\v-dakerv\PycharmProjects\Dale_project\Geo_Spatial_data_Feb_Project\NYC AirBnB data\AB_NYC_2019.csv')
print(NYC_locs)
NYC_bnbs = NYC_locs.dropna()
print(NYC_bnbs)
plt.scatter(x = NYC_bnbs.longitude, y = NYC_bnbs.latitude, marker = '2')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('New York City AirBnBs')
plt.grid()
plt.show()

# Import ShapeFile
NYC_map = gpd.read_file(r'C:\Users\v-dakerv\PycharmProjects\Dale_project\Geo_Spatial_data_Feb_Project\GeoPandas\Borough_Boundaries\nybb.shp')
NYC_map = NYC_map.to_crs(4326)
NYC_map.plot(figsize=(10, 10), column='BoroName', cmap='Set2', legend=True)
plt.title('New York City Borough Boundaries')
print(NYC_map)

# Scatterplots over polygon
NYC_map.plot(figsize=(10, 10), column='BoroName', cmap='Set2', legend=True, legend_kwds={'loc': 'lower right'})
plt.scatter(x = NYC_bnbs.longitude, y = NYC_bnbs.latitude, marker = '2')
plt.title('New York City Airbnb Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('New York City Airbnb Locations.png')
plt.grid()
plt.show()

# GeoDataFrame
ireland = gpd.read_file(r'C:\Users\v-dakerv\PycharmProjects\Dale_project\Geo_Spatial_data_Feb_Project\GeoJSON\counties.geojson')
print(ireland.head())
ireland.plot(column = 'AREA', cmap = 'Dark2')
ireland_crs = {'init': 'espg:4326'}
ireland_geo = gpd.GeoDataFrame(ireland, crs = ireland.crs, geometry=ireland.geometry)
ireland_geo = ireland_geo.to_crs(4326)
plt.title('Republic of Ireland')
print(type(ireland_geo))
print(ireland_geo)
plt.savefig('Republic of Ireland.png', bbox_inches="tight")

# Folium
Carrauntoohil = folium.Map(location = [51.999245, -9.743611], zoomstart=4, tiles="Stamen Terrain")
folium.Marker([51.999245, -9.743611]).add_to(Carrauntoohil)
Carrauntoohil.save("Highest_Point.html")