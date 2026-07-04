import os
import re

directory = r"c:\Users\ASUS\Desktop\johnsnow\italy project\ahmed agency\pre final desing choosed"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # In about.html we have:
    #    // Mobile lang toggle
    #    );
    #    }
    content = re.sub(r'// Mobile lang toggle\s*\);\s*\}', '', content)

    # In candidates.html, contact.html, entreprise.html we have:
    #    // Mobile menu toggle
    #    document.getElementById('mobile-menu-btn').addEventListener('click', () => {
    #      document.getElementById('mobile-menu').classList.toggle('hidden');
    #    });
    content = re.sub(r'// Mobile menu toggle\s*document\.getElementById\(\'mobile-menu-btn\'\)\.addEventListener\(\'click\', \(\) => \{\s*document\.getElementById\(\'mobile-menu\'\)\.classList\.toggle\(\'hidden\'\);\s*\}\);', '', content)
    
    # Also another variant in candidates.html:
    #    /* 📱 Mobile menu toggle 📱 */
    #    const mobileBtn = document.getElementById('mobile-menu-btn');
    #    const mobileMenu = document.getElementById('mobile-menu');
    #    if (mobileBtn && mobileMenu) {
    #      mobileBtn.addEventListener('click', () => {
    #        mobileMenu.classList.toggle('hidden');
    #      });
    #    }
    content = re.sub(r'/\*.*Mobile menu toggle.*\*/\s*const mobileBtn = document\.getElementById\(\'mobile-menu-btn\'\);\s*const mobileMenu = document\.getElementById\(\'mobile-menu\'\);\s*if \(mobileBtn && mobileMenu\) \{\s*mobileBtn\.addEventListener\(\'click\', \(\) => \{\s*mobileMenu\.classList\.toggle\(\'hidden\'\);\s*\}\);\s*\}', '', content)

    # In entreprise.html line 653:
    #    // Mobile menu toggle
    #    const mobileBtn = document.getElementById('mobile-menu-btn');
    #    const mobileMenu = document.getElementById('mobile-menu');
    #    if (mobileBtn && mobileMenu) {
    #      mobileBtn.addEventListener('click', () => {
    #        mobileMenu.classList.toggle('open');
    #      });
    #    }
    content = re.sub(r'// Mobile menu toggle\s*const mobileBtn = document\.getElementById\(\'mobile-menu-btn\'\);\s*const mobileMenu = document\.getElementById\(\'mobile-menu\'\);\s*if \(mobileBtn && mobileMenu\) \{\s*mobileBtn\.addEventListener\(\'click\', \(\) => \{\s*mobileMenu\.classList\.toggle\(\'(?:open|hidden)\'\);\s*\}\);\s*\}', '', content)

    # In index.html and about.html:
    #  // Mobile menu toggle
    #  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    #  const mobileMenu = document.getElementById('mobile-menu');
    #  if (mobileMenuBtn && mobileMenu) {
    #    mobileMenuBtn.addEventListener('click', () => {
    #      mobileMenu.classList.toggle('hidden');
    #    });
    #  }
    content = re.sub(r'// Mobile menu toggle\s*const mobileMenuBtn = document\.getElementById\(\'mobile-menu-btn\'\);\s*const (?:mobileMenu|mobileMenuEl) = document\.getElementById\(\'mobile-menu\'\);\s*if \(mobileMenuBtn && (?:mobileMenu|mobileMenuEl)\) \{\s*mobileMenuBtn\.addEventListener\(\'click\', \(\) => (?:\{\s*(?:mobileMenu|mobileMenuEl)\.classList\.toggle\(\'hidden\'\);\s*\}|(?:mobileMenu|mobileMenuEl)\.classList\.toggle\(\'hidden\'\))\);\s*\}', '', content)

    # Any remaining mobile lang toggle
    content = re.sub(r'// Mobile lang toggle\s*const mlBtn = document\.getElementById\(\'mobile-lang-toggle-btn\'\);\s*const mlMenu = document\.getElementById\(\'mobile-lang-menu\'\);\s*if \(mlBtn && mlMenu\) \{\s*mlBtn\.addEventListener\(\'click\', \(\) => \{\s*mlMenu\.classList\.toggle\(\'hidden\'\);\s*mlMenu\.classList\.toggle\(\'flex\'\);\s*\}\);\s*\}', '', content)

    # Any remaining Language dropdown toggle
    content = re.sub(r'(?://|/\*.*)\s*Language dropdown\s*(?:toggle)?.*\s*const langBtn\s*=\s*document\.getElementById\(\'lang-toggle-btn\'\);\s*const langMenu\s*=\s*document\.getElementById\(\'lang-menu\'\);\s*if \(langBtn && langMenu\) \{\s*langBtn\.addEventListener\(\'click\', \(e\) => \{\s*e\.stopPropagation\(\);\s*langMenu\.classList\.toggle\(\'hidden\'\);\s*\}\);\s*document\.addEventListener\(\'click\', \(\) => langMenu\.classList\.add\(\'hidden\'\)\);\s*\}', '', content)
    
    # Inline entreprise.html variant:
    content = re.sub(r'// Language dropdown\s*const langBtn = document\.getElementById\(\'lang-toggle-btn\'\);\s*const langMenu = document\.getElementById\(\'lang-menu\'\);\s*if \(langBtn && langMenu\) \{\s*langBtn\.addEventListener\(\'click\', \(e\) => \{ e\.stopPropagation\(\); langMenu\.classList\.toggle\(\'hidden\'\); \}\);\s*document\.addEventListener\(\'click\', \(\) => langMenu\.classList\.add\(\'hidden\'\)\);\s*\}', '', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")
