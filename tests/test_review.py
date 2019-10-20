import unittest
from app.models import Review, User
from app import db

class ReviewTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Review class
    """
    def setUp(self):
        self.user_Collins = User(username = "Collins",
                                password = "easy",
                                email = "collins@mail.com")
        self.new_review = Review(movie_id = 12345,
                                movie_title = "Sample Movie",
                                image_path = "https://image.tmdb.org/t/p/w500/abcde",
                                movie_review = "One of the best movies I've watched",
                                review_title = "Amazing!",
                                user = self.user_Collins)

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Collins, User))
        self.assertTrue(isinstance(self.new_review, Review))

    def test_check_instance_variables(self):
        self.assertEqual(self.new_review.movie_id, 12345)
        self.assertEqual(self.new_review.movie_title, "Sample Movie")
        self.assertEqual(self.new_review.image_path, "https://image.tmdb.org/t/p/w500/abcde")
        self.assertEqual(self.new_review.movie_review, "One of the best movies I've watched")
        self.assertEqual(self.new_review.review_title, "Amazing!")
        self.assertEqual(self.new_review.user, self.user_Collins)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all()) > 0)

    def test_get_reviews_by_id(self):
        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)

if __name__ == "__main__":
    unittest.main()