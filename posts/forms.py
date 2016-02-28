from django import forms

from .models import House, Post, Tag, UserProfile

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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "gender", "school", "hometown", "job",
        ]
        widgets = {
            "gender": forms.TextInput(
                        attrs={'id': 'filter-gender', 'placeholder': 'M or F'}
                    ),
        }

#Form Wizard
class QuestionnaireForm1(forms.Form):
    school = forms.CharField(max_length=50)

class QuestionnaireForm2(forms.Form):
    hometown= forms.CharField(max_length=50)

class QuestionnaireForm3(forms.Form):
    job = forms.CharField(max_length=50)

class CityForm(forms.Form):
    initial_city = forms.CharField(max_length=50) 
