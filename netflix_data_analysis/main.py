#Import numpy and pandas libraries
import numpy as np
import pandas as pd

# Get Netflix Data
netflix_data = pd.read_csv("netflix_data.csv")
#print(netflix_data.head())
# Requirement 1
# First get all movies.
netflix_movies = netflix_data[netflix_data['type'] == 'Movie']
# Now filter movies which released in 1990 decade
ninety_decade_movies = netflix_movies[np.logical_and(netflix_movies['release_year'] >= 1990, netflix_movies['release_year'] < 2000)]
ninety_decade_movies_dur = ninety_decade_movies['duration'].value_counts()
# most_duration is 94
most_duration = ninety_decade_movies_dur.index[0]

# Requirement 2
# We have ninety_decade_movies dataframe which stores movies released in 1990 decade
ninety_decade_movies_action = ninety_decade_movies[np.logical_and(ninety_decade_movies['genre'] == 'Action', ninety_decade_movies['duration'] < 90 )]
total_movies = ninety_decade_movies_action.shape[0]