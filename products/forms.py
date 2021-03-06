from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """
    Form creation for adding product
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "border-black rounded-0"


class ReviewForm(forms.ModelForm):
    """
    Form creation for user reviews
    """
    class Meta:
        model = Review
        exclude = ('product', 'user')
