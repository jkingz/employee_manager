from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('managers.urls', namespace='managers')),
    path('admin/', admin.site.urls),
]
