from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'nitkracing_ev'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('lv/', views.lv, name='lv'),
    path('chassis/',views.chassis, name='chassis'),
    path('vehicledynamics/', views.vehicledynamics, name='vehicledynamics'),
    path('battery/', views.battery, name='battery'),
    path('epowertrain/', views.epowertrain, name='epowertrain'),
    path('media/', views.media, name='media'),
    path('marketing/', views.marketing, name='marketing'),
    path('gallery/', views.gallery, name='gallery')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
