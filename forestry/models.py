# forestry/models.py
from django.db import models

class ForestryCategory(models.Model):
    """Erdészeti gép kategória modell"""
    name_hu = models.CharField(max_length=100, verbose_name="Kategória neve (HU)")
    name_sk = models.CharField(max_length=100, verbose_name="Kategória neve (SK)")
    # Esetleg hozzáadhatsz egy leírást vagy képet a kategóriához, ha kell
    # description_hu = models.TextField(blank=True, verbose_name="Leírás (HU)")
    # description_sk = models.TextField(blank=True, verbose_name="Leírás (SK)")
    # image = models.ImageField(upload_to='forestry/categories/', blank=True, null=True, verbose_name="Kategória kép")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Erdészeti Gépkategória"
        verbose_name_plural = "Erdészeti Gépkategóriák"
        ordering = ['order']

    def __str__(self):
        return self.name_hu

class ForestryProduct(models.Model):
    id = models.AutoField(primary_key=True)  # Add hozzá ezt a sort
    category = models.ForeignKey(ForestryCategory, on_delete=models.CASCADE, related_name="products", verbose_name="Kategória")
    video_url = models.URLField(blank=True, null=True, verbose_name="YouTube videó URL")


    """Erdészeti termék modell"""
    # Nem kell külön id = models.AutoField(primary_key=True), a Django ezt automatikusan ad
    category = models.ForeignKey(ForestryCategory, on_delete=models.CASCADE, related_name="products", verbose_name="Kategória")
    name_hu = models.CharField(max_length=200, verbose_name="Termék neve (HU)")
    name_sk = models.CharField(max_length=200, verbose_name="Termék neve (SK)")
    intro_hu = models.TextField(verbose_name="Bevezető szöveg (HU)", blank=True) # Legyen opcionális?
    intro_sk = models.TextField(verbose_name="Bevezető szöveg (SK)", blank=True) # Legyen opcionális?
    # Lehetnek itt további specifikus mezők erdészeti gépekhez
    # pl. gyártó, állapot (új/használt), ár stb.
    # manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Gyártó")
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Ár")
    closing_text_hu = models.TextField(blank=True, verbose_name="Záró szöveg (HU)")
    closing_text_sk = models.TextField(blank=True, verbose_name="Záró szöveg (SK)")
    pdf_link_text_hu = models.CharField(max_length=100, default="Leírás itt!", verbose_name="PDF link szövege (HU)")
    pdf_link_text_sk = models.CharField(max_length=100, default="[SK] Popis tu!", verbose_name="PDF link szövege (SK)")
    pdf_file = models.FileField(upload_to='forestry/pdfs/', blank=True, null=True, verbose_name="PDF Fájl")


    class Meta:
        verbose_name = "Erdészeti Gép"
        verbose_name_plural = "Erdészeti Gépek"
        ordering = ['category__order', 'name_hu'] # Sorrend kategória szerint, azon belül név szerint

    def __str__(self):
        return self.name_hu

# --- Kapcsolódó modellek (hasonlóan a main_app-hoz) ---

class ForestryProductImage(models.Model):
    product = models.ForeignKey(ForestryProduct, on_delete=models.CASCADE, related_name="images", verbose_name="Termék")
    image = models.ImageField(upload_to='forestry/pics/', verbose_name="Kép") # Külön mappa a képeknek
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Erdészeti Gép Kép"
        verbose_name_plural = "Erdészeti Gép Képek"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - Kép {self.order}"

class ForestryProductSpec(models.Model):
    product = models.ForeignKey(ForestryProduct, on_delete=models.CASCADE, related_name="tech_specs", verbose_name="Termék")
    spec_hu = models.CharField(max_length=255, verbose_name="Műszaki adat (HU)")
    spec_sk = models.CharField(max_length=255, verbose_name="Műszaki adat (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Erdészeti Gép Műszaki Adat"
        verbose_name_plural = "Erdészeti Gép Műszaki Adatok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.spec_hu[:30]}"

class ForestryProductFeature(models.Model):
    product = models.ForeignKey(ForestryProduct, on_delete=models.CASCADE, related_name="features", verbose_name="Termék")
    feature_hu = models.CharField(max_length=255, verbose_name="Jellemző (HU)")
    feature_sk = models.CharField(max_length=255, verbose_name="Jellemző (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Erdészeti Gép Jellemző"
        verbose_name_plural = "Erdészeti Gép Jellemzők"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.feature_hu[:30]}"

class ForestryProductWhyChoose(models.Model):
    product = models.ForeignKey(ForestryProduct, on_delete=models.CASCADE, related_name="why_choose", verbose_name="Termék")
    reason_hu = models.CharField(max_length=255, verbose_name="Ok (HU)")
    reason_sk = models.CharField(max_length=255, verbose_name="Ok (SK)")
    order = models.IntegerField(default=0, verbose_name="Sorrend")

    class Meta:
        verbose_name = "Erdészeti Gép Miért Válassza"
        verbose_name_plural = "Erdészeti Gép Miért Válassza Okok"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name_hu} - {self.reason_hu[:30]}"