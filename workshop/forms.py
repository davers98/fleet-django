from django import forms
from workshop.models import Maintainance


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintainance
        fields = '__all__'
