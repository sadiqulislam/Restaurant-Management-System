from django.shortcuts import render
from django.views import View
from rms.models import Chef

def chef_list(req):
    template = 'rms/chef_list.html'
    context ={
        'chef':Chef.objects.all()
    }
    return render(req,template,context)
