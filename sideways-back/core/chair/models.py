from django.db import models


class Chair(models.Model):  # data chair has when updated and when viewed.
    model = models.CharField(max_length=30)
    location = models.CharField(max_length=130)
    status = models.CharField(max_length=130)
    destination = models.CharField(max_length=130)

    def __str__(self):
        return f"{self.model}"
