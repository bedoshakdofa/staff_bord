from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Department(models.Model):
    D_name=models.CharField(max_length=30)

    def __str__(self):
        return self.D_name

class postion(models.Model):
    name=models.CharField(max_length=30)

    def __str__ (self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=11,null=True)
    img=models.ImageField(upload_to='profile',null=True)
    email=models.EmailField(null=True)
    website=models.URLField(null=True)
    # notional_id=models.CharField(max_length=14)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    postion=models.ForeignKey(postion,on_delete=models.CASCADE,null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user
