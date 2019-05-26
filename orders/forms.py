from django import forms
from django.core.exceptions import ValidationError

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['problem', 'description']

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise ValidationError("Description must be more then 5 symbols.")
        return description
