from django.urls import path
from . import views

urlpatterns = [
    path('<slug:ob>/create/', views.create),
    path('<slug:ob>/view/', views.view_all),
    path('<slug:ob>/view/<int:pk>/', views.view_id),
    path("<slug:ob>/edit/<int:pk>/", views.update),
    path("<slug:ob>/delete/<int:pk>/", views.delete),
    path("user/<int:id>/order/", views.view_order_all)
]