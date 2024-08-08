from django.db import models
from django.core.validators import (
  MinValueValidator,
  MaxValueValidator
  )
from students.models import Student
from institutes.models import *

class Analysis(models.Model):
  student = models.ForeignKey(
    Student,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  origin_syllabus = models.ForeignKey(
    Syllabus,
    on_delete=models.SET_NULL,
    null=True,
    related_name="outer_syllabus"
  )
  receiver_syllabus = models.ForeignKey(
    Syllabus,
    on_delete=models.SET_NULL,
    null=True,
    related_name="inner_syllabus"
  )
  academy_president = models.CharField(max_length=256)
  department_head = models.CharField(max_length=256)
  created_at = models.DateField()

class Request(models.Model):
  student = models.ForeignKey(
    Student,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  to_institute = models.ForeignKey(
    Institute,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  to_career = models.ForeignKey(
    Career,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  created_at = models.DateField()

class Equivalence(models.Model):
  equivalence = models.ManyToManyField(Analysis, related_name="analysis")
  origin_subject = models.ForeignKey(
    Subject,
    on_delete=models.SET_NULL,
    null=True,
    related_name="outer_subjects"
  )
  receiver_subject = models.ForeignKey(
    Subject,
    on_delete=models.SET_NULL,
    null=True,
    related_name="inner_subjects"
  )
  percentage= models.IntegerField(
    default=0,
    validators=[MinValueValidator(0), MaxValueValidator(100)]
  )
