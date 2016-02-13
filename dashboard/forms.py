from django import forms
from django.forms import Form

from backend.models import PregnantGirl


class UpdateGirlForm(forms.ModelForm):
    class Meta:
        model = PregnantGirl
        fields = '__all__'

class BlastForm(Form):
    text = forms.CharField(max_length=160, widget=forms.Textarea)
