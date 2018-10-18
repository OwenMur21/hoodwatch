from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Neighbour(models.Model):
    """
    Class that defines neighbourhood details
    """
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
            hood = Neighbour.objects.get(id=id)
            return hood

    
class Profile(models.Model):
    """
    Class that contains Profile details
    """
    name = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbour)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_user_by_hood(cls, id):
            profile = Profile.objects.filter(hood_id=id).all()
            return profile




    



