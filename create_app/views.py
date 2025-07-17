from django.shortcuts import render, redirect
from create_app.models import student


# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        department = request.POST.get('department')
        image = request.FILES.get('image')

        # Create a new student instance
        if name :
            new_student = student.objects.create(
                name=name,
                email=email,
                age=age,
                department=department,
                image=image
            )
            new_student.save()
            return redirect('home')
    return render(request, 'create/create.html')