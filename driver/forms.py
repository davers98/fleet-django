from django import forms
from driver.models import Inspection, Refilling


class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = '__all__'


class RefillingForm(forms.ModelForm):
    class Meta:
        model = Refilling
        fields = '__all__'



