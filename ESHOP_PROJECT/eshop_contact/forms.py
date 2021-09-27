from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'type': "text",
                'class': "form-control",
                'required': "required"
            }),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی نمی تواند بیشتر از ۱۵۰ کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید',
                   'class': "form-control",
                   'required': "required"
                   }),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل نمی تواند بیشتر از ۱۰۰ کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا موضوع خود را وارد کنید',
                   'class': "form-control",
                   'required': "required"
                   }),
        label='موضوع',
        validators=[
            validators.MaxLengthValidator(200, 'موضوع نمی تواند بیشتر از ۲۰۰ کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا متن خود را وارد کنید',
                   'id': "message",
                   'required': 'required',
                   'class': "form-control",
                   'rows': '8'
                   }),
        label='متن',
    )
