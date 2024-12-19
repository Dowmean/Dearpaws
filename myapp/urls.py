from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import *
from . import views 

urlpatterns = [
    path('', login_view, name='login'),
    path('create/', views.pet_create, name='pet_create'),
    path('home/', home_view, name='home'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)