from django import form
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'email', 'mob_number', 'first_address_line',
                  'second_address_line', 'city', 'county', 'postcode',
                  'country',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'mob_number': 'Mobile Number',
            'first_address_line': '1st Address Line',
            'second_address_line': '2nd Address Line',
            'city': 'Town or City',
            'county': 'County',
            'postcode': 'Postcode',
            'country': 'Country',
        }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholder[field]} *'
        else:
            placeholder = placeholder[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.field[field].label = False