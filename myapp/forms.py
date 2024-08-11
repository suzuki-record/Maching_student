# myapp/forms.py
from django import forms
from .models import UserProfile

class QualificationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['qualification']
        widgets = {
            'qualification': forms.TextInput(attrs={'placeholder': '例: 基本情報技術者'}),
        }
        labels = {
            'qualification': '学習中の資格'
        }
