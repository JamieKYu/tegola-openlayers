import mapbox_vector_tile
import requests
import json

def fetch_and_decode_tile(z, x, y):
    # Construct the tile URL
    url = f"https://maps.theyuzone.com/maps/world/{z}/{x}/{y}.pbf"

    # Fetch the tile
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch tile: HTTP {response.status_code}")
        return

    tile_data = response.content

    # Decode the tile
    decoded_tile = mapbox_vector_tile.decode(tile_data)

    # Print the decoded tile in a readable JSON format
    print(json.dumps(decoded_tile, indent=2))

# Example usage
if __name__ == "__main__":
    # Accept z, x, y as input values
    z = int(input("Enter zoom level (z): "))
    x = int(input("Enter tile column (x): "))
    y = int(input("Enter tile row (y): "))

    # Fetch and decode the tile
    fetch_and_decode_tile(z, x, y)
