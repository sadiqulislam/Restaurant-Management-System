from django.urls import path, re_path
from django.conf import settings

from .views import (
        home,
        member,
        food_item,
        chef_list
)

from .views.about import (
    about
)

from .views .auths import (
        SignupView,
        LoginView,
)


urlpatterns =[

    path('',home,name='home'),
    path('Member-List',member,name='member-list'),
    path('Food-Item',food_item,name='food-item'),
    path('Chef-List',chef_list,name= 'chef-list'),
    path('about', about, name='about'),

    #Auths:
    path('SignUp', SignupView.as_view(), name="signup"),
    path('LogIn', LoginView.as_view(), name="login"),
]