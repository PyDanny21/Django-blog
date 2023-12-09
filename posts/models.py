from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=2000)
    image=models.ImageField(upload_to='Media', blank=True)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
