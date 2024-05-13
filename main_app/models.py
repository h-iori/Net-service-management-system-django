from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Assets(models.Model):
    pname = models.CharField(max_length=60)
    pdop = models.DateField()
    pavail = models.IntegerField()
    ptotal = models.IntegerField()
    poriginalcost = models.IntegerField()
    psellingcost = models.IntegerField()

    def __str__(self):
        return str(self.pname)


class Customer(models.Model):
    custname = models.CharField(max_length=60)
    custadd = models.CharField(max_length=60)
    cpname = models.CharField(max_length=60)
    cpquantity = models.IntegerField()
    cpeach = models.IntegerField()
    cptotal = models.IntegerField()
    cpdate = models.DateField()

    def __str__(self):
        return str(self.custname)

class UserLogin(models.Model):
    r_name = models.CharField(max_length=60)
    r_email = models.EmailField(max_length=60)
    r_password = models.CharField(max_length=60)

    def __str__(self):
        return str(self.r_name)

class SubmitRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_info = models.TextField()
    request_desc = models.TextField()
    requester_name = models.CharField(max_length=60)
    requester_add1 = models.TextField()
    requester_add2 = models.TextField()
    requester_city = models.CharField(max_length=60)
    requester_state = models.CharField(max_length=60)
    requester_zip = models.IntegerField()
    requester_email = models.EmailField(max_length=60)
    requester_mobile = models.BigIntegerField()
    request_date = models.DateField()

    def __str__(self):
        return str(self.request_id)

class Technician(models.Model):
    empName = models.CharField(max_length=60)
    empCity = models.CharField(max_length=60)
    empMobile = models.BigIntegerField()
    empEmail = models.EmailField(max_length=60)

    def __str__(self):
        return str(self.empName)
    
class AssignWork(models.Model):
    request = models.OneToOneField('SubmitRequest', on_delete=models.SET_NULL, default=None, null=True)
    request_info = models.TextField()
    request_desc = models.TextField()
    requester_name = models.CharField(max_length=60)
    requester_add1 = models.TextField()
    requester_add2 = models.TextField()
    requester_city = models.CharField(max_length=60)
    requester_state = models.CharField(max_length=60)
    requester_zip = models.IntegerField()
    requester_email = models.EmailField(max_length=60)
    requester_mobile = models.BigIntegerField()
    assign_tech = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True)
    assign_date = models.DateField()

    def __str__(self):
        return str(self.requester_name)

@receiver(post_save, sender=AssignWork)
def delete_submit_requests(sender, instance, created, **kwargs):
    if created and instance.request is not None:
        request_id = instance.request_id
        # Exclude the request_id field from deletion
        SubmitRequest.objects.filter(request_id=request_id).exclude(pk=instance.request_id).delete()