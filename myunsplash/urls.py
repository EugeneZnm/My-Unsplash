from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.Home,name='Home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^pic/(\d+)',views.single_image, name='single_image'),
    url(r'^location/(\w+)',views.location, name='location'),
    url(r'^location/(\d+)', views.location, name='locale')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)