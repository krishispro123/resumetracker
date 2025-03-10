from django.urls import path
from django.conf.urls.static import static
from .import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('upload/',views.FileUploadView.as_view() ),
    path('registerUser/',views.RegisterView.as_view()),
    path('admin/',admin.site.urls)


]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)




