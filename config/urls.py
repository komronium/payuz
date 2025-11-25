from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from payment.views import PaymeCallBackAPIView, ClickWebhookAPIView
from product.views import CategoryListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('order.urls')),
    path('products/', include('product.urls')),
    path('categories/', CategoryListAPIView.as_view()),
    path('payment/payme/update/', PaymeCallBackAPIView.as_view()),
    path("payment/click/update/", ClickWebhookAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
