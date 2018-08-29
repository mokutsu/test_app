from django.urls import path
from . import views
urlpatterns = [
    path('api/contact/', views.ContactListCreate.as_view()),
    path('api/post/', views.PostListCreate.as_view()),
]
