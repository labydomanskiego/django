from django import forms
from django.db.models.base import Model
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelChoiceField

from news import models

from .models import News
from django.forms import ModelChoiceField


class TopicChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.topic


class NewsModifyForm(forms.Form):
    choices_ = News.objects.all()
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice = TopicChoiceField(required=True, label='Enter Type', label_suffix='>>>', initial='none',
                                          help_text='choose the type', disabled=False,
                                          queryset=choices_)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['topic', 'text', 'author']

