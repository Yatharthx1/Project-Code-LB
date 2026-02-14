# import osmnx as ox
# from backend.routing.graph_builder import build_graph
# import folium





# G = build_graph()
# tags = {"highway": True}
# features = ox.features_from_place("Indore, India", tags)

# signals = features[features["highway"] == "traffic_signals"]

# print("Total highway objects:", len(features))
# print("Traffic signals found:", len(signals))
# signal_nodes = set()

# for idx, row in signals.iterrows():
#     lat = row.geometry.y
#     lng = row.geometry.x
#     node = ox.nearest_nodes(G, lng, lat)
#     signal_nodes.add(node)

# print("Unique signal nodes:", len(signal_nodes))
# for node in G.nodes:
#     G.nodes[node]["has_signal"] = False

# for node in signal_nodes:
#     G.nodes[node]["has_signal"] = True

# m = folium.Map(location=[22.7196, 75.8577], zoom_start=13)

# # Add signal markers
# for node in signal_nodes:
#     lat = G.nodes[node]["y"]
#     lng = G.nodes[node]["x"]
    
#     folium.CircleMarker(
#         location=[lat, lng],
#         radius=4,
#         color="red",
#         fill=True,
#         fill_opacity=0.8
#     ).add_to(m)

# m.save("indore_signals.html")


#--------------------------------------------------------------------------------------------------------------



from backend.signal.signal_model import SignalModel
from backend.routing.graph_builder import build_graph
from backend.routing.routing_engine import compute_route

# Build graph
G = build_graph()

# Create signal model
signal_model = SignalModel(G)

# Example coordinates
origin = (22.7196, 75.8577)
destination = (22.7450, 75.9000)

# Get route (fastest for now)
route = compute_route(origin, destination, mode="fastest")

# Analyze signals
stats = signal_model.analyze_route(route)

print("Signal Count:", stats["signal_count"])
print("Expected Stops:", stats["expected_stops"])
print("Expected Delay (sec):", stats["expected_signal_delay_sec"])
print("Expected Delay (min):", stats["expected_signal_delay_sec"] / 60)
