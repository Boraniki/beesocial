from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    data = Courses.objects.all()
    form = CoursesForm()
    # form = CoursesForm()
    # if request.method == 'POST':
    #     form = CoursesForm(request.POST)
    #     data = Courses.objects.filter(tenant=request.POST['tenant'])
    # context = {'data':data, 'form':form}
    return render(request, 'main/index.html', {'form':form,'data':data})
