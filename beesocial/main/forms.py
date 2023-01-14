from django.forms import ModelForm, TextInput, Select, ChoiceField, Form, ModelChoiceField
from .models import Courses


class CoursesForm(ModelForm):
    course_code = ChoiceField(choices=Courses.objects.values_list('course_code', 'course_code').distinct())
    class Meta:
        model = Courses
        fields = ['course_code', 'day_hour', 'crn']
        widgets = {
            'course_code': Select(attrs={'class': 'form-control'}),
        }