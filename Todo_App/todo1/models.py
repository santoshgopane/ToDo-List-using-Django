from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.conf import settings
class List(models.Model):
    # sno = models.AutoField(primary_key = True)
    item = models.CharField(max_length=30)
    # completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    object = models.Manager()

    def __str__(self):
        return self.item