from django import forms

from .models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price", "in_stock"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "rows": 3})
        self.fields["price"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["in_stock"].widget.attrs.update({"class": "form-check-input"})

    def clean_name(self):
        name = self.cleaned_data["name"]
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise forms.ValidationError(f"Запрещено использовать слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise forms.ValidationError(f"Запрещено использовать слово: {word}")
        return description

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной!")
        return price
