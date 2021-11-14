from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [
    path('', views.BasketListView.as_view(), name='basket-list'),
    path('<int:pk>/remove_basket_item/', views.RemoveBasketItemView.as_view(), name='remove-basket-item')
]
