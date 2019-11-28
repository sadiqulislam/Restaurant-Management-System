from django.shortcuts import render

def home(req):
    context ={

    }
    return render(req,'rms/home.html',context=context)