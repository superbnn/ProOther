from django.conf.urls import url

from app01 import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^add_user$', views.add_user),
    url(r'^do_add_user$', views.do_add_user),
    url(r'^show_images$', views.show_images),
]