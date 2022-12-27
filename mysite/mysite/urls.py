
from django.contrib import admin
from django.urls import *
from news.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
