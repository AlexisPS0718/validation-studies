from django.db import models

class Institute(models.Model):
  name = models.CharField(max_length=128)
  republic_state = models.CharField(max_length=128)

class Career(models.Model):
  institution = models.ForeignKey(
    Institute,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  name = models.CharField(max_length=128)
  is_engineering = models.BooleanField(default=0)

class Syllabus(models.Model):
  career = models.ForeignKey(
    Career,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  key = models.CharField(max_length=128)
  start_date = models.DateField()
  final_date = models.DateField()

class Subject(models.Model):
  syllabus = models.ManyToManyField(Syllabus, related_name="syllabus")
  key = models.CharField(max_length=128)
  name = models.CharField(max_length=128)
