# Tufa Machine weboldal

A weboldal django-t használ, ami htmlx templateket tölt be. A django kezeli az admin felületet.

## Beállítás

1. **Klónozd a github repository-t**

2. **Hozz létre egy virtuális py környezetet**

3. **Töltsd le a szükséges könyvtárakat: pip install -r requirements.txt**

4. **Az adatbázis beállításához szükséges migráció: python manage.py migrate**

5. **Hozz létre egy superusert (admin) név, email, jelszó szükséges**

6. **Teszteléshez developement szerver futtatása (localhost:8000): python manage.py runserver**

7. **Statikus filok gyüjtését érdemes lehet futtatni: python manage.py collectstatic**

9. **Webszerer beállítása**

10. **Én gunicorn és nginx kombót használtam, certbot-al*

