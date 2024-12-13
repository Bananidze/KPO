from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name ='records/record.html'), name = 'record'),
    # path('delete_record', TemplateView.as_view(template_name ='records/delete_record.html'), name = 'delete_record'),
    path('delete_record', views.get_record, name = 'delete_record'),
    path('create_record', views.create_record, name = 'create_record'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)