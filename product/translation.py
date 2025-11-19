from modeltranslation.translator import register, TranslationOptions

from product.models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

