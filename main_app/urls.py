from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('create/', views.create_record_view, name='create_record'),
    path('detail/<int:record_id>/', views.detail_view, name='detail'),
]
