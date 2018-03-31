from django.db import models


class Payment(models.Model):
    mobile_number = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    till_number = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    transaction_ref_no = models.CharField(max_length=20, unique=True)
    served_by = models.CharField(max_length=20, blank=True)
    customer_name = models.CharField(max_length=50, blank=True)
    additional_info = models.CharField(max_length=25, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_ref_no


    class Meta:
        unique_together = ('mobile_number', 'timestamp')
