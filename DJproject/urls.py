from django.contrib import admin
from django.urls import path, include

from app1.views import main_page, about_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page),
    path("about/", about_page),
    path('', include('app_download.urls')),

]
