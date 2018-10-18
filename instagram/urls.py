from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.entry,name = "entry"),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^search/', views.search, name='search'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^logout/', views.logout, {"next_page": '/'}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)