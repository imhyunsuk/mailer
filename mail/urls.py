from django.urls import path

from . import views

app_name='mail'
urlpatterns = [
    path('<uuid:promotion_uuid>/', views.check_open, name='check_open'),
]
