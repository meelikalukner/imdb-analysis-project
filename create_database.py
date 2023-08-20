from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table

DATABASE_FILE = "sqlite:///imdb_data.db"

def create_movies_table(engine):
    #Creates a 'movies' table in the database connected to the provided engine
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

if __name__ == "__main__":
    engine = create_engine(DATABASE_FILE)
    create_movies_table(engine)