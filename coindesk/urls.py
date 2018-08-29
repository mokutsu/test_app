from django.urls import path
from . import views
urlpatterns = [
    path('api/coindesk/', views.CoinDeskListCreate.as_view()),
]
