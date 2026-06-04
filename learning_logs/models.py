from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models is a module 
#a model is also a class
#Model below is the parent class in django that defines a models basic 
#...functionality
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of a model"""
        return self.text
#basically in models we use fields that describe the type of data stored in the
#... database and how django should deal with it
#argument auto_now_add=True tells django to automatically set this attribute to
#...the current date and time
class Entry(models.Model):
    """Something specific learned about the topic."""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text