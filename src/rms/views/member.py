from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from rms.models import Member
from rms.forms import MemberForm

@login_required(login_url='login')
def member(req):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(req, 'rms/member/member.html', context=context)

class NewMemberView(LoginRequiredMixin, View):
    login_url = 'login'
    template = 'rms/member/member.html'

    def get(self, request):
        name = request.session.get('name', '')
        email = request.session.get('email', '')
        about = request.session.get('about', '')

        member_form = MemberForm(initial= {
            'name': name,
            'email': email,
        })