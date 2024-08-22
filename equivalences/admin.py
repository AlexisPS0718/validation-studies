from django.contrib import admin
from .models import (
  Analysis,
  Request,
  Equivalence
)

admin.site.register(Analysis)
admin.site.register(Request)
admin.site.register(Equivalence)
