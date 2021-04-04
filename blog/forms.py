from django import forms
from .models import Contact, Post


class ContactUs(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','message']        

# class PostPrivacy(forms.ModelForm):
#     class Meta:
#         POST_PRIVACY = (
#          ('PUB', 'Public'),
#          ('PRI', 'Private')
#         )
#         privacy = forms.ChoiceField(choices=POST_PRIVACY, widget=forms.RadioSelect())