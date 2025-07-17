from django.shortcuts import render
from create_app.models import student
def home(request):
    students = student.objects.all()
    if request.method == "GET":
        search_query = request.GET.get("search")
        if search_query:
            students = students.filter(name__icontains=search_query)
    else:
        return render(request, 'home/home.html', {'students': students})
    return render(request, 'home/home.html', {'students': students})
# Create your views here.
