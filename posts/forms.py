from django import forms

from .models import House, Post, Tag

from django.forms.widgets import CheckboxSelectMultiple

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
            "title", "tags",
        ]

    #create multiple choice fields for tags
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()

    #save by first creating an id for the M2M
    # def save(self, commit=True):
    #     if (commit==True):
    #         post = super(PostForm, self).save()
    #         instance_tags = self.cleaned_data.get('tags')
    #         print(post)
    #         instance_post = post
    #     else:
    #         post = (PostForm, self).save(commit=False)
    #         return post

