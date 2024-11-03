from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
from .serializers import UserLoginSerializer
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Movie, Genre, User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
#Normal way of view
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, world!'})

#Using API view - post method for login
class UserLoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']
        print(username)
        print(password)
        
        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                request.session['username'] = username
                # token = Token.objects.create(user=user)
                # token = Token.objects.create(user=...)
                # print(token.key)

                return Response({'Success': "Valid credentials"}, status = status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials - user not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Invalid credentials - username ans password wrong'}, status=status.HTTP_400_BAD_REQUEST)

class UserSignUpView(APIView):
    def post(self, request, format = None):
        print(request.data)
        # data = json.loads(request.body)
        # username = data.get('username')
        # password = data.get('password')

        data = request.data
        username = data['username']
        password = data['password']

        # print(username)
        if username is None or password is None:
            return Response({'detail': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse({'detail': 'Please provide username and password.'}, status=400)
        
        try:
            user = User.objects.create_user(
                    username = username,
                    password = password,
                    email=  username)
            user.save()
            request.session['username'] = username

        except IntegrityError as e:
                return Response({'detail': 'Please enter a different email!'}, status=status.HTTP_400_BAD_REQUEST)
                # return JsonResponse({'detail': 'Please enter a different email!'}, status = 400)
    
        return Response({'detail':'Successfully registered'})
        # return JsonResponse({'detail':'Successfully registered'})

class UserLogOutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            request.session['username'] = ""
            return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class returnAllUserView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        users_data = [
        {
            'id' : user.id,
            'password': user.password,
            'email':user.email,
        }
        for user in users]

        # return JsonResponse({users_data}, status=200);
        return Response(users_data, status=status.HTTP_200_OK)
    
class returnMoviesFromGenreView(APIView):
    def post(self, request):
        # movies = models.Movie.objects.all()
        # print(request.body)
        data = json.loads(request.body)
        genres = data.get('genres')
        imdb = data.get('rating')
        print(genres)
        print(imdb)
        try:
            movies = Movie.objects.all() 
            if genres and imdb is None:
                return Response({'error': 'Genre and imdb not found'}, status=status.HTTP_404_NOT_FOUND)
            if imdb is not None:
                movies = movies.filter(imdb__gt=imdb)
            for genre in genres:
                print(genre)
                movies = movies.filter(genre__name=genre)

            print(movies)
            # current_movie = Movie.objects.filter(title=title).first()
            # genres = [genre.name for genre in current_movie.genre.all()]
            # print(genres)
            # movies = Movie.objects.all() 
            # for genre in genres:
                # movies = movies.filter(genre__name=genre)

            # Serialize movie data with genre details
            returned_movies = []
            unique_movies = set()
            for movie in movies:
               movie_key = (movie.title, movie.director)
               if movie_key not in unique_movies:
                    movie_data = {
                        'title': movie.title,
                        'url': movie.poster,
                        'director': movie.director,
                        'imdb': movie.imdb,
                        'overview': movie.overview,
                        'year': movie.year,
                        'genres': [genre.name for genre in movie.genre.all()]  # Get genre names associated with the movie
                    }
                    returned_movies.append(movie_data)
                    
                    # Add the movie title to the set of seen titles
                    unique_movies.add(movie_key)
            return Response({'movies':returned_movies}, status=status.HTTP_200_OK)
        
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        

# @login_required
class returnMoviesFromUserGenreView(APIView):
    def post(self, request, *args, **kwargs):
        authentication_classes = [SessionAuthentication]  # Use SessionAuthentication or another DRF authentication class
        permission_classes = [IsAuthenticated]  # Require authentication for this API view

        data = json.loads(request.body)
        genre_names = data.get('genres')
        imdb = data.get('rating')
        print(genre_names)
        print(imdb)
        # if request.user.is_authenticated:
        username = request.session.get('username')
        print(username)
        user = User.objects.get(username=username)
        print(user)
        if user is not None:
            user.favorite_genres.clear() 
            genres = Genre.objects.filter(name__in=genre_names)
            user.favorite_genres.add(*genres)
            
            user.imdb = imdb
            user.save()
            
            try:
                movies = Movie.objects.all() 
                if genres and imdb is None:
                    return Response({'error': 'Genre and imdb not found'}, status=status.HTTP_404_NOT_FOUND)
                if imdb is not None:
                    movies = movies.filter(imdb__gt=imdb)
                for genre in genres:
                    print(genre)
                    movies = movies.filter(genre__name=genre)

                print(movies)
                # current_movie = Movie.objects.filter(title=title).first()
                # genres = [genre.name for genre in current_movie.genre.all()]
                # print(genres)
                # movies = Movie.objects.all() 
                # for genre in genres:
                    # movies = movies.filter(genre__name=genre)

                # Serialize movie data with genre details
                returned_movies = []
                unique_movies = set()
                for movie in movies:
                    movie_key = (movie.title, movie.director)
                    if movie_key not in unique_movies:
                        movie_data = {
                            'title': movie.title,
                            'url': movie.poster,
                            'director': movie.director,
                            'imdb': movie.imdb,
                            'overview': movie.overview,
                            'year': movie.year,
                            'genres': [genre.name for genre in movie.genre.all()]  # Get genre names associated with the movie
                        }
                        returned_movies.append(movie_data)
                        
                        # Add the movie title to the set of seen titles
                        unique_movies.add(movie_key)

                return Response({'success': 'UserGenre updated successfully',
                                 'movies':returned_movies}, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response({'success': 'UserGenre updated successfully',
                                 'error': 'But no movies found'}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND) 

    def get(self, request):
        authentication_classes = [SessionAuthentication]  # Use SessionAuthentication or another DRF authentication class
        permission_classes = [IsAuthenticated]  # Require authentication for this API view

        # data = json.loads(request.body)
        # genre_names = data.get('genres')
        # imdb = data.get('rating')
        # print(genre_names)
        # print(imdb)
        # if request.user.is_authenticated:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        print(user)
        if user is not None:
            # user.favorite_genres.clear() 
            # genres = Genre.objects.filter(name__in=genre_names)
            # user.favorite_genres.add(*genres)
            
            # user.imdb = imdb
            # user.save()
            genres = user.favorite_genres.all()
            print("Genres", genres)
            imdb = user.imdb
            print("Imdb rating", imdb)
            try:
                movies = Movie.objects.all() 
                if genres and imdb is None:
                    return Response({'error': 'Genre and imdb not found'}, status=status.HTTP_404_NOT_FOUND)
                if imdb is not None:
                    movies = movies.filter(imdb__gt=imdb)
                
                returned_movies = []
                unique_movies = set()

                for genre in genres:
                    print(genre)
                    movies = movies.filter(genre__name=genre)
                    for movie in movies:
                        movie_key = (movie.title, movie.director)
                        if movie_key not in unique_movies:
                            movie_data = {
                                'title': movie.title,
                                'url': movie.poster,
                                'director': movie.director,
                                'imdb': movie.imdb,
                                'overview': movie.overview,
                                'year': movie.year,
                                'genres': [genre.name for genre in movie.genre.all()]  # Get genre names associated with the movie
                            }
                            returned_movies.append(movie_data)
                            
                            # Add the movie title to the set of seen titles
                            unique_movies.add(movie_key)

                # print(unique_movies)
                # print(returned_movies)

                # current_movie = Movie.objects.filter(title=title).first()
                # genres = [genre.name for genre in current_movie.genre.all()]
                # print(genres)
                # movies = Movie.objects.all() 
                # for genre in genres:
                    # movies = movies.filter(genre__name=genre)

                # Serialize movie data with genre details
                

                return Response({'success': 'UserGenre updated successfully',
                                 'movies':returned_movies}, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response({'success': 'UserGenre updated successfully',
                                 'error': 'But no movies found'}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND) 

