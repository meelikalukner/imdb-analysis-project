# Name of the project
In this project I will scrape data from IMDB's Top 250 movies and store the data into a SQLite database.
After scraping I will conduct analysis on the data on Jupyter Notebook and visualizing the data with Tableau.

* create_database.py - a script that initializes SQLite databse
* imdb_scraper.py - a script that scrapes IMDB's Top 250 movies page and inserts the scraped data to database
* imdb_data.db - SQLite database for scraped data
* data_abalysis.ipynb - Jupyter Notebook for data analysis
* movies_sorted_by_duration.csv - a csv containing a sorted list of Top 250 movies, sorted in descending order by duration
## Setup and usage

1 . use bash and install pip and python 3.11

2 . install the virual environment
```sh
pip install virtualenv
```
3 . Create your local virtual environment for the project
```sh
virtualenv venv
```

4 . Activate the virtual environment
```sh
source venv/Scripts/activate
```

5 . Install required packages
```sh
pip install -r requirements.txt
```

6 . Run the project
```sh
python create_database.py
```
Change the path to the DATABASE_FILE to point to the one in your project and execute
```sh
python imdb_scraper.py
```

7 . Once you're done working on the project, you can deactivate the virtual environment with
```sh
deactivate
```

A good tool for writing markdown is https://markdownlivepreview.com/


## License

MIT