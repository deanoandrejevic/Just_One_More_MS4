from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Creation of the Checkout form
    """
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
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
