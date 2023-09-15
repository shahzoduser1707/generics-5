from django.db import models
from datetime import datetime
# Create your models here.


class RoomModel(models.Model):
    name = models.CharField(max_length=300,default='')
    size = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='write something pls!')

    class Meta:
        db_table = 'RoomModel'
    def __str__(self) -> str:
        return self.name