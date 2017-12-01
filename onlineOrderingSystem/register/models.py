from django.db import models

# CreateAccount: contains information for registering
class Account(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name