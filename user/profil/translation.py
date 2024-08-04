from django.contrib import admin
from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(UserProfile)
class BookTranslationOptions(TranslationOptions):
    fields = ('bio',)