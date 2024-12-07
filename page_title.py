import requests

def test_page_title():
    page_title_url = "https://en.wikipedia.org/w/api.php?action=query&titles=NASA&format=json"
    try:
        response = requests.get(page_title_url)
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Check if 'pages' exists in the response
        pages = data.get('query', {}).get('pages', {})
        
        if pages:
            page_title = list(pages.values())[0].get('title', 'No title found')
            print("Page Title Endpoint:")
            print("Page Title:", page_title)
            print("Status: Success\n")
        else:
            print("Page Title Endpoint:")
            print("Error: No pages found in response\n")
    
    except requests.exceptions.RequestException as e:
        print("Page Title Endpoint:")
        print(f"Error: {e}\n")

if __name__ == "__main__":
    test_page_title()
