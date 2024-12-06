import requests
import sqlite3
from datetime import datetime

# Function to fetch page metadata and categories from Wikipedia API
def fetch_page_metadata(page_title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page_title}&prop=info|categories&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pages = data.get('query', {}).get('pages', {})
        
        for page_id, page_info in pages.items():
            title = page_info.get('title', 'N/A')
            fullurl = page_info.get('fullurl', 'N/A')
            
            # Get categories (if available)
            categories = [category['title'] for category in page_info.get('categories', [])]
            return title, fullurl, categories
    else:
        print(f"Error: Unable to fetch metadata for {page_title}")
        return None, None, []

# Function to generate HTML report
def generate_html_report(title, url, categories, page_title):
    # Create HTML content for the report
    html_content = f"""
    <html>
    <head>
        <title>Wikipedia API Test Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #5f6368;
            }}
            .report-container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 800px;
                margin: 0 auto;
            }}
            .section {{
                margin-bottom: 20px;
            }}
            .section h2 {{
                color: #444;
            }}
            .section p {{
                font-size: 14px;
                line-height: 1.5;
            }}
            .categories ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            .categories li {{
                margin: 5px 0;
            }}
            footer {{
                text-align: center;
                color: #888;
                font-size: 12px;
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <h1>Wikipedia API Test Report</h1>
        <div class="report-container">
            <div class="section">
                <h2>Page Information</h2>
                <p><strong>Title:</strong> {title}</p>
                <p><strong>URL:</strong> <a href="{url}" target="_blank">{url}</a></p>
            </div>
            <div class="section categories">
                <h2>Categories</h2>
                <ul>
    """
    
    # Add categories to the HTML
    if categories:
        for category in categories:
            html_content += f"<li>{category}</li>"
    else:
        html_content += "<li>No categories found</li>"

    # Closing HTML tags
    html_content += f"""
                </ul>
            </div>
            <footer>
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </footer>
        </div>
    </body>
    </html>
    """

    # Save the HTML report to a file
    with open(f"wikipedia_report_{page_title}.html", "w") as report_file:
        report_file.write(html_content)

    print(f"Report for '{page_title}' has been generated and saved as 'wikipedia_report_{page_title}.html'")

# Main function to fetch data and generate the report
def main():
    # Define the page title you want to fetch
    page_title = "Python_(programming_language)"  # You can change this to any Wikipedia page title

    # Fetch page metadata and categories from Wikipedia API
    title, url, categories = fetch_page_metadata(page_title)

    if title and url:
        # Generate the HTML report
        generate_html_report(title, url, categories, page_title)
    else:
        print("Failed to fetch or save page metadata.")

# Run the script
if __name__ == "__main__":
    main()
