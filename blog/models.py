from django.db import models
from django.utils import timezone


class Post(models.Model): #defines our model * class indicates that the object is defined
#Post name of our model
#models.,odel the model is a Django Model so Django saves in Database
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	#link to another model
    title = models.CharField(max_length=200)#defines only limited number od characters
    text = models.TextField()#no limit to the text
    created_date = models.DateTimeField(
            default=timezone.now)#date and time
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
