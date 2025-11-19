from payme.views import PaymeWebHookAPIView
from payme.models import PaymeTransactions
from click_up.views import ClickTransaction
from click_up.views import ClickWebhook

from order.models import Order


class PaymeCallBackAPIView(PaymeWebHookAPIView):

    def handle_created_payment(self, params, result, *args, **kwargs):
        pass

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        transaction = PaymeTransactions.get_by_transaction_id(
            transaction_id=params['id']
        )
        order = Order.objects.get(id=transaction.account_id)
        order.is_paid = True
        order.save()

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        transaction = PaymeTransactions.get_by_transaction_id(
            transaction_id=params['id']
        )

        if transaction.state == PaymeTransactions.CANCELED:
            order = Order.objects.get(id=transaction.account_id)
            order.is_paid = False
            order.save()


class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )
        order = Order.objects.get(id=transaction.account_id)
        order.is_paid = True
        order.save()

    def cancelled_payment(self, params):
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )

        if transaction.state == ClickTransaction.CANCELLED:
            order = Order.objects.get(id=transaction.account_id)
            order.is_paid = False
            order.save()
