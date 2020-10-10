
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('public/', include('apps.public.urls')),  # 微信公众号接口
]
