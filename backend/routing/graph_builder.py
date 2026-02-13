import osmnx as ox
import networkx as nx


def build_graph(place_name="Indore, Madhya Pradesh, India"):
    print(f"Downloading road network for {place_name}...")

    G = ox.graph_from_place(
        place_name,
        network_type="drive",
        simplify=True
    )

    print("Download complete.")
    print(f"Nodes: {len(G.nodes)}")
    print(f"Edges: {len(G.edges)}")

    # Add travel time attribute
    for u, v, k, data in G.edges(keys=True, data=True):
        length_m = data.get("length", 0)

        # Assume average speed = 40 km/h
        avg_speed_kmph = 40

        # Convert length to km
        length_km = length_m / 1000

        # Travel time in minutes
        if avg_speed_kmph > 0:
            travel_time_min = (length_km / avg_speed_kmph) * 60
        else:
            travel_time_min = 0

        data["base_time"] = travel_time_min

        # Default traffic factor (can vary later)
        data["traffic_factor"] = 1.0

    print("Graph prepared with base_time and traffic_factor.")

    return G
