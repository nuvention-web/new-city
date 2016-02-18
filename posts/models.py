from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=64, error_messages={'required': 'Please specify the city!', })
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Address(models.Model):
    street = models.CharField(max_length=128, error_messages={'required': 'Please specify the street name!', })
    city = models.ForeignKey(City)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.street, self.city)


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.ForeignKey(Address, null=True)
    birthday = models.DateField(null=True, error_messages={'invalid': "Please enter a correct date format"})
    picture = models.BinaryField(null=True)
    friends = models.ManyToManyField('self', through='Friendship',
                                     symmetrical=False)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_active = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)


class Subletter(models.Model):
    profile = models.OneToOneField(UserProfile)


class Tenant(models.Model):
    profile = models.OneToOneField(UserProfile)


class House(models.Model):
    subletter = models.OneToOneField(Subletter)
    address = models.OneToOneField(Address)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.subletter


class Friendship(models.Model):
    user_source = models.ForeignKey(UserProfile, related_name='user_source')
    user_target = models.ForeignKey(UserProfile, related_name='user_target')
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=100)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='post_user_profile')
    house = models.OneToOneField(House)
    tags = models.ManyToManyField(Tag, through='PostTag')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)


