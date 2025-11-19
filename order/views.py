from payme import Payme
from click_up import ClickUp
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from order.models import Order
from order.serializers import OrderSerializer

payme = Payme(
    payme_id=settings.PAYME_ID,
    is_test_mode=settings.PAYME_TEST_MODE
)

click_up = ClickUp(
    service_id=settings.CLICK_SERVICE_ID,
    merchant_id=settings.CLICK_MERCHANT_ID
)


class OrderCreate(APIView):
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        payment_method = serializer.data['payment_method']
        result = {
            'order': serializer.data
        }

        if payment_method == 'payme':
            payment_link = payme.initializer.generate_pay_link(
                id=serializer.data['id'],
                amount=serializer.data['total_cost'],
                return_url='gijduvancrafts.com'
            )
            result['payment_link'] = payment_link
        elif payment_method == 'click':
            payment_link = click_up.initializer.generate_pay_link(
                id=serializer.data['id'],
                amount=serializer.data['total_cost'],
                return_url='gijduvancrafts.com'
            )
            result['payment_link'] = payment_link

        return Response(result)


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
