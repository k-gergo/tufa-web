document.addEventListener('DOMContentLoaded', function() {
    // === V�ltoz�k ===
    const translations = {}; // Ford�t�sokhoz (jelenleg nem haszn�lt)
    const translatableElements = document.querySelectorAll('[data-lang-hu], [data-lang-sk]');
    const htmlElement = document.documentElement;
    const contactHu = document.querySelector('.contact-hungarian');
    const contactSk = document.querySelector('.contact-slovak');

    // Nyelvv�lt� Gomb Elemek
    const langToggleButton = document.getElementById('lang-toggle-btn');
    const currentLangFlagEl = document.getElementById('current-lang-flag');
    const currentLangTextEl = document.getElementById('current-lang-text');

    // Ellenorizz�k, hogy minden elem l�tezik-e
    console.log('langToggleButton:', langToggleButton);
    console.log('currentLangFlagEl:', currentLangFlagEl);
    console.log('currentLangTextEl:', currentLangTextEl);
    console.log('contactHu:', contactHu);
    console.log('contactSk:', contactSk);

    // Nyelvi adatok - CSS z�szl� oszt�lyok �s n�v
    const langData = {
        hu: { flagClass: 'lang-flag-hu', name: 'Magyar' },
        sk: { flagClass: 'lang-flag-sk', name: 'Slovensky' }
    };
    
    // === Nyelv Be�ll�t�sa Funkci� ===
    function setLanguage(lang) {
        const contactHu = document.getElementById('contact-hu');
        const contactSk = document.getElementById('contact-sk');

        if (contactHu && contactSk) {
            if (lang === 'hu') {
                contactHu.style.display = 'block';
                contactSk.style.display = 'none';
            } else {
                contactHu.style.display = 'none';
                contactSk.style.display = 'block';
            }
        }
        // Ellenorz�s �s alap�rtelmez�s
        if (!lang || !langData[lang]) {
            console.warn('Invalid language specified, defaulting to hu:', lang);
            lang = 'hu';
        }
        console.log('Setting language to:', lang);
        
        // 1. Oldal tartalm�nak friss�t�se
        htmlElement.lang = lang;
        translatableElements.forEach(el => {
            const text = el.getAttribute(`data-lang-${lang}`);
            if (text !== null) {
                // Ellenorzi, van-e benne HTML tag (pl. a highlight miatt)
                const containsHtml = /<[a-z][\s\S]*>/i.test(text);
                if (containsHtml) {
                     el.innerHTML = text;
                } else {
                     el.textContent = text;
                }
            }
        });

        // 2. Nyelvv�lt� GOMB friss�t�se a C�LNYELVRE (nem az aktu�lisra)
        if (langToggleButton && currentLangFlagEl && currentLangTextEl && langData[lang]) {
            // A m�sik nyelvet �ll�tjuk be, mint k�vetkezo c�lnyelv
            const nextLang = lang === 'hu' ? 'sk' : 'hu';
            
            // A C�LNYELV adatainak megjelen�t�se a gombon
            currentLangFlagEl.className = `lang-flag ${langData[nextLang].flagClass}`;
            currentLangTextEl.textContent = langData[nextLang].name;
            
            // Be�ll�tjuk a c�lnyelvet az attrib�tumban is
            langToggleButton.setAttribute('data-target-lang', nextLang);
            
            console.log('Updated button to target language:', langData[nextLang]);
        } else {
            console.error("Language toggle button elements not found or incomplete!");
        }

        // 3. El�rhetos�gek l�that�s�g�nak kezel�se (footer-hez)
        if (contactHu && contactSk) {
            if (lang === 'hu') {
                contactHu.style.display = 'block';
                contactSk.style.display = 'none';
                console.log('Displaying Hungarian contacts');
            } else {
                contactHu.style.display = 'none';
                contactSk.style.display = 'block';
                console.log('Displaying Slovak contacts');
            }
        } else {
            console.warn('Contact elements not found!');
            
            // �ltal�nos megk�zel�t�s (visszaes�s, ha az elem nem tal�lhat�)
            document.querySelectorAll('[data-lang-visibility]').forEach(element => {
                const visibleForLang = element.getAttribute('data-lang-visibility');
                element.style.display = (visibleForLang === lang) ? 'block' : 'none';
                console.log(`Setting visibility for element with data-lang-visibility=${visibleForLang} to ${(visibleForLang === lang) ? 'block' : 'none'}`);
            });
        }

        // 4. Nyelv ment�se localStorage-ba
        try {
            localStorage.setItem('preferredLanguage', lang);
        } catch (e) {
            console.warn('Could not save language preference to localStorage:', e);
        }
    }

    // === Kezdeti Nyelv Be�ll�t�sa ===
    let initialLang = 'hu';
    try {
        const savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang && langData[savedLang]) {
            initialLang = savedLang;
        }
    } catch (e) {
        console.warn('Could not read language preference from localStorage:', e);
    }
    // Elso fut�skor be�ll�tja az oldalt �s a gombot
    setLanguage(initialLang);

    // === Nyelvv�lt� Gomb Esem�nykezelo ===
    if (langToggleButton) {
        langToggleButton.addEventListener('click', function() {
            const targetLang = this.getAttribute('data-target-lang'); // Melyik nyelvre kell v�ltani
            console.log('Clicked language button, target language:', targetLang);
            if (targetLang) {
                setLanguage(targetLang); // V�lt�s a c�lnyelvre
            } else {
                console.error("Target language not set on button!");
                // V�szmegold�s: pr�b�ljuk kital�lni
                const currentActualLang = htmlElement.lang || 'hu';
                const nextLang = currentActualLang === 'hu' ? 'sk' : 'hu';
                setLanguage(nextLang);
            }
        });
    } else {
        console.error("Language toggle button (#lang-toggle-btn) not found!");
    }

    // === Mobil men� toggle ===
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navList = document.querySelector('.nav-list');
    const navItemsWithDropdown = document.querySelectorAll('.nav-item > .dropdown');

    if (mobileNavToggle && navList) {
        mobileNavToggle.addEventListener('click', function() {
            navList.classList.toggle('active');
            if (!navList.classList.contains('active')) {
                navItemsWithDropdown.forEach(dropdown => {
                    dropdown.parentElement.classList.remove('open');
                });
            }
        });
    }

    // === Mobil Dropdown Toggle ===
    navItemsWithDropdown.forEach(dropdown => {
        const parentItem = dropdown.parentElement;
        const link = parentItem.querySelector(':scope > .nav-link'); // Csak a k�zvetlen link

        if (link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 992) { // Csak mobilon
                    e.preventDefault(); // Ne navig�ljon
                    const wasOpen = parentItem.classList.contains('open');
                    // �sszes t�bbi bez�r�sa
                    navItemsWithDropdown.forEach(otherDropdown => {
                        otherDropdown.parentElement.classList.remove('open');
                    });
                    // Aktu�lis nyit�sa/z�r�sa
                    if (!wasOpen) {
                        parentItem.classList.add('open');
                    }
                }
            });
        }
    });

    // === Intersection Observer for animations ===
    const animateItems = document.querySelectorAll('.category-card, .product-card, .about-content, .about-image');
    const observerOptions = { threshold: 0.1 };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    animateItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = item.classList.contains('category-card') ? 'translateY(30px)' : 'translateY(20px)';
        item.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(item);
    });
}); 