from django.contrib import admin
from .models import (
  Institute,
  Career,
  Syllabus,
  Subject
)

admin.site.register(Institute)
admin.site.register(Career)
admin.site.register(Syllabus)
admin.site.register(Subject)
