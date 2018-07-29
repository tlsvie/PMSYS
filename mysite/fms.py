from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    CITY=[
        ['BJ','beijing'],
        ['TJ','tianjin'],
        ['NJ','nanjing'],
        ['HB','harbin'],
    ]

    user_name = forms.CharField(label="姓名", max_length=30)
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_school = forms.BooleanField(label="是否上学",required=False)
    user_email = forms.EmailField(label="电子邮件")
    user_message = forms.CharField(label='您的意见',widget=forms.Textarea)
    captcha = CaptchaField(label="请输入")

