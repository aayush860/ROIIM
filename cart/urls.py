from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include


urlpatterns = [
    path('checkout/', views.checkout),
    path('window/', views.windows),
    path('logout/', views.logout),
    path('payment_sucessful/', views.payment_sucessful),
    path('payment_unsucessful/', views.payment_unsucessful),
    path('payment_handle_not_created/', views.payment_handle_not_created),

    path('', views.windows),

]