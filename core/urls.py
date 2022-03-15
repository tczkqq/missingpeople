from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create', views.create_view, name='create'),
    path('submited', views.submited_view, name='submited'),
    path('person/<int:id>', views.detail_view, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)