from django import forms

class Send_email(forms.Form):
    Email = forms.EmailField()
    def __str__(self):Email
