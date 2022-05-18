from email.policy import default
from django import forms

class pushupLogsForm(forms.Form):
    exercize_date = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    pushup_count = forms.IntegerField(required=True, )

