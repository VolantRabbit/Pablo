from django.db import models

class Payment(models.Model):
    sum_bills = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    internet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    electricity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    water = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    household = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def format_updated_at(self):
        return self.updated_at.strftime('%Y-%m-%d')

    def __str__(self):
        return (f" Total: {self.total} | Bills: {self.sum_bills} | Internet: {self.internet} | Electricity: {self.electricity} "
                f" | Water: {self.water} | Household: {self.household} | Date: {self.format_updated_at}")
