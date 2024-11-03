from django.urls import path
from .views import UserLoginView, UserSignUpView, returnAllUserView, returnMoviesFromGenreView, returnMoviesFromUserGenreView, UserLogOutView

urlpatterns = [
    # path('test/', views.hello_world, name='hello_world'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('logout/', UserLogOutView.as_view(), name="logout"),
    path('getalluser/', returnAllUserView.as_view(), name='all_users'),
    path('movies/', returnMoviesFromGenreView.as_view(),name='movies'),
    path('usermovies/', returnMoviesFromUserGenreView.as_view(), name='usermovies')
    # path('usermovies/', returnMoviesFromUserGenreView.as_view(), name='usermovies')
]