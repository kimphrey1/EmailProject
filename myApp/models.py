from django.db import models

# Create your models here.

# emaily/models.py

class Recipient(models.Model):
    first_name = models.CharField(max_length=100)
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True, null=True)

class CCRecipient(models.Model):
    email = models.EmailField()
