from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("api/v1/movie/", views.MovieApiView.as_view()),
    path("api/v1/movie/<int:pk>/", views.MovieDetailApiView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name="filter"),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("search/", views.Search.as_view(), name="search"),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("category/<slug:slug>/", views.CategoryView.as_view(), name="categories"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]
