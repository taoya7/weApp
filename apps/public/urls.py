from django.urls import path

from .views import Index
app_name = 'public'

urlpatterns = [
    path('', Index.as_view()),
]