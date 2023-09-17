from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class RoomModel(models.Model):
    name = models.CharField(max_length=300,default='')
    size = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='write something pls!')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'RoomModel'
    def __str__(self) -> str:
        return self.name