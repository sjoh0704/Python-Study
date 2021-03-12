
from django import forms
from django.contrib.auth.hashers import check_password
from django.forms.fields import CharField
from .models import Fcuser


class LoginForm(forms.Form):
    username = CharField(error_messages={'required': "아이디를 입력해주세요"
                                         }, max_length=32, label="사용자 이름")
    password = CharField(error_messages={
        'required': "비밀번호를 입력해주세요"
    }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            try:

                fcuser = Fcuser.objects.get(username=username)

            except:
                self.add_error("username",  "아이디가 없습니다.")
                # 에러가 생기면 바로 isvalid로 리턴되는 듯하다
            else:

                if check_password(password, fcuser.password):
                    self.user_id = fcuser.id

                else:
                    self.add_error("password", "비밀번호가 틀립니다.")
