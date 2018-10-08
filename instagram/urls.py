from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^$',views.entry,name = "entry"),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^logout/', views.logout, {"next_page": '/'}),
]