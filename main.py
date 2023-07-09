import geopandas
import matplotlib.pyplot as plt

def plot(threshold, gs, base):
    buffer = gs.buffer(threshold[0])
    return buffer.plot(ax = base, color=threshold[1])

def main():

    hydrants = geopandas.read_file("data/agency11634_locations_1688920154565.csv")
    hydrant_geometries = geopandas.GeoDataFrame(
        hydrants, geometry=geopandas.points_from_xy(hydrants.lon, hydrants.lat), crs="WGS 84"
    )
    hydrant_geometries.to_crs("26916", inplace = True)
    hydrant_series = hydrant_geometries.centroid
    
    base = None
    thresholds = [[304.8, 'yellow'], [152.4, 'red']]
    for threshold in thresholds:
        base = plot(threshold, hydrant_series, base)

    plt.show()

if __name__ == "__main__":
    main()