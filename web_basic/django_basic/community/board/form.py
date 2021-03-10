
from django import forms
from django.forms.fields import CharField


class BoardForm(forms.Form):
    title = CharField(error_messages={'required': "제목을 입력해주세요"
                                      }, max_length=128, label="제목")
    contents = CharField(error_messages={
        'required': "내용을 입력해주세요"
    }, widget=forms.Textarea, label="내용")
