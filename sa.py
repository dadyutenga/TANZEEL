from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount', 'description', 'document', 'picture']
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': True}),
            'picture': forms.ClearableFileInput(attrs={'multiple': True}),
        }
