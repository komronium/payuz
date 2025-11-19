from django.urls import path

from order.views import OrderCreate, OrderDetail, OrderList


urlpatterns = [
    path('create/', OrderCreate.as_view()),
    path('', OrderList.as_view()),
    path('<int:pk>/', OrderDetail.as_view())
]
