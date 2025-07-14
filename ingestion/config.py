import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

db_url = URL.create(
    os.getenv("DB_KIND"),
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME")
)

path_base = 'https://datasets.imdbws.com/'
files = [
            'name.basics.tsv',
            'title.akas.tsv',
            'title.basics.tsv',
            'title.crew.tsv',
            'title.episode.tsv',
            'title.principals.tsv',
            'title.ratings.tsv'
        ]