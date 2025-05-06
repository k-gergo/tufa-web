# blog/admin.py
from django.contrib import admin
from .models import Category, BlogPost, PostGalleryImage # !!! PostGalleryImage importálva !!!
from django.db import models
from django.utils.html import format_html # Thumbnailhez

try:
    from ckeditor.widgets import CKEditorWidget
except ImportError:
    try:
        from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditorWidget
    except ImportError:
        # Fallback, ha egyik sincs (bár telepíteni kellene)
        from django.forms import Textarea as CKEditorWidget


#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('name_hu', 'name_sk', 'slug')
#    search_fields = ('name_hu', 'name_sk')
#    prepopulated_fields = {'slug': ('name_hu',)}
#    fields = ('name_hu', 'name_sk', 'slug')



# --- ÚJ Inline Admin a PostGalleryImage modellhez ---
class PostGalleryImageInline(admin.TabularInline): # Vagy StackedInline, ha úgy jobban tetszik
    model = PostGalleryImage
    extra = 1 # Hány üres sort mutasson alapból
    fields = ('image', 'get_thumbnail',) # Csak a kép és a bélyegkép
    readonly_fields = ('get_thumbnail',) # A bélyegkép csak olvasható
    verbose_name = "Galéria kép"
    verbose_name_plural = "Galéria képek"

    def get_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.image.url)
        return "Nincs kép"
    get_thumbnail.short_description = 'Bélyegkép'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title_hu', 'category', 'status', 'published', 'updated')
    list_filter = ('status', 'published', 'category', 'created', 'updated')
    search_fields = ('title_hu', 'title_sk', 'content_hu', 'content_sk', 'excerpt_hu', 'excerpt_sk')
    prepopulated_fields = {'slug': ('title_hu',)}
    date_hierarchy = 'published'
    ordering = ('-published',)

    # --- Az inlines most már az ÚJ PostGalleryImageInline-t használja ---
    inlines = [PostGalleryImageInline]

    # Fieldsetek maradnak, ahogy kérted
    fieldsets = (
        ('Publikálási Állapot és Kategória', {
            'fields': ('status', 'published', 'category')
        }),
        ('Fő Kép és Videó', {
            'fields': ('featured_image', 'video_url')
        }),
        ('Magyar Tartalom', {
            'classes': ('collapse',),
            'fields': ('title_hu', 'excerpt_hu', 'content_hu')
        }),
        ('Szlovák Tartalom', {
            'classes': ('collapse',),
            'fields': ('title_sk', 'excerpt_sk', 'content_sk')
        }),
        ('URL Beállítások', {
            'classes': ('collapse',),
            'fields': ('slug',),
            'description': "A 'slug' a bejegyzés URL-jének vége. Hagyd üresen az automatikus generáláshoz a magyar címből, vagy adj meg egyedit."
        }),
    )

    # CKEditor beállítása (marad)
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['content_hu', 'content_sk']:
            kwargs['widget'] = CKEditorWidget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)