In this project I will scrape data from IMDB's Top 250 movies and store the data into a SQLite database.
After scraping I will conduct analysis on the data on Jupyter Notebook and visualizing the data with Tableau.

* create_database.py - a script that initializes SQLite databse
* imdb_scraper.py - a script that scrapes IMDB's Top 250 movies page and inserts the scraped data to database
* imdb_data.db - SQLite database for scraped data
* data_abalysis.ipynb - Jupyter Notebook for data analysis
* movies_sorted_by_duration.csv - a csv containing a sorted list of Top 250 movies, sorted in descending order by duration