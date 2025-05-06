# blog/models.py
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# --- Category modell marad változatlan ---
class Category(models.Model):
    name_hu = models.CharField(max_length=100, verbose_name="Név (HU)")
    name_sk = models.CharField(max_length=100, verbose_name="Név (SK)", blank=True,
                               help_text="Ha üres, a magyar név jelenik meg.")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL slug",
                            help_text="Automatikusan generálódik a magyar névből, ha üres.")

    class Meta:
        verbose_name = "Blog Kategória"
        verbose_name_plural = "Blog Kategóriák"
        ordering = ['name_hu']

    def __str__(self):
        return self.name_hu

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name_hu)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


# --- BlogPost modell módosítása ---
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Vázlat'),
        ('published', 'Közzétéve'),
    )

    # Core Fields
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts',
                                 verbose_name="Kategória", null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL slug", blank=True,
                            help_text="Automatikusan generálódik a magyar címből, ha üres.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Állapot")

    # Magyar tartalom
    title_hu = models.CharField(max_length=200, verbose_name="Cím (HU)")
    excerpt_hu = models.TextField(blank=True, null=True, verbose_name="Bevezető (HU)")
    content_hu = models.TextField(verbose_name="Szövegtörzs (HU)", help_text="Formázható szöveg.")

    # Szlovák tartalom
    title_sk = models.CharField(max_length=200, verbose_name="Cím (SK)", blank=True, null=True)
    excerpt_sk = models.TextField(blank=True, null=True, verbose_name="Bevezető (SK)")
    content_sk = models.TextField(verbose_name="Szövegtörzs (SK)", blank=True, null=True, help_text="Formázható szöveg.")

    # Média
    featured_image = models.ImageField(upload_to='blog/featured/%Y/%m/', blank=True, null=True,
                                       verbose_name="Fő kép (Lista & Hero)")
    # !!! gallery_images ManyToManyField eltávolítva innen !!!
    video_url = models.URLField(blank=True, null=True, verbose_name="Videó URL (YouTube, Vimeo)",
                                help_text="Ha megadod, a tartalom fölött megjelenhet.")

    # Timestamps
    published = models.DateTimeField(default=timezone.now, verbose_name="Publikálás dátuma")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás dátuma")
    updated = models.DateTimeField(auto_now=True, verbose_name="Utolsó módosítás")

    class Meta:
        verbose_name = "Blog Bejegyzés"
        verbose_name_plural = "Blog Bejegyzések"
        ordering = ['-published']

    def __str__(self):
        return self.title_hu

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title_hu) if self.title_hu else 'bejegyzes'
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


# --- ÚJ Modell a galéria képekhez ---
class PostGalleryImage(models.Model):
    """Egy kép a BlogPost galériájában."""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='gallery_images', verbose_name="Bejegyzés")
    image = models.ImageField(upload_to='blog/gallery/%Y/%m/', verbose_name="Képfájl")


    class Meta:
        verbose_name = "Galéria kép (bejegyzéshez)"
        verbose_name_plural = "Galéria képek (bejegyzéshez)"
        ordering = ['id'] # Vagy más sorrend, ha kell

    def __str__(self):
        # Rövid névként visszaadja a képfájl nevét
        return self.image.name.split('/')[-1] if self.image else "Nincs kép"


