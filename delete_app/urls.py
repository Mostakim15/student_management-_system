from django.urls import path
from .views import delete_student
urlpatterns = [
    path('delete/<int:id>/', delete_student, name='delete_student'),  # URL for deleting a student
    # You can add more URL patterns for the delete application here
    # Define your URL patterns for the edit application here
    # Example:
    # path('edit/', edit_view, name='edit_view'),

]