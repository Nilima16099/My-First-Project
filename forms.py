from django import forms
from laamar.models import laamar

class laamarform(forms.modelForm):
class Meta:
    model=laamar
    fields={"tittle","name","email","message"}

