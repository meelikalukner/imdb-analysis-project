from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
import requests
from bs4 import BeautifulSoup

#Defining constants: user-agent for transparency, URL I want to scrape and my database file
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; IMDBScraper/1.0; +https://github.com/meelikalukner; mailto:meelikalukner@gmail.com)'
}
URL = 'https://www.imdb.com/chart/top/'
DATABASE_FILE = "sqlite:///imdb_data.db"

#Database configuration
engine = create_engine(DATABASE_FILE)
metadata = MetaData()

movies = Table(
    'movies',metadata,
    Column('id',Integer,primary_key=True),
    Column('title',String),
    Column('year',Integer),
    Column('duration',String),
    Column('rating',String),
    Column('IMDB rating',Float)
)

metadata.create_all(engine)

#Scraping logic
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
        title = movie_div.select_one('h3.ipc-title__text').text.strip()
        spans = movie_div.select('span.sc-b85248f1-6')
    
        if len(spans) < 3:  # Check if there are less than three spans
            print(f"Skipped movie: {title} due to insufficient data.")
            continue
        
        year = spans[0].text.strip()
        duration = spans[1].text.strip()
        other_rating = spans[2].text.strip()
        imdb_rating = float(movie_div.select_one('span.ipc-rating-star.ipc-rating-star--base').text.strip())

        movie_details.append({
            "title": title,
            "year": int(year),
            "duration": duration,
            "rating": other_rating,  
            "IMDB rating": imdb_rating
        })

    return movie_details

#Main execution
if __name__ == "__main__":
    data = scrape_imdb(URL)
    #print(data)
    #Inserting data to database
    with engine.connect() as conn:
        for movie in data:
            conn.execute(movies.insert(), movie)