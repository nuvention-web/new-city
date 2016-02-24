from django import forms

from .models import House, Post, Tag

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            "title",
            "content",
            "address",
            "price",
            "beds",
            "baths",
            "pet_allowed",
            "has_parking",
            "has_laundry",
            "has_pool",
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "tags",
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
            "content",
        ]

