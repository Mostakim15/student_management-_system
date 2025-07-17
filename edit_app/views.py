from django.shortcuts import render, redirect
from create_app.models import student
from django.contrib import messages
import os

# Create your views here.
def edit(request, id):
    students = student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        department = request.POST.get('department')
        image = request.FILES.get('image')
        try:
                if name:
                    students.name = name
                if email:
                    students.email = email
                    messages.success(request, 'Email updated successfully')
                if age:
                    students.age = age
                if department:
                    students.department = department
                if image and students.image  and students.image.name != 'images/default.jpg' :
                    os.remove(students.image.path)
                    students.image = image
                students.save()
                messages.success(request, 'Student updated successfully')
        except:
                messages.error(request, 'Error updating student: ')
        
        return redirect('home')

    return render(request, 'edit/edit.html', {'stu': students})