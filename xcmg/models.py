# xcmg/models.py
from django.db import models

class XcmgCategory(models.Model):
    """XCMG gép kategória modell"""
    name_hu = models.CharField(max_length=100, verbose_name="Kategória neve (HU)")
    name_sk = models.CharField(max_length=100, verbose_name="Kategória neve (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "XCMG Gép Kategória"
        verbose_name_plural = "XCMG Gép Kategóriák"
        ordering = ['order']

    def __str__(self):
        return self.name_hu

class XcmgProduct(models.Model):
    """XCMG gép termék modell"""
    category = models.ForeignKey(XcmgCategory, on_delete=models.CASCADE, related_name="products", verbose_name="Kategória")
    name_hu = models.CharField(max_length=200, verbose_name="Termék neve (HU)")
    name_sk = models.CharField(max_length=200, verbose_name="Termék neve (SK)")
    intro_hu = models.TextField(verbose_name="Bevezető szöveg (HU)", blank=True)
    intro_sk = models.TextField(verbose_name="Bevezető szöveg (SK)", blank=True)
    closing_text_hu = models.TextField(blank=True, verbose_name="Záró szöveg (HU)")
    closing_text_sk = models.TextField(blank=True, verbose_name="Záró szöveg (SK)")
    pdf_link_text_hu = models.CharField(max_length=100, default="Leírás itt!", verbose_name="PDF link szövege (HU)")
    pdf_link_text_sk = models.CharField(max_length=100, default="[SK] Popis tu!", verbose_name="PDF link szövege (SK)")
    pdf_file = models.FileField(upload_to='xcmg/pdfs/', blank=True, null=True, verbose_name="PDF Fájl")
    video_url = models.URLField(blank=True, null=True, verbose_name="YouTube videó URL")

    class Meta:
        verbose_name = "XCMG Gép"
        verbose_name_plural = "XCMG Gépek"
        ordering = ['category__order', 'name_hu']

    def __str__(self):
        return self.name_hu

# --- Kapcsolódó modellek ---

class XcmgProductImage(models.Model):
    product = models.ForeignKey(XcmgProduct, on_delete=models.CASCADE, related_name="images", verbose_name="Termék")
    image = models.ImageField(upload_to='xcmg/pics/', verbose_name="Kép")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "XCMG Gép Kép"
        verbose_name_plural = "XCMG Gép Képek"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - Kép {self.order}"

class XcmgProductSpec(models.Model):
    product = models.ForeignKey(XcmgProduct, on_delete=models.CASCADE, related_name="tech_specs", verbose_name="Termék")
    spec_hu = models.CharField(max_length=255, verbose_name="Műszaki adat (HU)")
    spec_sk = models.CharField(max_length=255, verbose_name="Műszaki adat (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "XCMG Gép Műszaki Adat"
        verbose_name_plural = "XCMG Gép Műszaki Adatok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.spec_hu[:30]}"

class XcmgProductFeature(models.Model):
    product = models.ForeignKey(XcmgProduct, on_delete=models.CASCADE, related_name="features", verbose_name="Termék")
    feature_hu = models.CharField(max_length=255, verbose_name="Jellemző (HU)")
    feature_sk = models.CharField(max_length=255, verbose_name="Jellemző (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "XCMG Gép Jellemző"
        verbose_name_plural = "XCMG Gép Jellemzők"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.feature_hu[:30]}"

class XcmgProductWhyChoose(models.Model):
    product = models.ForeignKey(XcmgProduct, on_delete=models.CASCADE, related_name="why_choose", verbose_name="Termék")
    reason_hu = models.CharField(max_length=255, verbose_name="Ok (HU)")
    reason_sk = models.CharField(max_length=255, verbose_name="Ok (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "XCMG Gép Miért Válassza"
        verbose_name_plural = "XCMG Gép Miért Válassza Okok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.reason_hu[:30]}"