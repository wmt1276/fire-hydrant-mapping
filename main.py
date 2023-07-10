import geopandas
import matplotlib.pyplot as plt

def plot(threshold, gs, base, layer):
    buffer = gs.buffer(threshold[0])
    return buffer.plot(ax = base, color=threshold[1], zorder = layer)

def main():
    roads = geopandas.read_file("data/tl_rd22_18145_roads")
    roads.to_crs("26916", inplace = True)
    
    hydrants = geopandas.read_file("data/agency11634_locations_1688920154565.csv")
    hydrant_geometries = geopandas.GeoDataFrame(
        hydrants, geometry=geopandas.points_from_xy(hydrants.lon, hydrants.lat), crs="WGS 84"
    )
    hydrant_geometries.to_crs("26916", inplace = True)
    hydrant_series = hydrant_geometries.centroid
    
    thresholds = [[304.8, 'yellow'], [152.4, 'red']]
    
    layers = len(thresholds)
    base = roads.plot(color="gray", zorder=layers)
    for threshold in range(layers):
        base = plot(thresholds[threshold], hydrant_series, base, threshold)

    plt.show()

if __name__ == "__main__":
    main()