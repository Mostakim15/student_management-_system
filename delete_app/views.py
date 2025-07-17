from django.shortcuts import render,redirect
from create_app.models import student
import os

# Create your views here.

def delete_student(request, id):
    students = student.objects.get(id=id)
    if students.image and students.image.name != 'images/default.jpg':
        os.remove(students.image.path)
        # Delete the image file from the filesystem
    students.delete()  # Delete the student record from the database
    # Redirect to the previous page or home
    return redirect(request.META.get('HTTP_REFERER', 'home'))
