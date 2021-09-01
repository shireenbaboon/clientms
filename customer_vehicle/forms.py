from django import forms
from .models import Vehicle


class DateInput(forms.DateInput):
    input_type='date'


class VehicleForm(forms.ModelForm):
    purchase_date=forms.DateField(widget=DateInput)
    last_service_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Vehicle
        fields = "__all__"

