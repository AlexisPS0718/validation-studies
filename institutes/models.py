from django.db import models
from django.urls import reverse

class Institute(models.Model):
  name = models.CharField(max_length=128)
  republic_state = models.CharField(max_length=128)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("institutes")

class Career(models.Model):
  institution = models.ForeignKey(
    Institute,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  name = models.CharField(max_length=128)
  is_engineering = models.BooleanField(default=0)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("careers", args=[self.institution.id])

class Syllabus(models.Model):
  career = models.ForeignKey(
    Career,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  key = models.CharField(max_length=128)
  start_date = models.DateField()
  final_date = models.DateField()

  def __str__(self):
    return self.career.name

class Subject(models.Model):
  syllabus = models.ManyToManyField(Syllabus, related_name="syllabus")
  key = models.CharField(max_length=128)
  name = models.CharField(max_length=128)

  def __str__(self):
    return self.name
