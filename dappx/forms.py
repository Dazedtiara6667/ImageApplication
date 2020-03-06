from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from dappx.models import Comment
from dappx.models import Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []
    zip = forms.FileField(required=False)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')