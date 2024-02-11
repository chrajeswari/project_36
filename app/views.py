from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
from app.models import *
# returning  string as response by using FBV

def fbv_string(request):
    return HttpResponse('<h1>this is the string from fbv_string</h1>')


 #returning  string as response by using FBV

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>string of cbvstring</h1>')
    

#rendering html by fbv

def fbvhtml(request):
    return render(request,'fbvhtml.html')

# rendering html by cbv

class Cbvhtml(View):
    def get(self,request):
        return render(request,'Cbvhtml.html')
    

#insert data by fbv through model forms
    
def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')
        
    return render(request,'insert_school_by_fbv.html',d)

#insert data by cbv through model forms 

class insert_school_by_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_school_by_cbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_cbv is done')
        

class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'

    