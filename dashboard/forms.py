from django import forms

from backend.models import PregnantGirl


class UpdateGirlForm(forms.ModelForm):
    class Meta:
        model = PregnantGirl
        fields = '__all__'