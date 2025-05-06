document.addEventListener('DOMContentLoaded', function() {
    // === Változók ===
    const translations = {}; // Fordításokhoz (jelenleg nem használt)
    const translatableElements = document.querySelectorAll('[data-lang-hu], [data-lang-sk]');
    const htmlElement = document.documentElement;
    const contactHu = document.querySelector('.contact-hungarian');
    const contactSk = document.querySelector('.contact-slovak');

    // Nyelvváltó Gomb Elemek
    const langToggleButton = document.getElementById('lang-toggle-btn');
    const currentLangFlagEl = document.getElementById('current-lang-flag');
    const currentLangTextEl = document.getElementById('current-lang-text');

    // Ellenorizzük, hogy minden elem létezik-e
    console.log('langToggleButton:', langToggleButton);
    console.log('currentLangFlagEl:', currentLangFlagEl);
    console.log('currentLangTextEl:', currentLangTextEl);
    console.log('contactHu:', contactHu);
    console.log('contactSk:', contactSk);

    // Nyelvi adatok - CSS zászló osztályok és név
    const langData = {
        hu: { flagClass: 'lang-flag-hu', name: 'Magyar' },
        sk: { flagClass: 'lang-flag-sk', name: 'Slovensky' }
    };
    
    // === Nyelv Beállítása Funkció ===
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
        // Ellenorzés és alapértelmezés
        if (!lang || !langData[lang]) {
            console.warn('Invalid language specified, defaulting to hu:', lang);
            lang = 'hu';
        }
        console.log('Setting language to:', lang);
        
        // 1. Oldal tartalmának frissítése
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

        // 2. Nyelvváltó GOMB frissítése a CÉLNYELVRE (nem az aktuálisra)
        if (langToggleButton && currentLangFlagEl && currentLangTextEl && langData[lang]) {
            // A másik nyelvet állítjuk be, mint következo célnyelv
            const nextLang = lang === 'hu' ? 'sk' : 'hu';
            
            // A CÉLNYELV adatainak megjelenítése a gombon
            currentLangFlagEl.className = `lang-flag ${langData[nextLang].flagClass}`;
            currentLangTextEl.textContent = langData[nextLang].name;
            
            // Beállítjuk a célnyelvet az attribútumban is
            langToggleButton.setAttribute('data-target-lang', nextLang);
            
            console.log('Updated button to target language:', langData[nextLang]);
        } else {
            console.error("Language toggle button elements not found or incomplete!");
        }

        // 3. Elérhetoségek láthatóságának kezelése (footer-hez)
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
            
            // Általános megközelítés (visszaesés, ha az elem nem található)
            document.querySelectorAll('[data-lang-visibility]').forEach(element => {
                const visibleForLang = element.getAttribute('data-lang-visibility');
                element.style.display = (visibleForLang === lang) ? 'block' : 'none';
                console.log(`Setting visibility for element with data-lang-visibility=${visibleForLang} to ${(visibleForLang === lang) ? 'block' : 'none'}`);
            });
        }

        // 4. Nyelv mentése localStorage-ba
        try {
            localStorage.setItem('preferredLanguage', lang);
        } catch (e) {
            console.warn('Could not save language preference to localStorage:', e);
        }
    }

    // === Kezdeti Nyelv Beállítása ===
    let initialLang = 'hu';
    try {
        const savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang && langData[savedLang]) {
            initialLang = savedLang;
        }
    } catch (e) {
        console.warn('Could not read language preference from localStorage:', e);
    }
    // Elso futáskor beállítja az oldalt és a gombot
    setLanguage(initialLang);

    // === Nyelvváltó Gomb Eseménykezelo ===
    if (langToggleButton) {
        langToggleButton.addEventListener('click', function() {
            const targetLang = this.getAttribute('data-target-lang'); // Melyik nyelvre kell váltani
            console.log('Clicked language button, target language:', targetLang);
            if (targetLang) {
                setLanguage(targetLang); // Váltás a célnyelvre
            } else {
                console.error("Target language not set on button!");
                // Vészmegoldás: próbáljuk kitalálni
                const currentActualLang = htmlElement.lang || 'hu';
                const nextLang = currentActualLang === 'hu' ? 'sk' : 'hu';
                setLanguage(nextLang);
            }
        });
    } else {
        console.error("Language toggle button (#lang-toggle-btn) not found!");
    }

    // === Mobil menü toggle ===
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
        const link = parentItem.querySelector(':scope > .nav-link'); // Csak a közvetlen link

        if (link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 992) { // Csak mobilon
                    e.preventDefault(); // Ne navigáljon
                    const wasOpen = parentItem.classList.contains('open');
                    // Összes többi bezárása
                    navItemsWithDropdown.forEach(otherDropdown => {
                        otherDropdown.parentElement.classList.remove('open');
                    });
                    // Aktuális nyitása/zárása
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