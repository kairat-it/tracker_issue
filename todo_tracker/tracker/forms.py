from django import forms
from .models import Issue, Status, Type


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        labels = {
            'summary': 'Описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'types': 'Типы задач'
        }
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'types': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")