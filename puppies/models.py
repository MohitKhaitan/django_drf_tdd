from django.db import models


class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        """
        To get the breed of the puppy
        :return: Breed form Puppy model
        """
        return self.name + ' belongs to ' + self.breed + ' breed.'

    def __repr__(self):
        """
        To view the representation of the model
        :return: Name from Puppy model
        """
        return self.name + ' is added'



