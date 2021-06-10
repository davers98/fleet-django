from django import forms
from staff.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
