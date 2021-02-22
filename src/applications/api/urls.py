from django.urls import path

from src.project.yasg import urlpatterns as doc_urls

from . import views

urlpatterns = [
    path("movie/", views.MovieApiView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailApiView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),
    path("actors/", views.ActorsListView.as_view()),
    path("actors/<int:pk>/", views.ActorsDetailView.as_view()),
]

urlpatterns += doc_urls
