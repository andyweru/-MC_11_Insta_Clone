from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^$',views.entry,name = "entry"),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^logout/', views.logout, {"next_page": '/'}),
]