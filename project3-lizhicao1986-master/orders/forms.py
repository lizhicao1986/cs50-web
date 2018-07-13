from django import forms
from .models import order

CATEGORIES = (
    ('REG', 'Reular'),
    ('SIC', 'Sicilian'),
    ('SUB', 'Sub'),
    ('PAS', 'Pasta'),
	('SAL', 'Salad'),
	('PLA', 'Platter')
)
SIZE = (
    ('SM', 'Small'),
    ('LG', 'Large'),
)


class orderForm(forms.ModelForm):
    error_css_class = 'error'

    category = forms.ChoiceField(choices=CATEGORIES, required=True )
    size = forms.ChoiceField(choices=SIZE, required=False )

    class Meta:
        model = order

        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'What type of menu item?'}),
            'size': forms.TextInput(attrs={'placeholder': 'what size?'}),

        }
