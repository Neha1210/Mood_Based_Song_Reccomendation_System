from django.forms import ModelForm
from .models import*

class addQuestionForm(ModelForm):
    class Meta:
        model=quiz
        fields='__all__'