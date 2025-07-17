from django.urls import path
from .views import create
urlpatterns = [
    # Define your URL patterns for the edit application here
    # Example:
    # path('edit/', edit_view, name='edit_view'),
    path('', create, name='create'),  # URL for creating a student

]