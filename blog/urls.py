from django.urls import path
from . import views
from blog.views import upload_video, display

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('base/', views.Homepage.as_view(), name='base'),

    path('upload/', upload_video, name='upload'),
    path('video/', display, name='video'),
    path('base/', display, name='base'),


    path('list/', views.list, name='list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

