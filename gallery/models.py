# gallery/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _ # Fordításhoz

class GalleryImage(models.Model):
    """Egy kép a galériában."""
    title_hu = models.CharField(
        _("Cím (Magyar)"),
        max_length=200,
        blank=True, # Nem kötelező megadni
        help_text=_("A képhez tartozó rövid cím vagy felirat (opcionális).")
    )
    title_sk = models.CharField(
        _("Cím (Szlovák)"),
        max_length=200,
        blank=True,
        help_text=_("A képhez tartozó rövid cím vagy felirat szlovákul (opcionális).")
    )
    image = models.ImageField(
        _("Képfájl"),
        upload_to='gallery/', # A 'media/gallery/' mappába menti a képeket
        help_text=_("Válassza ki a feltöltendő képfájlt.")
    )
    alt_text_hu = models.CharField(
        _("Alternatív szöveg (Magyar)"),
        max_length=255,
        blank=True,
        help_text=_("Rövid leírás a képről (akadálymentesítéshez és SEO-hoz, opcionális).")
    )
    alt_text_sk = models.CharField(
        _("Alternatív szöveg (Szlovák)"),
        max_length=255,
        blank=True,
        help_text=_("Rövid leírás a képről szlovákul (opcionális).")
    )
    uploaded_at = models.DateTimeField(
        _("Feltöltés ideje"),
        auto_now_add=True # Automatikusan beállítja a feltöltés idejét
    )
    order = models.PositiveIntegerField(
        _("Sorrend"),
        default=0,
        db_index=True, # Gyorsítja a sorrendezést
        help_text=_("Meghatározza a képek megjelenési sorrendjét (kisebb szám előrébb).")
    )

    class Meta:
        verbose_name = _("Galéria kép")
        verbose_name_plural = _("Galéria képek")
        ordering = ['order', '-uploaded_at'] # Sorrendezés először 'order' szerint, majd a legújabbak elöl

    def __str__(self):
        # Ha van cím, azt írjuk ki, ha nincs, akkor a fájlnevet
        return self.title_hu or self.image.name.split('/')[-1]