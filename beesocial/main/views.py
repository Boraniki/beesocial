from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        data = Courses.objects.filter(
        crn=request.POST['crn'])

        context = {'data':data, 'form':form}
        return render(request, 'main/index.html', context)



    context = {'form':form}
    return render(request, 'main/index.html', {'form':form})
