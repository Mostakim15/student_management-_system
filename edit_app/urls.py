from django.urls import path
from .views import edit

urlpatterns = [
    # Define your URL patterns for the edit application here
    # Example:
    # path('edit/', edit_view, name='edit_view'),
    path('edit/<int:id>/',edit, name='edit'),
]