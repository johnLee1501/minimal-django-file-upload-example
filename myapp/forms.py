from django import forms


class DocumentForm(forms.Form):
    csv = forms.FileField(label='Select a file')

