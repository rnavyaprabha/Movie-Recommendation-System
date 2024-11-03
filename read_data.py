import os
import csv
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rec.settings')
django.setup()

from landing_page.models import Movie, Genre

def convert_to_int(value):
    if value.strip() == '':
        return None
    return int(value)

def convert_to_double(value):
    if value.strip() == '':
        return None
    return float(value)

# Function to read data from CSV and populate the database
def populate_database(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Get or create genres
            genre_names = row['Genre'].split(',')  # Split genre names by comma
            genre_objects = []
            for genre_name in genre_names:
                genre_name = genre_name.strip()  # Remove leading/trailing spaces
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                genre_objects.append(genre)
                
            # Create movie instance
            movie = Movie.objects.create(
                title=row['Series_Title'],
                director=row['Director'],
                year=row['Released_Year'],
                overview=row['Overview'],
                poster = row['Poster_Link'],
                certificate = row['Certificate'],
                runtime = row['Runtime'],
                imdb = convert_to_double(row['IMDB_Rating']),
                meta_score = convert_to_int(row['Meta_score']),
                actor1 = row['Star1'],
                actor2 = row['Star2'],
                actor3 = row['Star3'],
                actor4 = row['Star4'],
                votes = row['No_of_Votes'],
                gross = convert_to_int(row['Gross'])
            )
            movie.genre.add(*genre_objects)  # Add genres to the movie

# Path to your CSV file
csv_file_path = 'imdb_top_1000.csv'

# Populate the database
populate_database(csv_file_path)
