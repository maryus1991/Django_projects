from django import forms


class UserNewOrder(forms.Form):
    productid = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'type': "text",
                'class': "search_box",
                'style': '''
                            border: 1px solid #DEDEDC;
                            color: #696763;
                            font-family: 'BYekan', # sans-serif;
                            font-size: 20px;
                            font-weight: 700;
                            height: 33px;
                            outline: medium none;
                            text-align: center;
                            width: 50px;
                            '''
            }),
        initial=1
    )

class Coppone(forms.Form):
    coppone_input = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'type': "text", 
                'placeholder': "کد تخفیف خود را وارد نمایید ...",
            }
        )
    )