from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"name"}))
    ph = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"ph"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control textas", "id":"message"}))