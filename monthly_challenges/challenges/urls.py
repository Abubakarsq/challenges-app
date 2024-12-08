from django.urls import path
from . import views


urlpatterns = [
    path('', views.challenge_pages, name="homepage"),
    path('<int:month>', views.monthly_challenge_page_with_number),
    path('<str:month>', views.monthly_challenge_page, name="month"),
]
