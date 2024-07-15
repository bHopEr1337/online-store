from django.contrib import admin
from django.urls import path, include
from frontMain.views import index, about, contact, house, price
from users.views import login, register

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('main/', include('frontMain.urls', namespace='frontMain')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)