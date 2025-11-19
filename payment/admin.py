from django.contrib import admin
from django.contrib.auth.models import User, Group

from click_up.models import ClickTransaction
from payme.models import PaymeTransactions


# Remove unnecessary models from the main admin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(ClickTransaction)
admin.site.unregister(PaymeTransactions)


# Customize admin texts
admin.site.site_header = "Gijduvan Crafts boshqaruv paneli"
admin.site.site_title = "Gijduvan Crafts admin"
admin.site.index_title = "Boshqaruv bo'limlari"


