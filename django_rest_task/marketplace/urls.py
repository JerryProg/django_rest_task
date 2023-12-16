from django.urls import path
from . import views

urlpatterns = [
    path('marketplace/', views.MarketpAPIView.as_view(), name='marketplace-list'),
    path('marketplace/<int:pk>/', views.MarketpRetrieveView.as_view(), name='marketplace-ret'),
    path('marketplace/create/', views.MarketpAPIView.as_view(), name='marketplace-create'),
    path('marketplace/<int:pk>/update/', views.MarketpAPIView.as_view(), name='marketplace-update'),
    path('marketplace/<int:pk>/delete/', views.MarketpAPIView.as_view(), name='marketplace-delete'),
]