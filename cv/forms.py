from django import forms
from .models import Post

class CvRowForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)