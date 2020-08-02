from django import forms
from django.core.exceptions import ValidationError
from first_app.models import Employee, UserProfileInfo,Post
from django.contrib.auth.models import User


class MyReg_Form(forms.Form):

    def check_for_z(value):
        if value[0].lower() != 'z':
            raise ValidationError("Name needs to start with Z or z")

    name = forms.CharField(max_length=100,validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)
    botchatcher = forms.CharField(required=False, widget=forms.HiddenInput,)

    def Clean_botchatcher(self):
        botcatcher_len= self.cleaned_data["botchatcher"]
        if len(botcatcher_len) > 0:
            print("Caught botchatcher successfully")
            raise forms.ValidationError("gotcha bot")
        return botcatcher_len

    def clean(self):
        all_clean_data= super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise ValidationError("Make sure your email matches")

class Employee_Login_From(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ['Name', 'Organisation', 'Email']


class PostingForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['myTopic','post_title', 'myPost' ]

'''
    Below two forms deal with the registration functionality.
    1. User Form - Linked with the Django's default User model
    2. UserProfileInfoForm - Linked with the model UserProfileInfo
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']