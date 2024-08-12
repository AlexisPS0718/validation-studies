from django.db import models
from django.urls import reverse
from institutes.models import (
  Institute,
  Career
)

class Student(models.Model):
  institution = models.ForeignKey(
    Institute,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  career = models.ForeignKey(
    Career,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  first_name = models.CharField(max_length=128)
  paternal_surname = models.CharField(max_length=128)
  maternal_surname = models.CharField(max_length=128)
  street_and_number = models.CharField(max_length=256)
  neighborhood = models.CharField(max_length=256)
  zip_code = models.IntegerField()
  municipality = models.CharField(max_length=128)
  city = models.CharField(max_length=128)
  state = models.IntegerField()
  nationality = models.CharField(max_length=128)
  sex = models.CharField(max_length=1)
  level = models.CharField(max_length=128)
  area = models.CharField(max_length=128)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.first_name

  def get_absolute_url(self):
    return reverse("students")
