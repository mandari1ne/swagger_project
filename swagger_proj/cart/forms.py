from django import forms

# для выпадающего списка
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)

    # для обновления количество, суммируется или новое
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
