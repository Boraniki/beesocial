from django.db import models

# Create your models here.

class Courses(models.Model):
    crn = models.IntegerField(max_length=8)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    teaching_method = models.CharField(max_length=100, default=None, blank=True, null=True)
    instructor = models.CharField(max_length=100, default=None, blank=True, null=True)
    building =  models.CharField(max_length=100, default=None, blank=True, null=True)
    day = models.CharField(max_length=100)
    start_time =  models.CharField(max_length=100)
    end_time =  models.CharField(max_length=100)
    room = models.CharField(max_length=100, default=None, blank=True, null=True)
    capacity = models.IntegerField(max_length=8, default=None, blank=True, null=True)
    enrolled = models.IntegerField(max_length=8, default=None, blank=True, null=True)
    major_restriction = models.CharField(max_length=100, default=None, blank=True, null=True)
    prerequisites = models.CharField(max_length=100, default=None, blank=True, null=True)
    class_rest = models.CharField(max_length=100, default=None, blank=True, null=True)
