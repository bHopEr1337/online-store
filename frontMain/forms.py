from django import forms

class EmailContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    text_body = forms.CharField(label='Большой текст',
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 80,
                'style': 'font-size: 14px;'
            }
        ),
        help_text='Администратор отвечает в течение нескольких часов. Постарайтесь описать свою проблему наиболее развёрнуто')
    #to = forms.EmailField()