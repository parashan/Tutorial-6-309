from django.urls import path
from Store import views

urlpatterns = [
    path('items/', views.item_list),
    path('login/', views.login_func),
    path('items/<int:pk>/', views.item_detail),
    path('Images/<int:pk>', views.get_picture)
]