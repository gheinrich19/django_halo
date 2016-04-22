from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^test/?$', views.TestView.as_view(), name="test"),
	]