from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sendMail', views.send_mail_func, name='sendMail'),
]