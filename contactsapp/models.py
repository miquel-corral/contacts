# from django.db import models
import django.db.models


class Common(django.db.models.Model):
    """
    Abstract class for common attributes and behaviour
    """
    name = django.db.models.CharField(max_length=200, unique=True)
    # ...
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tag(Common):
    """
    Represents a TAG to categorize contacts
    """


class Contact(Common):
    """
    Represents a contact
    """
    first_name = django.db.models.CharField(max_length=50, null=True, blank=True)
    last_name = django.db.models.CharField(max_length=200, null=True, blank=True)
    treatement = django.db.models.CharField(max_length=10, null=True, blank=True)
    organization = django.db.models.CharField(max_length=200, null=True, blank=True)
    position = django.db.models.CharField(max_length=200, null=True, blank=True)
    department = django.db.models.CharField(max_length=200, null=True, blank=True)
    email1 = django.db.models.EmailField(max_length=250, null=True, unique=False, blank=True)
    email2 = django.db.models.EmailField(max_length=250, null=True, unique=False, blank=True)
    telephone1 = django.db.models.CharField(max_length=50, null=True, blank=True)
    mobile1 = django.db.models.CharField(max_length=50, null=True, blank=True)
    mobile2 = django.db.models.CharField(max_length=50, null=True, blank=True)
    country = django.db.models.CharField(max_length=50, null=True, blank=True)
    state = django.db.models.CharField(max_length=50, null=True, blank=True)
    city = django.db.models.CharField(max_length=50, null=True, blank=True)
    street = django.db.models.CharField(max_length=200, null=True, blank=True)
    zip_code = django.db.models.CharField(max_length=50, null=True, blank=True)
    website = django.db.models.CharField(max_length=200, null=True, blank=True)
    tags = django.db.models.ManyToManyField(Tag)

