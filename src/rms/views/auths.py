from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


#For SignUp:

class SignupView(View):
    template = "rms/auths/signup.html"

    def get(self, request):
        context ={

        }
        return render(request,self.template,context=context)

    def post(self, request):
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['e-mail']
        password = request.POST['password']
        username = email

        #create User:

        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        user.save()
        messages.add_message(request, messages.INFO,
                             f"User Registered Succesfully")
        return redirect('login')


#For LogIn:

class LoginView(View):
    template = 'rms/auths/login.html'

    def get(self,request):
        context = {

        }

        return render(request,self.template,context=context)

    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']

        #Authenticate User:
        user = authenticate(request,username=email,password=password)
        if user is None:
            messages.add_message(request,messages.ERROR,
                                 f"Invalid Username Or Password")
            return redirect('login')
        else:
            login(request,user)
            messages.add_message(request,messages.INFO,
                                 f"Successfully Logged In")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#Forget Password:

def forget_password(req):

    context = {

        }
    return render(req,'rms/forgetpassword.html', context)




#Logout:

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))