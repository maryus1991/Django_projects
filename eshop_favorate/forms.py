from django import forms


class FavorateItem(forms.Form):
    pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )
