from django.urls import path,include
from django.urls.resolvers import URLPattern
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.getRoutes),
    #USER URLS
    path('user/',views.getUsers),
    path('user/create/',views.createUser),
    path('user/<str:uname>/',views.getSingleUser),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)