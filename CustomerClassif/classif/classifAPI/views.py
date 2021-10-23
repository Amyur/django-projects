from django.shortcuts import render
from . forms import CustomerForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Customer
from . forms import CustomerForm
from . serializers import customerSerializers
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = customerSerializers

def customerreject(unit):
    try:
        model = joblib.load('C:/Users/Usuario/Google Drive/Google Drive/Proyectos/proyectos_django/CustomerClassif/classif/classifAPI/kmeans.pkl')
        unit = np.array(list(unit.values())).astype(float)
        unit = unit.reshape(1,-1)
        scaler = joblib.load("C:/Users/Usuario/Google Drive/Google Drive/Proyectos/proyectos_django/CustomerClassif/classif/classifAPI/scaler.pkl")
        X = scaler.fit_transform(unit)
        y_pred = model.predict(X)

        if y_pred == 0:
            answer = "have not cancer"
        else:
            answer = "have cancer"  
    
        return(answer)
    except ValueError as e:
        return Response(e.args[0])

def cxcontact(request):
    if request.method=='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            Fresh = form.cleaned_data["Fresh"]
            Milk = form.cleaned_data["Milk"]
            Grocery = form.cleaned_data["Grocery"]
            Frozen = form.cleaned_data["Frozen"]
            Detergents_Paper = form.cleaned_data["Detergents_Paper"]
            Delicassen = form.cleaned_data["Delicassen"]
            Channel_1 = form.cleaned_data["Channel_1"]
            Channel_2 = form.cleaned_data["Channel_2"]
            Region_1 = form.cleaned_data["Region_1"]
            Region_2 = form.cleaned_data["Region_2"]
            Region_3 = form.cleaned_data["Region_3"]
            myDict = dict(request.POST.lists())
            vars = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen", "Channel_1",
                    "Channel_2", "Region_1", "Region_2", "Region_3"]
            myDict = {x: myDict[x] for x in vars}
            answer = customerreject(myDict)
            messages.success(request,'Application Status: {}'.format(answer))

    form=CustomerForm()
    return(render(request, 'myform/cxform.html', {'form':form}))
