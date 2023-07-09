import geopandas
import matplotlib.pyplot as plt


gdf = geopandas.read_file("data/export.geojson")

print(gdf)

gdf.plot()
plt.show()