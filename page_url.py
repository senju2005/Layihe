import requests

def test_page_url():
    page_url = "https://en.wikipedia.org/w/api.php?action=query&titles=NASA&prop=info&inprop=url&format=json"
    
    try:
        # Send request to the API
        response = requests.get(page_url)
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        
        # Parse the response JSON
        data = response.json()
        
        # Access the 'pages' part safely
        pages = data.get('query', {}).get('pages', {})
        
        if pages:
            # Get the page ID from the dictionary
            page_id = list(pages.keys())[0]
            page_info = pages.get(page_id, {})
            
            # Extract the full URL of the page
            page_url = page_info.get('fullurl', 'No URL found')
            print("Page URL Endpoint:")
            print("Page URL:", page_url)
            print("Status: Success\n")
        else:
            print("Page URL Endpoint:")
            print("Error: No pages found in response\n")
    
    except requests.exceptions.RequestException as e:
        print("Page URL Endpoint:")
        print(f"Error: {e}\n")

if __name__ == "__main__":
    test_page_url()
