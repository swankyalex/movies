from django.urls import path

from . import views

urlpatterns = [
    path("movie/", views.MovieApiView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailApiView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
]
