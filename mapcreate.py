import folium
import pandas as pd

# Load your dataset (replace 'your_file.csv' with your actual file)
df = pd.read_csv("data/DeltaCAN_Dataset.csv")

# Define the latitude and longitude range for the Mackenzie Delta region
mackenzie_lat_min, mackenzie_lat_max = 67.0, 69.5
mackenzie_lon_min, mackenzie_lon_max = -137.0, -132.0

# Filter the dataset for locations within the Mackenzie Delta region
mackenzie_delta_data = df[
    (df["Latitude"] >= mackenzie_lat_min) & (df["Latitude"] <= mackenzie_lat_max) &
    (df["Longitude"] >= mackenzie_lon_min) & (df["Longitude"] <= mackenzie_lon_max)
]

# Define the center of the map based on the mean coordinates
map_center = [mackenzie_delta_data["Latitude"].mean(), mackenzie_delta_data["Longitude"].mean()]

# Create a folium map
m = folium.Map(location=map_center, zoom_start=7, tiles="CartoDB Positron")

# Add points to the map
for _, row in mackenzie_delta_data.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        popup=f"Delta ID: {row['Delta ID']}"
    ).add_to(m)

# Save the map as an HTML file
m.save("mackenzie_delta_map.html")

print("Map saved as 'mackenzie_delta_map.html'. Open this file in a web browser to view it.")
