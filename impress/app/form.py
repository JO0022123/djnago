from django import forms
from .models import company
class detailsform(forms.ModelForm):
    class Meta:
        model=company
        fields=("name","age","address")
        