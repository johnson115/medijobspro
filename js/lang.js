// Medijobs Pro — Language Detection & Application Engine
// Geo-detects language based on user's country, with manual override support.

(function () {
  const SUPPORTED = ['fr', 'en', 'de', 'ar'];
  const DEFAULT_LANG = 'en';
  const STORAGE_KEY = 'mjp-lang';

  // Derive current page name for active nav highlighting
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  function getNestedValue(obj, keyPath) {
    return keyPath.split('.').reduce((acc, k) => acc && acc[k], obj);
  }

  function applyTranslations(lang) {
    const t = translations[lang];
    if (!t) return;

    // RTL for Arabic
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

    // Apply all [data-i18n] elements
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = getNestedValue(t, key);
      if (val && typeof val === 'string') {
        el.textContent = val;
      }
    });

    // Apply [data-i18n-placeholder] elements
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      const val = getNestedValue(t, key);
      if (val && typeof val === 'string') {
        el.placeholder = val;
      }
    });

    // Update language toggle display
    const currentLangEl = document.getElementById('current-lang-label');
    const mobileCurrentLangEl = document.getElementById('mobile-current-lang-label');
    const flags = { fr: '🇫🇷 FR', en: '🇬🇧 EN', de: '🇩🇪 DE', ar: '🇹🇳 AR' };
    const labelText = flags[lang] || lang.toUpperCase();
    if (currentLangEl) {
      currentLangEl.textContent = labelText;
    }
    if (mobileCurrentLangEl) {
      mobileCurrentLangEl.textContent = labelText;
    }

    // Highlight active lang button
    document.querySelectorAll('.lang-option-btn').forEach(btn => {
      const isActive = btn.dataset.lang === lang;
      btn.classList.toggle('font-bold', isActive);
      btn.classList.toggle('text-secondary', isActive);
    });

    // Save choice
    localStorage.setItem(STORAGE_KEY, lang);
  }

  function detectAndApply() {
    // 1. Check stored preference
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored && SUPPORTED.includes(stored)) {
      applyTranslations(stored);
      return;
    }

    // 2. Geo-detect via free API
    fetch('https://ipapi.co/json/', { cache: 'force-cache' })
      .then(r => r.json())
      .then(data => {
        const country = data.country_code;
        let lang = DEFAULT_LANG;
        if (country === 'DE' || country === 'AT' || country === 'CH') {
          lang = 'de';
        } else if (country === 'TN') {
          lang = 'fr';
        } else if (['FR', 'BE', 'MA', 'DZ'].includes(country)) {
          lang = 'fr';
        }
        applyTranslations(lang);
      })
      .catch(() => {
        // Fallback: check browser language
        const browserLang = navigator.language?.slice(0, 2).toLowerCase();
        const lang = SUPPORTED.includes(browserLang) ? browserLang : DEFAULT_LANG;
        applyTranslations(lang);
      });
  }

  // Toggle dropdown visibility
  function setupLangToggle() {
    // Mobile Hamburger Menu
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        mobileMenu.classList.toggle('open');
      });
    }

    // Desktop lang dropdown
    const desktopLangBtn = document.getElementById('lang-toggle-btn');
    const desktopLangMenu = document.getElementById('lang-menu');
    if (desktopLangBtn && desktopLangMenu) {
      desktopLangBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        desktopLangMenu.classList.toggle('hidden');
      });
      document.addEventListener('click', (e) => {
        if (!desktopLangMenu.contains(e.target) && !desktopLangBtn.contains(e.target)) {
          desktopLangMenu.classList.add('hidden');
        }
      });
    }

    // Mobile lang dropdown
    const mobileLangBtn = document.getElementById('mobile-lang-toggle-btn');
    const mobileLangMenu = document.getElementById('mobile-lang-menu');
    if (mobileLangBtn && mobileLangMenu) {
      mobileLangBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isHidden = mobileLangMenu.classList.contains('hidden');
        if (isHidden) {
          mobileLangMenu.classList.remove('hidden');
          mobileLangMenu.classList.add('flex');
        } else {
          mobileLangMenu.classList.add('hidden');
          mobileLangMenu.classList.remove('flex');
        }
      });
    }
  }

  // Highlight current nav page
  function highlightCurrentNav() {
    document.querySelectorAll('[data-nav-page]').forEach(link => {
      const page = link.dataset.navPage;
      if (currentPage === page || (currentPage === '' && page === 'index.html')) {
        link.classList.add('text-secondary', 'border-b-2', 'border-secondary');
        link.classList.remove('text-on-surface-variant');
      }
    });
  }

  // Public API for onclick buttons
  window.setLang = function (lang) {
    if (SUPPORTED.includes(lang)) {
      applyTranslations(lang);
      // Close desktop lang menu
      const langMenu = document.getElementById('lang-menu');
      if (langMenu) langMenu.classList.add('hidden');
      // Close mobile lang menu
      const mobileLangMenu = document.getElementById('mobile-lang-menu');
      if (mobileLangMenu) {
        mobileLangMenu.classList.add('hidden');
        mobileLangMenu.classList.remove('flex');
      }
    }
  };

  // Init
  document.addEventListener('DOMContentLoaded', () => {
    setupLangToggle();
    highlightCurrentNav();
    detectAndApply();
  });

})();
