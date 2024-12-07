import requests

def test_suggest():
    suggest_url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=Python&format=json"
    
    try:
        # Send the request to the API
        response = requests.get(suggest_url)
        response.raise_for_status()  # Will raise an exception for 4xx/5xx errors
        
        # Parse the response JSON
        data = response.json()
        
        # Check if the response contains valid suggestions
        if len(data) >= 4:
            search_query = data[0]
            suggestions = data[1]
            descriptions = data[2]
            urls = data[3]
            
            print("Suggest Endpoint:")
            print(f"Search Query: {search_query}")
            print("Suggestions:")
            
            for title, description, url in zip(suggestions, descriptions, urls):
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"URL: {url}")
                print("-" * 40)
            
            print("Status: Success\n")
        else:
            print("Suggest Endpoint:")
            print("Error: No valid suggestions found\n")
    
    except requests.exceptions.RequestException as e:
        print("Suggest Endpoint:")
        print(f"Error: {e}\n")

if __name__ == "__main__":
    test_suggest()
