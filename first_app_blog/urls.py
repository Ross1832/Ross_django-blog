from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('offshore_blog.urls', namespace='offshore_blog')),
    path('admin/', admin.site.urls),
]
