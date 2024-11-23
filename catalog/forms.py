from django.forms import ModelForm, ValidationError, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):

        clean_data = self.cleaned_data.get('name')

        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        for word in words:
            if word in clean_data:
                raise ValidationError('Содержит запрещенные слова')
        return clean_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, ModelForm):
    """ Форма модератора для публикации продукта """

    class Meta:
        model = Product
        fields = ('is_publication', 'depiction', 'category',)
