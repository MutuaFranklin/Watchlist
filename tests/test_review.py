import unittest
from app.models import Review,User
from flask_login import current_user
from app import db

class TestReview(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )


    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)