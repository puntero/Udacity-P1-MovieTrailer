import media

def load_movies():  
  movieArray = [] 
  #Iterating over the list of movies in external file, and building the Movie array
  with open("./data/movies.txt", "r") as moviesFile:
    for entry in moviesFile: 
      movieArray.append(build_movie_data_structure(entry))

  return movieArray

def build_movie_data_structure(entry):
  movie = media.Movie()
  movie.title = entry.split('|')[0]      
  movie.trailer_youtube_url = entry.split('|')[1]
  movie.poster_image_url = entry.split('|')[2]    
  movie.actor = entry.split('|')[3]
  movie.release_date = entry.split('|')[4]
  
  return movie 