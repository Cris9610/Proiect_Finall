from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from utils.upload import store_uploaded_file
from users.models import Profile

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'company']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs["class"] = "input"
        self.fields["last_name"].widget.attrs["class"] = "input"
        self.fields["password"].widget.attrs["class"] = "input"
        self.fields["password_confirmation"].widget.attrs["class"] = "input"
        self.fields["email"].widget.attrs["class"] = "input"
        self.fields["phone_no"].widget.attrs["class"] = "input"
        self.fields["company"].widget.attrs["class"] = "input"


        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
        self.fields["password_confirmation"].widget.attrs["placeholder"] = "Password Confirmation"
        self.fields["phone_no"].widget.attrs["placeholder"] = "Phone No."
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["company"].widget.attrs["placeholder"] = "Company"

    password = forms.CharField(
        max_length=255,
        required=True,
        label='Password',
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html()
    )

    password_confirmation = forms.CharField(
        max_length=255,
        required=True,
        label='Confirm password',
        widget=forms.PasswordInput,
        help_text='Please confirm your password'
    )

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
        )

        validate_password(password, user=user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password not confirmed.')

        return password_confirmation

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')

        try:
            AuthUser.objects.get(phone_no=phone_no)
        except AuthUser.DoesNotExist:
            return phone_no

        raise forms.ValidationError('This phone number is already used.')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            AuthUser.objects.get(email=email)
        except AuthUser.DoesNotExist:
            return email

        raise forms.ValidationError('This email is already used.')

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.instance.set_password(password)

        return super().save(commit)


class UserImageForm(forms.Form):
    image = forms.ImageField(label='Incarca imaginea:', required=True)

    def save(self):
        image = self.cleaned_data.get('image')
        store_uploaded_file(image)


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
