# main_app/management/commands/import_dummy_products.py
from django.core.management.base import BaseCommand
from main_app.views import DUMMY_PRODUCTS
from main_app.models import Category, Product, ProductSpec, ProductFeature, ProductWhyChoose, ProductImage

class Command(BaseCommand):
    help = 'Imports dummy product data from the views.py file to the database'

    def handle(self, *args, **options):
        # Kategóriák létrehozása
        categories = {
            'kompakt_rakodo': Category.objects.create(name_hu="Gumikerekes csúszókormányzású kompakt rakodó", name_sk="Rýpadlá", order=1),
            'forgokotro': Category.objects.create(name_hu="Forgókotró", name_sk="Nakladače", order=2),
            'urhenger': Category.objects.create(name_hu="Úthenger", name_sk="Cestné Valce", order=3),
            'kotrorakodo': Category.objects.create(name_hu="Kotrórakodó", name_sk="Teleskopické Nakladače", order=4),
            'homlokrakodo': Category.objects.create(name_hu="Homlokrakodó", name_sk="Grejdre", order=5),
        }
        
        self.stdout.write(self.style.SUCCESS('Kategóriák létrehozva.'))

        # Kategória hozzárendelés termék ID alapján
        category_map = {
            1: categories['forgokotro'],  # XE35E
            2: categories['kompakt_rakodo'],  # XC7-SV12
            3: categories['kompakt_rakodo'],  # XC7-TV12
            4: categories['kompakt_rakodo'],  # XC7-SR08
            5: categories['forgokotro'],  # XE20E
            6: categories['forgokotro'],  # XE27E
            7: categories['forgokotro'],  # XE55E
        }

        # Termékek importálása
        for product_id, data in DUMMY_PRODUCTS.items():
            # Termék kategória meghatározása
            category = category_map.get(product_id, categories['kompakt_rakodo'])
            
            # Termék létrehozása
            product = Product.objects.create(
                id=product_id,
                category=category,
                name_hu=data['name_hu'],
                name_sk=data['name_sk'],
                intro_hu=data['intro_hu'],
                intro_sk=data['intro_sk'],
                closing_text_hu=data.get('closing_text_hu', ''),
                closing_text_sk=data.get('closing_text_sk', ''),
                pdf_link_text_hu=data.get('pdf_link_text_hu', 'Leírás itt!'),
                pdf_link_text_sk=data.get('pdf_link_text_sk', '[SK] Popis tu!'),
                pdf_url=data.get('pdf_url', '')
            )
            
            # Képek hozzáadása
            for i, image_path in enumerate(data.get('images', [])):
                ProductImage.objects.create(
                    product=product,
                    image=image_path,  # Itt feltételezzük, hogy a media/pics/ mappában már léteznek
                    order=i
                )
            
            # Műszaki adatok hozzáadása
            for i, spec in enumerate(data.get('tech_specs_hu', [])):
                spec_sk = data.get('tech_specs_sk', [])[i] if i < len(data.get('tech_specs_sk', [])) else ''
                ProductSpec.objects.create(
                    product=product,
                    spec_hu=spec,
                    spec_sk=spec_sk,
                    order=i
                )
            
            # Jellemzők hozzáadása
            for i, feature in enumerate(data.get('features_hu', [])):
                feature_sk = data.get('features_sk', [])[i] if i < len(data.get('features_sk', [])) else ''
                ProductFeature.objects.create(
                    product=product,
                    feature_hu=feature,
                    feature_sk=feature_sk,
                    order=i
                )
            
            # "Miért válassza" okok hozzáadása
            for i, reason in enumerate(data.get('why_choose_hu', [])):
                reason_sk = data.get('why_choose_sk', [])[i] if i < len(data.get('why_choose_sk', [])) else ''
                ProductWhyChoose.objects.create(
                    product=product,
                    reason_hu=reason,
                    reason_sk=reason_sk,
                    order=i
                )
            
            self.stdout.write(self.style.SUCCESS(f'Termék importálva: {product.name_hu}'))

        self.stdout.write(self.style.SUCCESS('Összes termék importálása sikeres!'))