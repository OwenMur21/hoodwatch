from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Neighbour(models.Model):
    """
    Class that defines neighbourhood details
    """
    name = models.CharField(max_length = 30)
    loc = (
    ('Westlands', 'Westlands'),
    ('South b', 'South b'),
    ('South c', 'South c'),
    ('Langata', 'Langata'),
    ('Satelite', 'Satelite'),
    ('Buruburu', 'Buruburu'),
    ('Kinoo', 'Kinoo'),
    ('Donholm', 'Donholm'),
    ('Karen', 'Karen')
)
    description = models.TextField(default="My hood is cool")
    location = models.CharField(max_length = 30, choices=loc)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

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
    name = models.CharField(max_length = 30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbour, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_user_by_hood(cls, id):
        profile = Profile.objects.filter(hood_id=id).all()
        return profile


   
class Business(models.Model):
    """
    Class that contains Business details
    """
    name = models.CharField(max_length = 30)
    description = models.TextField(default="Check out my business")
    email = models.CharField(max_length = 30)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbour)

    def __str__(self):
        return self.name

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()

    @classmethod
    def get_by_bizid(cls, id):
        biz = Business.objects.get(id=id)
        return biz
            
    @classmethod
    def search_biz(cls, name):
        biz = cls.objects.filter(name__icontains=name)
        return biz

class Join(models.Model):
    """
    Class that contains monitors which users have joined which neighbourhoods
    """
    user = models.OneToOneField(User)
    hood = models.ForeignKey(Neighbour)

    def __str__(self):
        return self.user





  



    



