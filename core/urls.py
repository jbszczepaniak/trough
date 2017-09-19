from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', auth_views.login, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': reverse_lazy('core:index')}, name='logout'),
    # url(r'register/$', views.signup, name='signup'),

]