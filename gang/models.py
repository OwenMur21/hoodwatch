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


    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def get_hood_by_id(cls, id):
            hood = Neighbour.objects.get(id=id)
            return hood

    



