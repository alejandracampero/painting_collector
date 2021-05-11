from django.forms import ModelForm
from .models import Type

class TypeForm(ModelForm):
  class Meta:
    model = Type
    fields = ['type']