from django import forms
from yaleapp import Survey

class SurveyForm(forms.ModelForm):

    class Meta:
        model = Survey
        fields = ('Q1', 'Q2', 'Q3',)
