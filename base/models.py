from django.db import models
from login.models import User
from django.urls import reverse
from cryptography.fernet import Fernet


class AccountDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accountdetails', null=True)
    website = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.BinaryField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    encryption_key = models.BinaryField(null=True)

    def save(self, *args, **kwargs):
        if not self.encryption_key:
            self.encryption_key = Fernet.generate_key()

        fernet = Fernet(self.encryption_key)
        self.password = fernet.encrypt(self.password.encode())

        super().save(*args, **kwargs)

    def get_password(self):
        # Create a Fernet object with the encryption key
        fernet = Fernet(self.encryption_key)

        # Decrypt the password and return it as a string
        return fernet.decrypt(bytes(self.password)).decode()

    def __str__(self):
        return self.website

    def get_absolute_url(self):
        return reverse('base:detail', kwargs={'id': self.id})

    def get_absolute_url1(self):
        return reverse('base:delete', kwargs={'id': self.id})

    def get_absolute_url2(self):
        return reverse('base:update', kwargs={'id': self.id})
