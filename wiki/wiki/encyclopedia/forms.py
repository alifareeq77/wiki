from django import forms


class CreatePageForm(forms.Form):

    title = forms.CharField(label="TITLE")
    body = forms.CharField(label="BODY")
