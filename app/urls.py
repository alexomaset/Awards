from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.index,name = 'home_page'),
    url(r'^profile/(?P))
]