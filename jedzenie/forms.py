from django.forms import ModelChoiceField

from jedzenie.models import Jedzenie
from django import forms

class JedzenieChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.danie


class JedzenieModifyForm(forms.Form):
    choices_ = Jedzenie.objects.all()
    kcal = forms.IntegerField()
    smaczne = forms.BooleanField()
    choice = JedzenieChoiceField(required=True, label='Enter Type', label_suffix='>>>', initial='none',
                                          help_text='choose the type', disabled=False,
                                          queryset=choices_)
class JedzenieForm(forms.ModelForm):
    class Meta:
        model = Jedzenie
        fields = ['danie', 'kcal', 'smaczne']