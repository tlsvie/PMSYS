from django import forms


# class LoginForm(forms.Form):
#     COLORS = [
#         ['红','红'],
#         ['黄','黄'],
#         ['绿','绿'],
#         ['紫','紫'],
#     ]
#     user_name = forms.CharField(label="姓名", max_length=20)
#     user_color = forms.ChoiceField(label="幸运颜色", choices=COLORS)


class LoginForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=20)
    password = forms.ChoiceField(label="密码", widget=forms.PasswordInput())

