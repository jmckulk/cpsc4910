from django.db import models

# Account: stores user login information (user name, password, security questions, etc.)
class Account(models.Model):
	account_name = models.CharField(max_length=100, null=False, blank=False)