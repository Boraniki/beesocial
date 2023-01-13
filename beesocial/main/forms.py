from django.forms import ModelForm, TextInput, Select, ChoiceField, Form, ModelChoiceField
from .models import *


class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['crn']