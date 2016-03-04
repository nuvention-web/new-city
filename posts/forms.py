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
            "title",
        ]

    #create multiple choice fields for tags
    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)

    #     self.fields["tags"].widget = CheckboxSelectMultiple()
    #     self.fields["tags"].queryset = Tag.objects.all()

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)

#NOT USED CURRENTLY
class FilterRoommateForm(forms.Form):
    gender = forms.ChoiceField(widget=forms.RadioSelect(
                                attrs={'id': 'filter-gender'}),
                                choices=SEX)

    # def __init__(self, *args, **kwargs):
    #     super(FilterRoommateForm, self).__init__(*args, **kwargs)
    #     self.fields['description'].widget = TextInput(attrs={
    #         'id': 'myCustomId',
    #         'class': 'myCustomClass',
    #         'name': 'myCustomName',
    #         'placeholder': 'myCustomPlaceholder'})

        # widgets = {
        #     "gender": forms.Select(
        #                 attrs={'id': 'filter-gender',},
        #                 choices= SEX)
        # }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "user",
            "school",
            "gender",
            "hometown",
            "city_to",
            "tags",
            "picture",
            "birthday",
        ]


#Form Wizard
# class QuestionnaireForm1(forms.Form):
#     school = forms.CharField(max_length=50)

# class QuestionnaireForm2(forms.Form):
#     hometown= forms.CharField(max_length=50)

# class QuestionnaireForm3(forms.Form):
#     job = forms.CharField(max_length=50)

class CityForm(forms.Form):
    initial_city = forms.CharField(max_length=50)

# class SignupForm(forms.Form):
