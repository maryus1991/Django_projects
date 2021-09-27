from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        username = self.cleaned_data.get('user_name')
        is_exist_user = User.objects.filter(username=username).exists()
        if not is_exist_user:
            raise forms.ValidationError('کاربر یافت نشد')
        return username


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(25, 'تعداد کاراکترهای وارد شده در نام کاربری نمی تواند بیشتر از ۲۵ باشد'),
            validators.MinLengthValidator(3, 'تعداد کاراکترهای وارد شده در نام کاربری نمی تواند کمتر از ۳ باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور',
        validators=[
            validators.MinLengthValidator(8, 'حداقل کلمه عبور شما نمی تواند کمتر از ۸ کاراکتر باشد')
        ]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'لطفا کلمه عبور خود را دوباره وارد کنید'}),
        label='تکرار کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_user_exists = User.objects.filter(username=user_name).exists()
        if is_user_exists:
            raise forms.ValidationError('این کاربر قبلا ثبت نام شده است')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_db = User.objects.filter(email=email).exists()
        if email_db:
            raise forms.ValidationError('کاربری قبلا با این ایمیل ثبت نام کرده است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور باید مشابه هم باشند')

        return password
