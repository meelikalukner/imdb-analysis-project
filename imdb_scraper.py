from sqlalchemy import create_engine, MetaData, Table, insert
import requests
from bs4 import BeautifulSoup

# Defining constants: user-agent for transparency and the URL I want to scrape
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; IMDBScraper/1.0; +https://github.com/meelikalukner; mailto:meelikalukner@gmail.com)'
}
URL = 'https://www.imdb.com/chart/top/'
DATABASE_FILE = r"sqlite:///D:\Meelika\Proge\imdb analysis project\imdb_data.db"

# Establishing connection to the database and loading the schema of the table
engine = create_engine(DATABASE_FILE) 
metadata = MetaData()

# Load an existing table 'movies' from the metadata of the engine
movies = Table('movies', metadata, autoload_with=engine)

# Scraping logic
def scrape_imdb(url):
    response = requests.get(url, headers=HEADERS)
    #print(response.status_code) #Checking the status code I get with response
    #print(response.encoding) #Checking the encoding of the page
    #print(response.text[:1000]) #Checking the response text
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify()) #Checking soup object
    movie_details = []

    for movie_div in soup.select('div.sc-b85248f1-0'):
        title = movie_div.select_one('h3.ipc-title__text').text.strip() #Finding the movie title
        spans = movie_div.select('span.sc-b85248f1-6') #Finding spans where is the info about year, duration, rating and imdb rating
    
        if len(spans) < 3:  # Check if there are less than three spans
            print(f"Skipped movie: {title} due to insufficient data.")
            continue
        
        year = spans[0].text.strip()
        duration = spans[1].text.strip()
        rating = spans[2].text.strip()
        imdb_rating = float(movie_div.select_one('span.ipc-rating-star.ipc-rating-star--base').text.strip())

        movie_details.append({ #Creates a dictionary from the scraped data
            "title": title,
            "year": int(year),
            "duration": duration,
            "rating": rating,  
            "IMDB rating": imdb_rating
        })

    return movie_details

# Adds scraped movie data to the SQLite database
def add_data_to_db(data, engine):
    with engine.connect() as conn:
        try:
            conn.execute(insert(movies), data)
            print(f"Inserted {len(data)} movies into the database.")
            conn.commit()
        except Exception as e:
            print(f"Error inserting into database: {e}")

#Main execution
if __name__ == "__main__":
    data = scrape_imdb(URL)
    add_data_to_db(data,engine)