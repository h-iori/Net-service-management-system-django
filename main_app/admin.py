from django.contrib import admin
from .models import Assets, AssignWork, Customer, UserLogin, SubmitRequest, Technician

# Register your models here.
admin.site.register(Assets)
admin.site.register(AssignWork)
admin.site.register(Customer)
admin.site.register(UserLogin)
admin.site.register(SubmitRequest)
admin.site.register(Technician)

