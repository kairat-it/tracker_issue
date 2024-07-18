from django import forms
from .models import Issue, Status, Type

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'status': forms.ModelChoiceField(queryset=Status.objects.all()),
            'types': forms.ModelMultipleChoiceField(queryset=Type.objects.all()),
        }
