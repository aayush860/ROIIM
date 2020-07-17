from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include


urlpatterns = [
    path('checkout/', views.checkout),
    path('window/', views.windows),
    path('logout/', views.logout),
]