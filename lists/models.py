from django.db import models
from django.urls import reverse


class List(models.Model):

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"

    def __str__(self):
        pass

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
