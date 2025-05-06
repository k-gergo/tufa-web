# forestry/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ForestryCategory, ForestryProduct, ForestryProductImage,
    ForestryProductSpec, ForestryProductFeature, ForestryProductWhyChoose
)

# --- Inline Osztályok ---
class ForestryProductImageInline(admin.TabularInline):
    model = ForestryProductImage
    extra = 1
    readonly_fields = ['image_preview']
    def image_preview(self, obj):
        if obj.image: return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Előnézet'

class ForestryProductSpecInline(admin.TabularInline):
    model = ForestryProductSpec
    extra = 3

class ForestryProductFeatureInline(admin.TabularInline):
    model = ForestryProductFeature
    extra = 3

class ForestryProductWhyChooseInline(admin.TabularInline):
    model = ForestryProductWhyChoose
    extra = 2

# --- ModelAdmin Osztályok ---
@admin.register(ForestryCategory)
class ForestryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_hu', 'name_sk', 'order', 'product_count')
    ordering = ('order',)
    def product_count(self, obj): return obj.products.count()
    product_count.short_description = 'Termékek száma'

@admin.register(ForestryProduct)
class ForestryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_hu', 'category', 'preview_image')
    list_filter = ('category',)
    search_fields = ('name_hu', 'name_sk', 'intro_hu')
    fieldsets = (
        ('Alap információk', {
            'fields': ('category', 'name_hu', 'name_sk', 'intro_hu', 'intro_sk') # Add itt a többi mezőt is (pl. manufacturer, price) ha hozzáadtad a modellhez
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
        ForestryProductImageInline,
        ForestryProductSpecInline,
        ForestryProductFeatureInline,
        ForestryProductWhyChooseInline
    ]
    def preview_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image: return format_html('<img src="{}" width="100" height="auto" />', first_image.image.url)
        return "-"
    preview_image.short_description = 'Termék kép'