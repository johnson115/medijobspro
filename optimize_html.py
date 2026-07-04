import os
import re
import glob

# HTML files to process
html_files = glob.glob("*.html")

splash_html = """
  <!-- SPLASH SCREEN LOADER -->
  <style>
    #global-loader {
      position: fixed;
      inset: 0;
      z-index: 99999;
      background-color: #00263f;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    #global-loader.hide {
      opacity: 0;
      visibility: hidden;
    }
    .loader-pulse {
      position: relative;
      width: 80px;
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .loader-pulse::before, .loader-pulse::after {
      content: '';
      position: absolute;
      border: 3px solid #c9a76f;
      border-radius: 50%;
      animation: pulseRipple 2s linear infinite;
    }
    .loader-pulse::after {
      animation-delay: 1s;
    }
    .loader-cross {
      width: 30px;
      height: 30px;
      position: relative;
      background: #c9a76f;
      clip-path: polygon(33% 0, 66% 0, 66% 33%, 100% 33%, 100% 66%, 66% 66%, 66% 100%, 33% 100%, 33% 66%, 0 66%, 0 33%, 33% 33%);
      animation: heartbeat 1.5s ease-in-out infinite;
    }
    @keyframes pulseRipple {
      0% { width: 40px; height: 40px; opacity: 1; }
      100% { width: 120px; height: 120px; opacity: 0; }
    }
    @keyframes heartbeat {
      0%, 100% { transform: scale(1); }
      15% { transform: scale(1.15); }
      30% { transform: scale(1); }
      45% { transform: scale(1.15); }
      60% { transform: scale(1); }
    }
  </style>
  <div id="global-loader">
    <div class="loader-pulse">
      <div class="loader-cross"></div>
    </div>
    <div style="margin-top: 30px; color: #fff; font-family: 'Manrope', sans-serif; font-weight: 700; font-size: 1.25rem; letter-spacing: 2px;">
      Medijobs Pro
    </div>
  </div>
  <script>
    window.addEventListener('load', function() {
      const loader = document.getElementById('global-loader');
      if (loader) {
        setTimeout(() => { loader.classList.add('hide'); }, 400);
      }
    });
  </script>
  <!-- END SPLASH SCREEN -->
"""

preconnect_html = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="css/styles.css">
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove CDN script
    content = re.sub(r'<script src="https://cdn\.tailwindcss\.com\?.*?"></script>\s*', '', content)

    # 2. Remove inline config script
    content = re.sub(r'<script id="tailwind-config">.*?</script>\s*', '', content, flags=re.DOTALL)

    # 3. Add Preconnect & Compiled CSS link
    if '<link rel="stylesheet" href="css/styles.css">' not in content:
        # Insert before the first font link
        content = re.sub(
            r'(<link href="https://fonts\.googleapis\.com.*?>)', 
            f'{preconnect_html}\\1', 
            content, 
            count=1
        )

    # 4. Inject Splash Screen
    if 'global-loader' not in content:
        content = re.sub(
            r'(<body[^>]*>)', 
            f'\\1\n{splash_html}', 
            content, 
            count=1
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML Optimization and Splash Screen injected successfully!")
