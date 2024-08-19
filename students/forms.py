from django import forms
from institutes.models import Career
from .models import Student

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ("institute", "career", "first_name", "paternal_surname", "maternal_surname", "street_and_number", "neighborhood", "zip_code", "municipality", "city", "state", "phone_number", "nationality", "sex", "level", "area")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['career'].queryset = Career.objects.none()

    if 'institute' in self.data:
      try:
        institute_id = int(self.data.get('institute'))
        self.fields['career'].queryset = Career.objects.filter(institute_id=institute_id).order_by('name')
      except (ValueError, TypeError):
        pass
    elif self.instance.pk:
      self.fields['career'].queryset = self.instance.institute.career_set.order_by('name')
