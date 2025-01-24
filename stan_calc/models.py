from django.db import models

class Payment(models.Model):
    sum_payments = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment: {self.sum_payments}"
