from . import db

class Movie:
    """
    Movie class to define Movie Objects
    """

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
    
    @classmethod
    def get_reviews(cls,id):
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response

class User(db.Model):
    # Ovewriting a the table name geneerated by SQLAlchemy
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    # string representaion to print out a row of a column, important in debugging
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship("User", backref = "role", lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'