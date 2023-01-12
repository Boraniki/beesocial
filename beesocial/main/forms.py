from django.forms import ModelForm, TextInput, Select, ChoiceField, Form
from .models import *

class CoursesForm(ModelForm):
    class Meta:
        data = Courses.objects.all()
        model = Courses
        # fields = '__all__'
        fields = ['course_code','course_title','crn',]
        # OPTIONS = (('FIZ', 'FIZ'),('MAT','MAT'),)  #('Flo', 'Flo'),('Mavi Jeans', 'Mavi'), ('Derimod','Derimod'), ('Koton', 'Koton'),
        # labels = {'course_code':''}
        # widgets = {'course_code' : Select(attrs={'class':'form-select'}, choices=OPTIONS)}
