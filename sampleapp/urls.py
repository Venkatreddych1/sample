from django.conf.urls import url
from . import views
app_name = 'sampleapp'
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^reg$', views.reg,name='reg'),
    url(r'^login$',views.login,name='login'),
    url(r'^display$',views.display),
    url(r'^image$', views.myview, name='image_upload'),
]
