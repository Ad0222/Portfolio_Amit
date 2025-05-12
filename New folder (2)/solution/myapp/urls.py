from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    #  path('', include('myapp.urls')),
     path('',views.index,name='index'),
     
    #  path('api/contact/', views.contact_api, name='contact_api'),
    # path('api/contact/', views.contact_form, name='contact_form'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)