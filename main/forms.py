from django import forms
from main.models import VehicleStatus


class VehicleForm(forms.ModelForm):
    class Meta:
        model = VehicleStatus
        fields = '__all__'
