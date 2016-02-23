from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# from django.core.urlresolvers import reverse

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
        return u'%s, %s' % (self.street, self.city)


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.ForeignKey(Address, null=True, blank=True)
    birthday = models.DateField(error_messages={'invalid': "Please enter a correct date format"}, null=True, blank=True)
    picture = models.BinaryField(null=True)
    friends = models.ManyToManyField('self', through='Friendship',
                                     symmetrical=False)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    last_active = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)


class Subletter(models.Model):
    profile = models.OneToOneField(UserProfile)


class Tenant(models.Model):
    profile = models.OneToOneField(UserProfile)


class House(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.TextField(max_length=1000, default="")
    #How shoulld users input address
    address = models.OneToOneField(Address, default="", null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    beds = models.PositiveIntegerField(default=0)
    baths = models.PositiveIntegerField(default=0)
    pet_allowed = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_laundry = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Friendship(models.Model):
    user_source = models.ForeignKey(UserProfile, related_name='user_source')
    user_target = models.ForeignKey(UserProfile, related_name='user_target')
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='post_user_profile', blank=True, null=True)
    title = models.CharField(max_length=100, default="")
    house = models.OneToOneField(House, null=True, blank=True)
    tags = models.ManyToManyField(Tag, through='PostTag', blank=True)
    created_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_tags(self):
        return ",".join([str(tag) for tag in self.tags.all()])

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def get_user(self):
        return self.user

    def get_absolute_url(self):
    #     return reverse("details", kwargs={"user": self.user})
        return "posts/%s" %(self.id)


class PostTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)


