from django.db import models
from django.core.validators import (
  MinValueValidator,
  MaxValueValidator
)
from students.models import Student
from institutes.models import *

class Analysis(models.Model):
  student = models.OneToOneField(
    Student,
    on_delete=models.CASCADE,
    primary_key=True
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
  student = models.OneToOneField(
    Student,
    on_delete=models.CASCADE,
    primary_key=True
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
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.student.first_name} {self.student.paternal_surname} {self.student.maternal_surname} - {self.student.institute.name}"

class Equivalence(models.Model):
  student = models.ManyToManyField(Student)
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
