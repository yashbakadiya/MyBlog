from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    # POST_PRIVACY = (
    #      ('PUB', 'Public'),
    #      ('PRI', 'Private')
    #     )
    # privacy = models.CharField(default='PUB' ,choices=POST_PRIVACY, max_length=120)
    privacy = models.TextChoices('prv','Public Private')
    privacy = models.CharField(default='Public' , max_length=20, choices=privacy.choices)
    category = models.TextChoices('cat','---Select--- Food Music Nature Education Wedding Travel Movie Car Project Photography Other')
    category = models.CharField(default ='---Select---',max_length=20, choices=category.choices)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('my_blog')
        # return reverse('post-detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=43)
    message = models.TextField()

    def __str__(self):
        return self.name