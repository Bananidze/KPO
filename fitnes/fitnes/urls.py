from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('records/', include('records.urls')),
    path('', TemplateView.as_view(template_name ='main/main.html'), name = 'main'),
    path('about', TemplateView.as_view(template_name ='main/about.html'), name = 'about'),
    # path('record', TemplateView.as_view(template_name ='main/record.html'), name = 'record'),
    path('hospitals', TemplateView.as_view(template_name ='main/hospitals.html'), name = 'hospitals'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
