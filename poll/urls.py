from django.conf.urls import url
from . import views

# noinspection PyInterpreter
urlpatterns = [

   url(r'^$', views.home, name='home'),
   url(r'^about/$',views.about, name='about'),
   url(r'^panel/$',views.panel, name='panel'),
  
]

