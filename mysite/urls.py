from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('index', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('aerodynamics/', views.aerodynamics, name='aerodynamics'),
    path('vehicledynamics/', views.vehicledynamics, name='vehicledynamics'),
    path('electronics/', views.electronics, name='electronics'),
    path('powertrain/', views.powertrain, name='powertrain'),
    path('media/', views.media, name='media'),
    path('marketing/', views.marketing, name='marketing'),
    path('gallery/', views.gallery, name='gallery')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)