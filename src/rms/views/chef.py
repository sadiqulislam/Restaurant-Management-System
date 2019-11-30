from django.shortcuts import render
from django.views import View
from rms.models import Chef

def chef_list(req):
    template = 'rms/chef/chef_list.html'
    context ={
        'chef': Chef.objects.all()
    }
    return render(req, template, context)

class ChefAddUpdate(View):
    def get(self,request):
        raise NotImplemented

    def post(self,request):
        raise NotImplemented

def chef_delete(request):
    raise NotImplemented