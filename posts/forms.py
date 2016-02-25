from django import forms

from .models import House, Post

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

class QuestionnaireForm1(forms.Form):
    school = forms.CharField(max_length=50)

class QuestionnaireForm2(forms.Form):
    hometown= forms.CharField(max_length=50)

class QuestionnaireForm3(forms.Form):
    job = forms.CharField(max_length=50)

