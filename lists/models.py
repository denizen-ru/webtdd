from django.db import models


class Item(models.Model):
    text = models.TextField(default='')

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.text
