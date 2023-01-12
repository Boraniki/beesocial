from django.db import models

# Create your models here.

class Intern(models.Model):
    crn = models.IntegerField(max_length=8)
    course_code = models.IntegerField(max_length=8)
    course_title = models.CharField(max_length=100)
    teaching_method = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    building =  models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    start_time =  models.CharField(max_length=100)
    end_time =  models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=8)
    enrolled = models.IntegerField(max_length=8)
    major_restriction = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100)
    class_rest = models.CharField(max_length=100)
    
