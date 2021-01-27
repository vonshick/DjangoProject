from django.db import models
from django.urls import reverse


class Position(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def get_absolute_url(self):
        return reverse('position_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.name)

