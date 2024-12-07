import requests

def test_geo_search():
    geo_search_url = "https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=37.786971|-122.399677&gsradius=10000&format=json"
    
    try:
        # Send the request to the API
        response = requests.get(geo_search_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx, 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Access the 'geosearch' results safely
        geo_search_results = data.get('query', {}).get('geosearch', [])
        
        if geo_search_results:
            print("Geo Search Endpoint:")
            print("Geo Search Results:")
            for result in geo_search_results:
                title = result.get('title', 'No Title')
                lat = result.get('lat', 'No Latitude')
                lon = result.get('lon', 'No Longitude')
                print(f"Title: {title}, Latitude: {lat}, Longitude: {lon}")
            print("Status: Success\n")
        else:
            print("Geo Search Endpoint:")
            print("Error: No geosearch results found\n")
    
    except requests.exceptions.RequestException as e:
        print("Geo Search Endpoint:")
        print(f"Error: {e}\n")

if __name__ == "__main__":
    test_geo_search()
