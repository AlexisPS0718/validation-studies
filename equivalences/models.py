from django.db import models
from django.core.validators import (
  MinValueValidator,
  MaxValueValidator
)
from students.models import Student
from institutes.models import *

class Analysis(models.Model):
  origin_syllabus = models.ForeignKey(
    Syllabus,
    on_delete=models.SET_NULL,
    null=True,
    related_name="origin_syllabus"
  )
  receiver_syllabus = models.ForeignKey(
    Syllabus,
    on_delete=models.SET_NULL,
    null=True,
    related_name="receiver_syllabus"
  )

  def __str__(self):
    return f"{self.origin_syllabus.career} - {self.origin_syllabus.career.institute}"

  def get_absolute_url(self):
    return reverse("analysis")

class DocAnalysis(models.Model):
  student = models.OneToOneField(
    Student,
    on_delete=models.CASCADE,
    primary_key=True,
    related_name="analysis"
  )
  analysis = models.ForeignKey(
    Analysis,
    on_delete=models.SET_NULL,
    null=True
  )
  academy_president = models.CharField(max_length=256)
  department_head = models.CharField(max_length=256)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.student.first_name} {self.student.paternal_surname} {self.student.maternal_surname}"

  def get_absolute_url(self):
    return reverse("doc-analysis", args=(self.student.id,))

class Request(models.Model):
  student = models.OneToOneField(
    Student,
    on_delete=models.CASCADE,
    primary_key=True,
    related_name="request"
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

  def get_absolute_url(self):
    return reverse("request", args=(self.student.id,))

class Equivalence(models.Model):
  analysis = models.ForeignKey(
    Analysis,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  origin_subject = models.ForeignKey(
    Subject,
    on_delete=models.CASCADE,
    blank=True, null=True,
    related_name="origin_subject"
  )
  receiver_subject = models.ForeignKey(
    Subject,
    on_delete=models.CASCADE,
    blank=True, null=True,
    related_name="receiver_subject"
  )
  percentage= models.IntegerField(
    default=0,
    validators=[MinValueValidator(0), MaxValueValidator(100)]
  )

  def __str__(self):
    return f"{self.origin_subject}"
