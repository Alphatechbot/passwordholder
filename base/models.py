from django.db import models
from login.models import User
from django.urls import reverse


class AccountDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accountdetails', null=True)
    website = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website

    def get_absolute_url(self):
        return reverse('base:detail', kwargs={'id': self.id})

    def get_absolute_url1(self):
        return reverse('base:delete', kwargs={'id': self.id})

    def get_absolute_url2(self):
        return reverse('base:update', kwargs={'id': self.id})
