from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get-models/', views.TestModelList.as_view(), name='get-models'),
]
