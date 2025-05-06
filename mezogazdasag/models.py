# mezogazdasag/models.py
from django.db import models

class MezogazdasagCategory(models.Model):
    """Mezőgazdasági gép kategória modell"""
    name_hu = models.CharField(max_length=100, verbose_name="Kategória neve (HU)")
    name_sk = models.CharField(max_length=100, verbose_name="Kategória neve (SK)")
    # description_hu = models.TextField(blank=True, verbose_name="Leírás (HU)")
    # description_sk = models.TextField(blank=True, verbose_name="Leírás (SK)")
    # image = models.ImageField(upload_to='mezogazdasag/categories/', blank=True, null=True, verbose_name="Kategória kép")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Mezőgazdasági Gépkategória"
        verbose_name_plural = "Mezőgazdasági Gépkategóriák"
        ordering = ['order']

    def __str__(self):
        return self.name_hu

class MezogazdasagProduct(models.Model):
    """Mezőgazdasági termék modell"""
    category = models.ForeignKey(MezogazdasagCategory, on_delete=models.CASCADE, related_name="products", verbose_name="Kategória")
    name_hu = models.CharField(max_length=200, verbose_name="Termék neve (HU)")
    name_sk = models.CharField(max_length=200, verbose_name="Termék neve (SK)")
    intro_hu = models.TextField(verbose_name="Bevezető szöveg (HU)", blank=True)
    intro_sk = models.TextField(verbose_name="Bevezető szöveg (SK)", blank=True)
    closing_text_hu = models.TextField(blank=True, verbose_name="Záró szöveg (HU)")
    closing_text_sk = models.TextField(blank=True, verbose_name="Záró szöveg (SK)")
    pdf_link_text_hu = models.CharField(max_length=100, default="Leírás itt!", verbose_name="PDF link szövege (HU)")
    pdf_link_text_sk = models.CharField(max_length=100, default="[SK] Popis tu!", verbose_name="PDF link szövege (SK)")
    pdf_file = models.FileField(upload_to='mezogazdasag/pdfs/', blank=True, null=True, verbose_name="PDF Fájl")
    video_url = models.URLField(blank=True, null=True, verbose_name="YouTube videó URL")

    class Meta:
        verbose_name = "Mezőgazdasági Gép"
        verbose_name_plural = "Mezőgazdasági Gépek"
        ordering = ['category__order', 'name_hu']

    def __str__(self):
        return self.name_hu

# --- Kapcsolódó modellek ---

class MezogazdasagProductImage(models.Model):
    product = models.ForeignKey(MezogazdasagProduct, on_delete=models.CASCADE, related_name="images", verbose_name="Termék")
    image = models.ImageField(upload_to='mezogazdasag/pics/', verbose_name="Kép")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Mezőgazdasági Gép Kép"
        verbose_name_plural = "Mezőgazdasági Gép Képek"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - Kép {self.order}"

class MezogazdasagProductSpec(models.Model):
    product = models.ForeignKey(MezogazdasagProduct, on_delete=models.CASCADE, related_name="tech_specs", verbose_name="Termék")
    spec_hu = models.CharField(max_length=255, verbose_name="Műszaki adat (HU)")
    spec_sk = models.CharField(max_length=255, verbose_name="Műszaki adat (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Mezőgazdasági Gép Műszaki Adat"
        verbose_name_plural = "Mezőgazdasági Gép Műszaki Adatok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.spec_hu[:30]}"

class MezogazdasagProductFeature(models.Model):
    product = models.ForeignKey(MezogazdasagProduct, on_delete=models.CASCADE, related_name="features", verbose_name="Termék")
    feature_hu = models.CharField(max_length=255, verbose_name="Jellemző (HU)")
    feature_sk = models.CharField(max_length=255, verbose_name="Jellemző (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Mezőgazdasági Gép Jellemző"
        verbose_name_plural = "Mezőgazdasági Gép Jellemzők"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.feature_hu[:30]}"

class MezogazdasagProductWhyChoose(models.Model):
    product = models.ForeignKey(MezogazdasagProduct, on_delete=models.CASCADE, related_name="why_choose", verbose_name="Termék")
    reason_hu = models.CharField(max_length=255, verbose_name="Ok (HU)")
    reason_sk = models.CharField(max_length=255, verbose_name="Ok (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Mezőgazdasági Gép Miért Válassza"
        verbose_name_plural = "Mezőgazdasági Gép Miért Válassza Okok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.reason_hu[:30]}"