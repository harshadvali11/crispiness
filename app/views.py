from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def form(request):
    form=Crispy_Form()
    if request.method=='POST':
        form_data=Crispy_Form(request.POST)# it has collected the data
        if form_data.is_valid():
            #return HttpResponse(form_data.cleaned_data['name'])
            return HttpResponse(form_data.cleaned_data)
    return render(request,'form.html',context={'form':form})