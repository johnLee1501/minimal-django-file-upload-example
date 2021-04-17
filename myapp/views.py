import os
import unittest
import pandas as pd
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import Employee

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@transaction.atomic
def my_view(request):
    message = 'Registro de usuarios csv!'
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_csv = request.FILES['csv']
            usuario_dataframe = pd.read_csv(new_csv.file)
            usuario_dataframe = usuario_dataframe.drop('id', axis=1)
            for i in usuario_dataframe.index:
                Employee.objects.create(fullname=usuario_dataframe.fullname[i], emp_code=usuario_dataframe.emp_code[i],
                                        mobile=usuario_dataframe.mobile[i],
                                        position_id=usuario_dataframe.position_id[i])
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load base for the list page
    employes = Employee.objects.all()

    # Render list page with the base and the form
    context = {'employes': employes, 'form': form, 'message': message}
    return render(request, 'list.html', context)
