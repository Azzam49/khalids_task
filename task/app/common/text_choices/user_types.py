from django.db import models

class UserTypeOption(models.TextChoices):
    ADMIN = 'Admin', 'ADMIN'
    STAFF = 'Staff', 'STAFF'