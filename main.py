import geopandas
import pandas
import matplotlib.pyplot as plt

def plot(threshold, gs, base, layer):
    envelope = gs.buffer(threshold[0])
    return envelope.plot(ax = base, color=threshold[1], zorder = layer)

def main():
    roads = geopandas.read_file("data/tl_rd22_18145_roads")
    roads.to_crs("26916", inplace = True)
    
    active_911_hydrants = geopandas.read_file("data/agency11634_locations_1688920154565.csv")
    active_911_hydrant_geometries = geopandas.GeoDataFrame(
        active_911_hydrants, geometry=geopandas.points_from_xy(active_911_hydrants.lon, active_911_hydrants.lat), crs="WGS 84"
    )
    active_911_hydrant_geometries.to_crs("26916", inplace = True)
    active_911_series = active_911_hydrant_geometries.centroid
    
    osm_hydrants = geopandas.read_file("data/export.geojson")
    osm_hydrants.to_crs("26916", inplace = True)
    osm_series = osm_hydrants.geometry
    hydrant_series = pandas.concat([active_911_series, osm_series])
    
    print(hydrant_series)
    
    thresholds = [[304.8, 'yellow'], [152.4, 'red']]
    
    layers = len(thresholds)
    base = roads.plot(color="gray", zorder=layers)
    for threshold in range(layers):
        base = plot(thresholds[threshold], hydrant_series, base, threshold)
        
    plt.xlim([590100, 602969])
    plt.ylim([4375357, 4386894])
    plt.show()

if __name__ == "__main__":
    main()