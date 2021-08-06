from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):

    user_id = forms.CharField(
        label = '아이디',
        required=True,
        error_messages={'required': '아이디를 입력해주세요'}
    )

    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        error_messages={'required': '비밀번호를 입해주세요'}
    )

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pw'
        ]