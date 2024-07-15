from django.contrib import admin
from .models import Doctor, BankDetail, StipendRate, StipendSlip, Status, PaymentHistory, DocCounter

# Register your models here.
admin.site.register(Doctor),
admin.site.register(BankDetail),
admin.site.register(StipendRate),
admin.site.register(StipendSlip),
admin.site.register(Status),
admin.site.register(PaymentHistory),
admin.site.register(DocCounter),