import requests

def test_page_title():
    page_title_url = "https://en.wikipedia.org/w/api.php?action=query&titles=NASA&format=json"
    response = requests.get(page_title_url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            # Extract the first page's title, if it exists
            if pages:
                page_title = list(pages.values())[0].get('title', 'No title found')
                print("Page Title Endpoint:")
                print("Page Title:", page_title)
                print("Status: Success\n")
            else:
                print("Page Title Endpoint:")
                print("Error: No pages found in response\n")
        except Exception as e:
            print(f"Error parsing the response: {e}")
    else:
        print("Page Title Endpoint:")
        print(f"Status: Error - {response.status_code} {response.reason}\n")

if __name__ == "__main__":
    test_page_title()
