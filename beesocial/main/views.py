from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        data = Courses.objects.filter(crn=request.POST['crn'],
                                      course_code=request.POST['course_code'],
                                      course_title=request.POST['course_title'])
        context = {'data':data, 'form':form}
        return render(request, 'main/index.html', {'form':form,'data':data[:10]})

    context = {'form':form}
    return render(request, 'main/index.html', {'form':form})
