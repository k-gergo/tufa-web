# gallery/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('order', 'image_preview', 'get_title', 'uploaded_at')
    list_display_links = ('image_preview',)
    list_editable = ('order',) # Engedélyezi a sorrend szerkesztését a listában
    list_filter = ('uploaded_at',) # Szűrés dátum alapján
    search_fields = ('title_hu', 'title_sk', 'alt_text_hu', 'alt_text_sk', 'image__icontains') # Keresés több mezőben
    fields = ('image', 'title_hu', 'title_sk', 'alt_text_hu', 'alt_text_sk', 'order', 'image_preview_detail') # Mezők sorrendje a szerkesztőben
    readonly_fields = ('image_preview_detail', 'uploaded_at') # Csak olvasható mezők a szerkesztőben
    ordering = ('order', '-uploaded_at') # Admin listában is ez a sorrend

    # Kép előnézet a listában
    @admin.display(description=_("Kép előnézet"))
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 60px; width: auto;" />', obj.image.url)
        return _("Nincs kép")

    # Kép előnézet a szerkesztő oldalon
    @admin.display(description=_("Jelenlegi kép"))
    def image_preview_detail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 400px; height: auto;" />', obj.image.url)
        return _("Nincs kép feltöltve")

    # Cím megjelenítése a listában (magyar vagy szlovák)
    @admin.display(description=_("Cím"))
    def get_title(self, obj):
        # Egyszerűsítve itt csak a magyart mutatjuk, de lehetne bonyolultabb logika
        return obj.title_hu or _("(Nincs cím)")