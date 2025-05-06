class DomainLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Az aktuális domain lekérése a kérésből
        domain = request.get_host()
        
        # Nyelvválasztás domain alapján
        if domain.endswith('.sk'):
            # Slovak domain esetén szlovák nyelv beállítása
            request.LANGUAGE_CODE = 'sk'
            # A Django beépített nyelvi cookie-jának beállítása
            response = self.get_response(request)
            response.set_cookie('django_language', 'sk')
            return response
        else:
            # Minden más esetben magyar nyelv (alapértelmezett)
            request.LANGUAGE_CODE = 'hu'
            # A Django beépített nyelvi cookie-jának beállítása
            response = self.get_response(request)
            response.set_cookie('django_language', 'hu')
            return response