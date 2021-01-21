from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    name = forms.CharField(label='Nombre:', max_length=15)
    class_name = forms.CharField(label='Nombre de Clase:', max_length=15)
