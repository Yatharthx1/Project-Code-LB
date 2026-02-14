import osmnx as ox

def compute_route(G, origin_lat, origin_lon, dest_lat, dest_lon):
    origin_node = ox.distance.nearest_nodes(G, origin_lon, origin_lat)
    dest_node = ox.distance.nearest_nodes(G, dest_lon, dest_lat)

    route = ox.shortest_path(G, origin_node, dest_node, weight="base_time")

    total_time = 0
    total_distance = 0

    for i in range(len(route) - 1):
        u = route[i]
        v = route[i + 1]

        edge_data = G.get_edge_data(u, v)
        first_edge = list(edge_data.values())[0]

        total_time += first_edge["base_time"]
        total_distance += first_edge["length"]

    return {
        "route": route,
        "distance_km": round(total_distance / 1000, 2),
        "time_min": round(total_time, 2)
    }
