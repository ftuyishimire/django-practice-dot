from django.urls import path
from products import views

urlpatterns = [
    path('index/', views.index_view, name="index"),
]