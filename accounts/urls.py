from django.conf.urls import url
from django.urls import path
from . import views

appname = 'accounts'

urlpatterns=[
    path('signup/', views.signup_view, name="signup")
]
