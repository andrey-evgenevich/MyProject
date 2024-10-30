from django import forms
from models import Materials


class MaterialsForm(forms.ModelForm):

    class Meta:
        model = Materials
        fields = ('name', 'content',)
        widgets = {
            'views_count': forms.NumberInput(
                attrs={'readonly': True, 'disabled': True}
            )
        }
