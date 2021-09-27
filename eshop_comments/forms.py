from django import forms
from django.core import validators


class CommentsForms(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید',

                   })

    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید',
                   }),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا نظر خود را وارد کنید',
                   'rows': '8'
                   }),
    )
    productid = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('ایمیل وارد شده معتبر نمی باشد')
        elif len(email) < 5:
            raise forms.ValidationError('ایمیل وارد شده معتبر نمی باشد')

        return email

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) <= 1:
            raise forms.ValidationError('لطفا نظر خود را بنویسید')
        return text


class SubmitForEditCommentsForms(forms.Form):
    commentid = forms.IntegerField(
        widget=forms.HiddenInput()
    )


class EditCommentsForms(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید',

                   })

    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید',
                   }),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )
    commentid = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا نظر خود را وارد کنید',
                   'rows': '8'
                   }),
    )
    productid = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('ایمیل وارد شده معتبر نمی باشد')
        elif len(email) < 5:
            raise forms.ValidationError('ایمیل وارد شده معتبر نمی باشد')

        return email

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) <= 1:
            raise forms.ValidationError('لطفا نظر خود را بنویسید')
        return text
