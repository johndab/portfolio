from django import forms
from .models import CvRow

class CvRowForm(forms.ModelForm):

    class Meta:
        model = CvRow
        fields = ('section', 'title', 'subtitle', 'date', 'content')