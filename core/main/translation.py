from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )



@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )



@register(Product)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', )