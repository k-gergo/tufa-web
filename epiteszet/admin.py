# epiteszet/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    EpiteszetCategory, EpiteszetProduct, EpiteszetProductImage,
    EpiteszetProductSpec, EpiteszetProductFeature, EpiteszetProductWhyChoose
)

# --- Inline Osztályok ---
class EpiteszetProductImageInline(admin.TabularInline):
    model = EpiteszetProductImage
    extra = 1
    readonly_fields = ['image_preview']
    def image_preview(self, obj):
        if obj.image: return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Előnézet'

class EpiteszetProductSpecInline(admin.TabularInline):
    model = EpiteszetProductSpec
    extra = 3

class EpiteszetProductFeatureInline(admin.TabularInline):
    model = EpiteszetProductFeature
    extra = 3

class EpiteszetProductWhyChooseInline(admin.TabularInline):
    model = EpiteszetProductWhyChoose
    extra = 2

# --- ModelAdmin Osztályok ---
@admin.register(EpiteszetCategory)
class EpiteszetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_hu', 'name_sk', 'order', 'product_count')
    ordering = ('order',)
    def product_count(self, obj): return obj.products.count()
    product_count.short_description = 'Termékek száma'

@admin.register(EpiteszetProduct)
class EpiteszetProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_hu', 'category', 'preview_image') # ID itt is hasznos lehet
    list_filter = ('category',)
    search_fields = ('name_hu', 'name_sk', 'intro_hu')
    fieldsets = (
        ('Alap információk', {
            'fields': ('category', 'name_hu', 'name_sk', 'intro_hu', 'intro_sk') # Itt is add hozzá az esetleges új mezőket
        }),
        ('PDF dokumentáció', {
            'fields': ('pdf_link_text_hu', 'pdf_link_text_sk', 'pdf_file'),
            'classes': ('collapse',),
        }),
        ('Záró szöveg', {
            'fields': ('closing_text_hu', 'closing_text_sk'),
            'classes': ('collapse',),
        }),
         ('Videó', {
            'fields': ('video_url',),
            'classes': ('collapse',),
        }),
    )
    inlines = [
        EpiteszetProductImageInline,
        EpiteszetProductSpecInline,
        EpiteszetProductFeatureInline,
        EpiteszetProductWhyChooseInline
    ]
    def preview_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image: return format_html('<img src="{}" width="100" height="auto" />', first_image.image.url)
        return "-"
    preview_image.short_description = 'Termék kép'