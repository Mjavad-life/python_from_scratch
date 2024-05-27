from django import forms
from .models import Mabhas , Mohtava

class MabhasForm(forms.ModelForm) :
    class Meta :
        model = Mabhas
        fields = ['text']
        labels = {'text': ''}


class MohtavaForm(forms.ModelForm) :
    class Meta :
        model = Mohtava
        fields = ['text']
        labels = {'text':''}
        widgets = {'text' : forms.Textarea(attrs={'cols' :80})}
        