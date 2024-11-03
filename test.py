from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from landing_page.models import Genre, Movie, User


class MovieModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="Action")
        cls.movie = Movie.objects.create(
            poster="sample_poster.jpg",
            title="Sample Movie",
            year=2022,
            certificate="PG-13",
            runtime="2h 30m",
            imdb=8.5,
            overview="This is a sample movie overview.",
            meta_score=85,
            director="Sample Director",
            actor1="Actor 1",
            actor2="Actor 2",
            actor3="Actor 3",
            actor4="Actor 4",
            votes=1000,
            gross=1000000
        )
        cls.movie.genre.add(genre)

    def test_movie_creation(self):
        self.assertEqual(self.movie.poster, "sample_poster.jpg")
        self.assertEqual(self.movie.title, "Sample Movie")
        self.assertEqual(self.movie.year, 2022)
        self.assertEqual(self.movie.certificate, "PG-13")
        self.assertEqual(self.movie.runtime, "2h 30m")
        self.assertEqual(self.movie.imdb, 8.5)
        self.assertEqual(self.movie.overview, "This is a sample movie overview.")
        self.assertEqual(self.movie.meta_score, 85)
        self.assertEqual(self.movie.director, "Sample Director")
        self.assertEqual(self.movie.actor1, "Actor 1")
        self.assertEqual(self.movie.actor2, "Actor 2")
        self.assertEqual(self.movie.actor3, "Actor 3")
        self.assertEqual(self.movie.actor4, "Actor 4")
        self.assertEqual(self.movie.votes, 1000)
        self.assertEqual(self.movie.gross, 1000000)

    def test_movie_genre(self):
        self.assertEqual(self.movie.genre.count(), 1)
        genre = self.movie.genre.first()
        self.assertEqual(genre.name, "Action")

class GenreModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Action")
        Genre.objects.create(name="Comedy")

    def test_genre_creation(self):
        action_genre = Genre.objects.get(name="Action")
        comedy_genre = Genre.objects.get(name="Comedy")

        self.assertEqual(action_genre.name, "Action")
        self.assertEqual(comedy_genre.name, "Comedy")

    def test_genre_str_method(self):
        action_genre = Genre.objects.get(name="Action")
        comedy_genre = Genre.objects.get(name="Comedy")

        self.assertEqual(str(action_genre), "Action")
        self.assertEqual(str(comedy_genre), "Comedy")

class UserModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.username = "testuser"
        cls.password = "testpassword"
        cls.email = "testuser@example.com"
        cls.favorite_genre = Genre.objects.create(name="Action")
        cls.imdb_rating = 8.5
        cls.user = User.objects.create_user(
            username=cls.username, 
            password=cls.password, 
            email=cls.email,
            imdb=cls.imdb_rating
        )
        cls.user.favorite_genres.add(cls.favorite_genre)

    def test_user_creation(self):
        self.assertEqual(self.user.username, self.username)
        self.assertTrue(self.user.check_password(self.password))
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.imdb, self.imdb_rating)

    def test_user_authentication(self):
        authenticated_user = User.objects.get(username=self.username)
        self.assertTrue(authenticated_user.check_password(self.password))

    def test_favorite_genres(self):
        self.assertEqual(self.user.favorite_genres.count(), 1)
        genre = self.user.favorite_genres.first()
        self.assertEqual(genre.name, "Action")

class UserLoginViewTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.email = "testuser@example.com"
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)

    def test_valid_login(self):
        client = APIClient()
        response = client.post('/login/', {'username': self.username, 'password': self.password}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Success', response.data)
        self.assertEqual(response.data['Success'], "Valid credentials")

    def test_invalid_login(self):
        client = APIClient()
        response = client.post('/login/', {'username': self.username, 'password': 'wrongpassword'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], "Invalid credentials - user not authenticated")

class UserSignUpViewTestCase(TestCase):
    def test_valid_signup(self):
        client = APIClient()
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = client.post('/signup/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], "Successfully registered")


    def test_duplicate_username(self):
        # Simulate a sign up request with an existing username
        client = APIClient()
        # Create a user with the same username
        User.objects.create_user(username='testuser', password='testpassword')
        data = {'username': 'testuser', 'password': 'testpassword2'}
        response = client.post('/signup/', data, format='json')
        
        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], "Please enter a different email!")

class ReturnMoviesFromGenreViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre1 = Genre.objects.create(name="Action")
        cls.genre2 = Genre.objects.create(name="Adventure")
        cls.movie1 = Movie.objects.create(title="Movie 1", director="Director 1", imdb=8.0, overview="Overview 1", year=2022)
        cls.movie1.genre.add(cls.genre1)
        cls.movie2 = Movie.objects.create(title="Movie 2", director="Director 2", imdb=7.5, overview="Overview 2", year=2021)
        cls.movie2.genre.add(cls.genre2)

    def test_return_movies(self):
        client = APIClient()
        data = {'genres': ['Action'], 'rating': 7.8}
        response = client.post('/movies/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('movies', response.data)
        self.assertEqual(len(response.data['movies']), 1)
        self.assertEqual(response.data['movies'][0]['title'], "Movie 1")

    def test_no_movies_found(self):
        client = APIClient()
        data = {'genres': ['Comedy'], 'rating': 7.8}
        response = client.post('/movies/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['movies']), 0)
