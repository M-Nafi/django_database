from django.urls import path
from .views import CustomerListView, CustomerListSearchView, CustomerDetailView


urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>/', CustomerListSearchView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view()),

]
