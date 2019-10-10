from flask import render_template
from app import app # import the app instance from the __init__ file in our app folder.
from .request import get_movies, get_movie


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies("popular")
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    message = "Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups."*2
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', 
                            message = message, 
                            title = title, 
                            popular = popular_movies,
                            upcoming = upcoming_movie,
                            now_showing = now_showing_movie)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = "Movie"
    movie = get_movie(id)
    return render_template('movie.html',
                            id = movie_id, 
                            title = title,
                            movie = movie)