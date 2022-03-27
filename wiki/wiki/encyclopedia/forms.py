from django import forms


class CreatePageForm(forms.Form):
    title = forms.CharField(label="TITLE")
    body = forms.CharField(label="BODY", widget=forms.Textarea())


class EditForm(forms.Form):

    title = forms.CharField(label="TITLE")
    body = forms.CharField(label="BODY", widget=forms.Textarea(attrs={'style': 'width: 800px; height: 300px'}))
