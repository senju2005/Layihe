import requests
import sqlite3

# Function to fetch Wikipedia suggestions
def fetch_suggestions(query):
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=5&namespace=0&format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# Function to save suggestions to SQLite database
def save_suggestions_to_db(query, suggestions, descriptions, urls):
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('wikipedia_suggestions.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suggestions (
            query TEXT,
            suggestion_title TEXT,
            description TEXT,
            url TEXT
        )
    ''')
    # Insert each suggestion into the table
    for title, description, url in zip(suggestions, descriptions, urls):
        cursor.execute('''
            INSERT INTO suggestions (query, suggestion_title, description, url)
            VALUES (?, ?, ?, ?)
        ''', (query, title, description, url))
    
    # Commit and close the database connection
    conn.commit()
    conn.close()

# Main function to orchestrate the request and saving
def main():
    search_query = "python"
    data = fetch_suggestions(search_query)
    
    if data:
        # Extract the results from the API response
        query = data[0]  # The search query itself
        suggestions = data[1]
        descriptions = data[2]
        urls = data[3]
        
        # Save the data to the database
        save_suggestions_to_db(query, suggestions, descriptions, urls)
        print("Data saved successfully!")

if __name__ == "__main__":
    main()
