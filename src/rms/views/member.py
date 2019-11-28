from django.shortcuts import render

def member(req):
    context ={

    }
    return render(req,'rms/member.html',context=context)