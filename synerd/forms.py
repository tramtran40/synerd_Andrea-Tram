from django import forms

class DashboardForm(forms.Form):
    office = forms.CharField(max_length=100)
    officer = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    member = forms.CharField(max_length=100)
    subscriber = forms.CharField(max_length=100)
