from django.contrib import admin
from .models import (
  Analysis,
  DocAnalysis,
  Request,
  Equivalence
)

admin.site.register(Analysis)
admin.site.register(DocAnalysis)
admin.site.register(Request)
admin.site.register(Equivalence)
