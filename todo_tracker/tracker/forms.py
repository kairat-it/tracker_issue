from django import forms
from .models import Issue, Status, Type


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'status': forms.ModelChoiceField(queryset=Status.objects.all()),
            'type': forms.ModelChoiceField(queryset=Type.objects.all()),
        }
