from django.forms import ModelForm, NumberInput
from models import Materials


class MaterialsForm(ModelForm):

    class Meta:
        model = Materials
        fields = ('name', 'content',)
        widgets = {
            'views_count': NumberInput(
                attrs={'readonly': True, 'disabled': True}
            )
        }
