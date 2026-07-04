import os
import re

directory = r"c:\Users\ASUS\Desktop\johnsnow\italy project\ahmed agency\pre final desing choosed"

html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

seo_data = {
    "index.html": {
        "title": "Medijobs Pro — Recrutement Médical en Allemagne",
        "desc": "Agence spécialisée dans le recrutement et l'accompagnement des professionnels de santé vers l'Allemagne. Infirmiers, techniciens, accompagnement complet."
    },
    "about.html": {
        "title": "À propos de Medijobs Pro | Recrutement Médical",
        "desc": "Découvrez l'histoire, la mission et l'équipe derrière Medijobs Pro, votre partenaire de confiance pour travailler en Allemagne."
    },
    "candidates.html": {
        "title": "Candidats | Postulez pour travailler en Allemagne",
        "desc": "Démarrez votre carrière médicale en Allemagne. Découvrez notre processus d'accompagnement et postulez en ligne dès aujourd'hui."
    },
    "entreprise.html": {
        "title": "Entreprises & Hôpitaux | Recrutez du personnel qualifié",
        "desc": "Partenaires de santé en Allemagne : trouvez le personnel infirmier qualifié dont vous avez besoin avec Medijobs Pro."
    },
    "contact.html": {
        "title": "Contact | Medijobs Pro",
        "desc": "Contactez Medijobs Pro pour toute question concernant le recrutement médical en Allemagne. Nous sommes là pour vous aider."
    }
}

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove inline JS for lang toggles to prevent conflict with lang.js
    content = re.sub(r'const langToggleBtn = document\.getElementById\(\'lang-toggle-btn\'\);.*?\}\s*\}\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'const mobileLangBtn = document\.getElementById\(\'mobile-lang-toggle-btn\'\);.*?\}\s*\}\s*', '', content, flags=re.DOTALL)

    # 2. Add SEO / OpenGraph
    data = seo_data.get(filename, {"title": "Medijobs Pro", "desc": "Medijobs Pro"})
    
    seo_tags = f"""<meta name="description" content="{data['desc']}"/>
<meta property="og:title" content="{data['title']}" />
<meta property="og:description" content="{data['desc']}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="https://medijobspro.com/media/employer_hero.png" />
<meta property="og:site_name" content="Medijobs Pro" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{data['title']}" />
<meta name="twitter:description" content="{data['desc']}" />"""

    # Remove existing <title> and <meta name="description">
    content = re.sub(r'<title>.*?</title>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<meta name="description" content=".*?"\s*/?>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Insert new tags
    insert_pos = '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>'
    replacement = f'{insert_pos}\n<title>{data["title"]}</title>\n{seo_tags}'
    content = content.replace(insert_pos, replacement)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filename}")
