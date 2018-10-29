from django.conf.urls import url
from first__app import views

urlpatterns = [
url(r'^$', views.index, name = "index")
]
